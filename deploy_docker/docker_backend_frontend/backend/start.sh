APP_FOLDER="/backend/app"

sed -i -e "s+localUrl: .*+localUrl: '${localURL}'+" ${APP_FOLDER}/config/database.js

node ${APP_FOLDER}/server.js