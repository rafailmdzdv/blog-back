import time
from collections.abc import Generator

import pytest


@pytest.fixture(scope='session')
def django_db_modify_db_settings(
    setup_postgres: None,
    django_db_modify_db_settings_parallel_suffix: None,
) -> None:
    from django.conf import settings

    settings.DATABASES['default']['HOST'] = 'localhost'
    settings.DATABASES['default']['PORT'] = '5436'
    settings.DATABASES['default']['USER'] = 'test'
    settings.DATABASES['default']['PASSWORD'] = 'test'
    settings.DATABASES['default']['NAME'] = 'test'


@pytest.fixture(scope='session')
def setup_postgres() -> Generator[None, None, None]:
    import docker

    client = docker.from_env()
    container = client.containers.run(
        'postgres:17.5',
        environment={
            'POSTGRES_USER': 'test',
            'POSTGRES_PASSWORD': 'test',
            'POSTGRES_DB': 'test',
        },
        ports={'5432': 5436},
        detach=True,
    )
    while container.status != 'running':
        container.reload()
        time.sleep(1)
        continue
    yield
    container.remove(force=True)


pytest_plugins = ('it.fixtures',)
