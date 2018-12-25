import Errors

class EventRepository:
    def __init__(self):

        # create connect or todo something.
        self.list = []

    def addNewEvent(self, event):
        try:
            self.list.append(event)
            event.displayInfo()
            return Errors.Errors(None, 0)
        except:
            return Errors.Errors('Can not add event to DB.', 1)