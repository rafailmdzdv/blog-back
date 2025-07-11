uv run --no-sync python src/manage.py migrate
uv run --no-sync python src/manage.py collectstatic --clear --no-input

exec "$@"
