# Create new Events for next day.
import Events
from datetime import datetime, date, time
import EventUsercase


def createEvent():

    # Declare event.
    eventId = '123456'
    eventTitle ='Meeting machine learning'
    eventContent ='Weekly meeting for discus NG\'s course.'
    eventAuthor = 'Thinh Ung V.'
    startDate = datetime.combine(date(2018, 12, 25), time(16, 30))
    endDate = datetime.combine(date(2018, 12, 25), time(17, 30))
    roomName = "Son Tra meeting room."
    contact = 'info@asiantech.vn'
    event = Events.Events(eventId, eventTitle, eventContent, eventAuthor, startDate, endDate, False, False, roomName, contact)

    userCase = EventUsercase.EventUsercase()
    result = userCase.addEvent(event)

    if result.statusCode == 0:
        print('Add success')
    else:
        print('Error message :', result.message)
