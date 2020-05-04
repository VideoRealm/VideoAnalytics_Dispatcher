class Camera(object):
    def __init__(self, networkAddress, location, productName, vendor, registeredOn, lastUpdateOn, note):
        # Constructor of the Camera's class
        self.networkAddress = networkAddress
        self.location = location
        self.productName = productName
        self.vendor = vendor
        self.registeredOn = registeredOn
        self.lastUpdateOn = lastUpdateOn
        self.note = note

    def addCamera(self):
        # Method of adding the camera into DataBase
        """
        INSERT INTO Camera VALUES(...)
        """

    def changeNetworkAddress(self):
        # Method of changing the network Address in DataBase
        """
        UPDATE "Camera" SET "NetworkAddress" = self.NetworkAddress
        """

    def setCameraUpdate(self):
        # Method of changing the lastUpdateOn parameter in DataBase
        """
        UPDATE "Camera" SET "lastUpdateOn" = self.lastUpdateOn
        """

    def bindWithServer(self):
        # Method of binding the camera to Server
        """
        UPDATE "Camera" SET "serverAssigned" = self.serverAssigned
        UPDATE "lastUpdateOn" SET "lastUpdateOn" = self.lastUpdateOn
        """

    def unbind(self):
        # Method of unbinding the camera to Server
        """
        UPDATE "Camera" SET "serverAssigned" = self.serverAssigned
        UPDATE "lastUpdateOn" SET "lastUpdateOn" = self.lastUpdateOn
        """

    def delete(self):
        # Method of deleting the camera in DataBase
        """
        DELETE FROM "Camera" where networkAddress=self.networkAddress
        """