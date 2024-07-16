import psycopg2
import sys
import logging

log = logging.getLogger(__name__)

class DataBase:
    def __init__(self) -> None: 
        try: 
            self.con = psycopg2.connect(
                database = 'test',
                user = 'test',
                password = 'test',
                host = '127.0.0.1',
                port = 5432
                )
            log.info('PostgreSQL Connected...')
        except psycopg2.Error as e:
            log.error(f'PostgreSQL ERROR: {e}')
            sys.exit(1)

        self.cur = self.con.cursor()

    def create_table(self) -> None:
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL)")
        self.con.commit()
        log.debug('Creating table...')
        self.con.close()

    def get_user(self, username: str, password: str) -> bool:
        self.cur.execute("SELECT password FROM users WHERE username=%s", (username, ))
        passw = self.cur.fetchone()
        self.con.close()
        try:
            if passw == None:
                return False
            elif password != passw[0]:
                return False
            elif password == passw[0]:
                return True
        except:
            return False
        
    def register_user(self, username: str, password: str) -> bool:
        try:
            self.cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            self.con.commit()
            self.con.close()
            return True
        except psycopg2.errors.UniqueViolation:
            return False