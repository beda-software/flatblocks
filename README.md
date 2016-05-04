FlatBlocks example
===============

# Build

```bash
docker-compose build
docker-compose up

docker-compose run --rm server ./manage.py migrate
docker-compose run --rm server ./manage.py createsuperuser
```

# Use
```bash
docker-compose up
```

Server starts on http://localhost:3000 by default

If you want another host, change it in docker-compose.override.yml environment:
```
FRONTEND_DEV_HOST: '10.211.55.8'
```
