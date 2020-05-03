import CheckInOutAccessChecks

class CheckInAccessChecks(CheckInOutAccessChecks.CheckInOutAccessChecks):
    def __init__(self, isCheckIn):
        self.isCheckIn = isCheckIn
