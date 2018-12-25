import EventRepository

class EventUsercase:
    def __init__(self):
        self.repository = EventRepository.EventRepository()
        print('create repository.')

    def addEvent(self, event):
        return self.repository.addNewEvent(event)