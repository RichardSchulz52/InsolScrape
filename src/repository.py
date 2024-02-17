import os
import psycopg2


class Repository:

    def __init__(self) -> None:
        self.con = None
        self.cur = None

        self.host = os.environ['host']
        self.port = os.environ['port']
        self.dbname = os.environ['dbname']
        self.user = os.environ['user']
        self.password = os.environ['password']

    def open(self):
        self.con = psycopg2.connect(host=self.host,
                                    port=self.port,
                                    dbname=self.dbname,
                                    user=self.user,
                                    password=self.password)
        self.cur = self.con.cursor()
        self.create_table()

    def insert_data(self, insolvency):
        pass  # TODO

    def close(self):
        self.cur.close()
        self.con.close()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS insolvency (
            id integer PRIMARY KEY,
            reference_number VARCHAR(250),
            publication_date date,
            curt VARCHAR(250),
            name VARCHAR(250),
            residence VARCHAR(50)
            ) """)
        self.con.commit()
