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

Frontend server starts on `http://localhost:3000` by default

If you use another host (for example, across docker-machine), change it in `docker-compose.override.yml` environment:
```
FRONTEND_DEV_HOST: '10.211.55.8'
```

Backend server starts on `http://localhost:8000`
Admin url is `http://localhost:8000/admin/`

Also change appropriate constant settings in Admin panel (`FRONTEND_SITE_URL`, `BACKEND_SITE_URL`) for correct image displaying
