import Camera
import Server
import Record
import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='123', host='localhost')


def findAllServers():
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "SELECT * FROM \"Server\""
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        for row in cur:
            print(row)
        count = cur.rowcount
        print(count, "findAllServers success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("findAllServers failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def findAllCameras():
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "SELECT * FROM \"Camera\""
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        for row in cur:
            print(row)
        count = cur.rowcount
        print(count, "findAllCameras success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("findAllCameras failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def findAllPairs():
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "SELECT * FROM \"Camera\" WHERE server_id>0"
        cur.execute(sql)
        # commit the changes to the database
        conn.commit()
        for row in cur:
            print(row)
        count = cur.rowcount
        print(count, "findAllPairs success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("findAllPairs failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def ServerByCamID(camera_id):
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "SELECT * FROM \"Server\" JOIN \"Camera\" on  \"Camera.server_id=Server.server_id\" WHERE " \
              "\"Camera.camera_id=%s\">0"
        cur.execute(sql, camera_id)
        # commit the changes to the database
        conn.commit()
        for row in cur:
            print(row)
        count = cur.rowcount
        print(count, "ServerByCamID success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("ServerByCamID failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def findCamerasByServerId(server_id):
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "SELECT * FROM \"Camera\" JOIN \"Server\" on  \"Server.server_id=Camera.server_id\" WHERE " \
              "\"Camera.server_id=%s\">0"
        cur.execute(sql, server_id)
        # commit the changes to the database
        conn.commit()
        for row in cur:
            print(row)
        count = cur.rowcount
        print(count, "findCamerasByServerId success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("findCamerasByServerId failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def runRoundRobin():
    """
    runRoundRobin implementation
    :return:
    """


def bindCameraWithServer(camera_id,server_id):
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "UPDATE \"Camera\" SET 'server_id' = %s WHERE 'camera_id' = '%s'"
        cur.execute(sql, server_id, camera_id)
        # commit the changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "bindCameraWithServer success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("bindCameraWithServer failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")


def unbindCamera(camera_id):
    try:
        cur = conn.cursor()
        # execute the INSERT statement
        sql = "UPDATE \"Camera\" SET 'server_id' = 0 WHERE 'camera_id' = '%s'"
        cur.execute(sql, camera_id)
        # commit the changes to the database
        conn.commit()
        count = cur.rowcount
        print(count, "unbindCamera success")

    except (Exception, psycopg2.Error) as error:
        if conn:
            print("unbindCamera failed", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")
