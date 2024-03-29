import psycopg2
import InventoryCoreCredentials as credentials


class PGInventoryDataAccess:

    def getConnection():
        conn = psycopg2.connect(
            host=credentials.host,
            port=credentials.port,
            database=credentials.database,
            user=credentials.user,
            password=credentials.password)
        return conn


    def connect():
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters
            #params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = PGInventoryDataAccess.getConnection()
            
            # create a cursor
            cur = conn.cursor()
            
        # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
        
        # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


if __name__ == '__main__':
    PGInventoryDataAccess.connect()