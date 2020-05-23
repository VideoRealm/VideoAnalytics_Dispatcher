import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='123', host='localhost')


class Camera(object):
    def __init__(self, camera_id, server_id, networkAddress, location, productName, vendor, registeredOn, lastUpdateOn, note):
        # Constructor of the Camera's class
        self.camera_id = camera_id
        self.server_id = server_id
        self.networkAddress = networkAddress
        self.location = location
        self.productName = productName
        self.vendor = vendor
        self.registeredOn = registeredOn
        self.lastUpdateOn = lastUpdateOn
        self.note = note

    def addCamera(self):
        # Method of adding the camera into DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "INSERT INTO \"Camera\" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, (self.camera_id, self.server_id, self.networkAddress, self.location, self.productName, self.vendor, self.registeredOn,
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

    def changeNetworkAddress(self):
        # Method of changing the network Address in DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Camera\" SET 'NetworkAddress' = %s WHERE 'camera_id' = '%s'"
            cur.execute(sql, self.networkAddress, self.camera_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "changeNetworkAddress success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("changeNetworkAddress failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def setCameraUpdate(self):
        # Method of changing the lastUpdateOn parameter in DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Camera\" SET 'lastUpdateOn' = %s WHERE 'camera_id' = '%s'"
            cur.execute(sql, self.lastUpdateOn, self.camera_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "setCameraUpdate success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("setCameraUpdate failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def bindWithServer(self):
        # Method of binding the camera to Server
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Camera\" SET 'sever_id' = %s WHERE 'camera_id' = '%s'"
            cur.execute(sql, (self.server_id, self.camera_id))
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "bindWithServer success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("bindWithServer failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def unbind(self):
        # Method of unbinding the camera to Server
        # Method of binding the camera to Server
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "UPDATE \"Camera\" SET sever_id = 0 WHERE camera_id = %s"
            cur.execute(sql, self.camera_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "unbind success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("unbind failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def delete(self):
        # Method of deleting the camera in DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "DELETE FROM \"Camera\" WHERE camera_id = %s"
            cur.execute(sql, self.camera_id)
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "delete Camera success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("delete Camera failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")
