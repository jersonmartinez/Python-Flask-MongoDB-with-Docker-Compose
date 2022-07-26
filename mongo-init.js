db.createUser(
    {
        user: 'root-crashell',
        pwd: 'password-crashell',
        roles: [
            { role: "clusterMonitor", db: "admin" },
            { role: "dbOwner", db: "db_name" },
            { role: 'readWrite', db: 'db_crashell' }
        ]
    }
)