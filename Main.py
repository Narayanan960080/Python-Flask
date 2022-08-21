
class MainData:
    DBName = "shashonk"
    DBPassword = "12345"
    DBHost = "127.0.0.1"
    User = "root"

    def MySqlConnect(app):
        app.config['MYSQL_HOST'] = MainData.DBHost
        app.config['MYSQL_USER'] = MainData.User
        app.config['MYSQL_PASSWORD'] = MainData.DBPassword
        app.config['MYSQL_DB'] = MainData.DBName
        return app