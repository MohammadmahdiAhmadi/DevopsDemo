Docker run command:

docker run -d \
  --name ideablog-back \
  -p 8005:8005 \
  -v $(pwd)/db_data:/usr/scr/ideablog/db.sqlite3 \
  -v /usr/src/ideablog/.env:/usr/src/ideablog/.env \
  -w /usr/src/ideablog \
  --restart unless-stopped \
  --network ideablog-net \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=5 \
  ideablog:latest \
  gunicorn --chdir ideablog --bind :8005 --timeout 300 ideablog.wsgi:application


Docker compose:

docker-compose up -d
docker-compose down -v
