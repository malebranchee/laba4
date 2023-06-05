def login_check():
        with open('login.txt', 'r') as file:
            lines = file.readlines()
            database = dict()
            for x in lines:
                log, password = x.split(':')[0], x.split(':')[1]
                password = password[:-1]
                database[log] = password
            return database
            close()

