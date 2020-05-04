class Server(object):
    def __init__(self, networkAddress, location, productName, vendor, registeredOn, lastUpdateOn, note):
        # Constructor of the Server's class
        self.networkAddress = networkAddress
        self.productName = productName
        self.vendor = vendor
        self.registeredOn = registeredOn
        self.lastUpdateOn = lastUpdateOn
        self.note = note

    def add(self):
        # Method of adding the server into DataBase
        """
        INSERT INTO "Server" VALUES(...)
        """

    def setServerUpdate(self):
        # Method of changing the lastUpdateOn parameter in DataBase
        """
        UPDATE "Server" SET "lastUpdateOn" = self.lastUpdateOn
        """

    def changeNetworkAddress(self):
        # Method of changing the network Address in DataBase
        """
        UPDATE "Server" SET "NetworkAddress" = self.NetworkAddress
        """

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
        """
        DELETE FROM "Server" where networkAddress=self.networkAddress
        """