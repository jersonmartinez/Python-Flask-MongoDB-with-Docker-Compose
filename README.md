# Python-Flask-MongoDB-with-Docker-Compose
Launching Tech Stack in order to Python, Flask Framework and MongoDB with Docker Compose



### Remove volumes
We have two ways to remove our volumes with Docker.

First is using `prune` command.

```bash
docker volume prune -f
```

Second is using the current command `volume rm` with `-f` like parameter.

```bash
docker volume rm $(docker volume ls -q)
```

#### Delete All

```bash
rm -rf mongo-volume app/__pycache__/ && mkdir mongo-volume
```

### Delete cache

```bash
docker system prune -a -f && docker builder prune -a -f
```

### Recreate container web

```bash
docker-compose up --build --force-recreate --no-deps -d web
```

### Show logs of API Execution

```bash
docker logs --tail 1000 -f cs_api
```