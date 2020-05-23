import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='123', host='localhost')


class Record(object):
    def __init__(self, record_id, camera_id, fileName, fileSize, fileExtension, duration, timeStart, timeFinish,
                 savedOn, note):
        # Constructor of the Record's class
        self.record_id = record_id
        self.camera_id = camera_id
        self.fileName = fileName
        self.fileSize = fileSize
        self.fileExtension = fileExtension
        self.duration = duration
        self.timeStart = timeStart
        self.timeFinish = timeFinish
        self.savedOn = savedOn
        self.note = note

    def addRecord(self):
        # Method of adding the Record into DataBase
        try:
            cur = conn.cursor()
            # execute the INSERT statement
            sql = "INSERT INTO \"Record\" VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql, (self.record_id, self.camera_id, self.fileName, self.fileSize, self.fileExtension,
                              self.duration, self.timeStart, self.timeFinish, self.savedOn, self.note))
            # commit the changes to the database
            conn.commit()
            count = cur.rowcount
            print(count, "addRecord success")

        except (Exception, psycopg2.Error) as error:
            if conn:
                print("addRecord failed", error)

        finally:
            # closing database connection.
            if conn:
                cur.close()
                conn.close()
                print("PostgreSQL connection is closed")
