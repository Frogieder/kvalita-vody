# sudo docker run -p 8086:8086 -v "$PWD":/var/lib/influxdb2 influxdb
npm install
npm run build

docker compose up -d --build
