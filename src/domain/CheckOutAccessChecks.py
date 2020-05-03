import CheckInOutAccessChecks

class CheckOutAccessChecks(CheckInOutAccessChecks.CheckInOutAccessChecks):
    def __init__(self, isCheckOut):
        self.isCheckOut = isCheckOut
