
class Config:
    DBName = "shashonk"
    DBPassword = "12345"
    DBHost = "127.0.0.1"
    User = "root"

    def MySqlConnect(app):
        app.config['MYSQL_HOST'] = Config.DBHost
        app.config['MYSQL_USER'] = Config.User
        app.config['MYSQL_PASSWORD'] = Config.DBPassword
        app.config['MYSQL_DB'] = Config.DBName
        return app