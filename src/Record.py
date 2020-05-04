class Record(object):
    def __init__(self, camera, fileName, fileSize, fileExtension, duration, timeStart, timeFinish,savedOn,note):
        # Constructor of the Record's class
        self.camera = camera
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
        """
        INSERT INTO "Record" VALUES(...)
        """