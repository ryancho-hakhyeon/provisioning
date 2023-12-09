db.createUser(
    {
        user: "${DB_USER}",
        pwd: "${DB_PASSWORD}",
        roles: [
            {
                role: "readWrite",
                db: "${MONGO_INITDB_DATABASE}"
            }
        ]
    }
);