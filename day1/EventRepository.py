
class EventRepository:
    def __init__(self):

        # create connect or todo something.
        self.list = []

    def addNewEvent(self, event):
        try:
            self.list.append(event)
            event.displayInfo()
            return True
        except:
            return False