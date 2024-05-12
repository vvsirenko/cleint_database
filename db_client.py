from typing import Optional

import psycopg2


class PostgresClient:

    def __init__(self, db_config: dict):
        self.db_config = db_config
        self.user = self.db_config.get('user')
        self.password = self.db_config.get('password')
        self.database = self.db_config.get('database')
        self.host = self.db_config.get('host')
        self.port = self.db_config.get('port')

    def get_connection(self):
        return psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def insert(self, table_name: str, data: list[dict]) -> str:
        """
        INSERT INTO product (store_id,  url,  price,  charecteristics,  color,  dimensions)
        VALUES (%(store_id)s, %(url)s, %(price)s, %(charecteristics)s, %(color)s, %(dimensions)s ); 495
        """
        conn = self.get_connection()
        curr = conn.cursor()
        try:
            sql = '''
                INSERT INTO %s (%s)
                VALUES (%%(%s)s );
                ''' % (table_name, ',  '.join(data[0]), ')s, %('.join(data[0]))
            for item in data:
                curr.execute(sql, item)
            conn.commit()
            print(f"Insertion successful to table: {table_name}")
        except psycopg2.IntegrityError as e:
            conn.rollback()
            print(f"Duplicate key violation occurred. Ignoring the duplicate entry. Error: {e}")
        except Exception as e:
            print(f"Connection error as {e}")
        finally:
            curr.close()
            conn.close()

    def select(self, table_name: str) -> Optional[list]:
        result = []
        conn = self.get_connection()
        curr = conn.cursor()
        try:
            sql = "SELECT * FROM %s" % (table_name)

            curr.execute(sql)
            result = curr.fetchall()
            print(f"Select successful to table: {table_name}")
        except Exception as e:
            print(f"Connection error as {e}")
        finally:
            curr.close()
            conn.close()
            return result