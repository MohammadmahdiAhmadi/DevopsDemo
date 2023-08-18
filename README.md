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


# ToDo
1. Fix static files bug in docker



docker run -d \
  --name ideablog-back \
  -p 8005:8005 \
  -e DEBUG='1' \
  -e SECRET_KEY='SECRET_KEY' \
  -e DJANGO_ALLOWED_HOSTS='localhost,127.0.0.1,[::1],ideablog.fesenjoon.xyz' \
  mmahmadi0101/ideablog:latest


# Some temp commands
kubectl logs -f ingress-nginx-controller-6cc5ccb977-9djf8 -n ingress-nginx
openssl req -x509 -newkey rsa:4096 -keyout tls.key -out tls.crt -days 365 -nodes -subj "/CN=ideablog.com"
minikube addons enable ingress
minikube ip