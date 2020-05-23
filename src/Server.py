import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='123', host='localhost')


class Server(object):
    def __init__(self, server_id, networkAddress, productName, vendor, registeredOn, lastUpdateOn, note):
        # Constructor of the Server's class
        self.server_id = server_id
        self.networkAddress = networkAddress
        self.productName = productName
        self.vendor = vendor
        self.registeredOn = registeredOn
        self.lastUpdateOn = lastUpdateOn
        self.note = note

    def add(self):
        # Method of adding the server into DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "INSERT INTO \"Server\" VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, (self.server_id, self.networkAddress, self.productName, self.vendor, self.registeredOn,
                              self.lastUpdateOn, self.note))
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "addCamera success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("addCamera failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def setServerUpdate(self):
        # Method of changing the lastUpdateOn parameter in DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Server\" SET lastUpdateOn = %s WHERE server_id = %s"
            cur.execute(sql, self.lastUpdateOn, self.server_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "setServerUpdate success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("setServerUpdate failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def changeNetworkAddress(self):
        # Method of changing the network Address in DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Server\" SET 'NetworkAddress' = %s WHERE server_id = %s"
            cur.execute(sql, self.networkAddress, self.server_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "changeNetworkAddress Server success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("changeNetworkAddress Server failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def connectCamera(self):
        # Method of connecting camera to Server
        """
        """

    def videoCapture(self):
        # Method of capturing the video from Camera
        """
        """

    def detachAnalytics(self):
        # Method of detaching Analytics from Server
        """
        """

    def startRecording(self):
        # Method of start recording from Camera
        """
        """

    def stopRecording(self):
        # Method of stop recording from Camera
        """
        """

    def compileRecord(self):
        # Method of compile the record
        """
        """

    def delete(self):
        # Method of deleting server
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "DELETE FROM \"Server\" WHERE server_id = %s"
            cur.execute(sql, self.server_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "delete Server success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("delete Server failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")
