import EventRepository
import Errors
# lib for check Email.
import re


class EventUsercase:
    def __init__(self):
        self.repository = EventRepository.EventRepository()
        print('create repository.')

    def addEvent(self, event):
        error = self.__validateData(event)
        if error.statusCode == 0:
            return self.repository.addNewEvent(event)
        return error

    def __validateData(self, data):
        # Check lengh
        if len(data.event_name) > 100:
            return Errors.Errors('Over event name length.', 1)
        elif len(data.event_owner) > 60:
            return Errors.Errors('Over event author length.', 1)
        elif len(data.event_location) > 200:
            return Errors.Errors('Over event location length.', 1)

        # Check validate base regex.
        emailRegex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        match = re.match(emailRegex, data.event_contact)
        if match == None:
            return Errors.Errors('Invalid email contact.', 1)
        
        return Errors.Errors(None, 0)
