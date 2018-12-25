from datetime import datetime


class Events:

    def __init__(self, id, name, content, owner, fromdate, todate, isdelete, ispublic, location):
        self.event_id = id
        self.event_name = name
        self.event_content = content
        self.event_owner = owner
        self.event_fromdate = fromdate
        self.event_todate = todate
        self.isdelete = isdelete
        self.ispublic = ispublic
        self.event_location = location
        self.event_timecreate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.event_lasttime_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.event_user_update = owner

    def displayInfo(self):
        print('Event ID: ', self.event_id)
        print('Event name: ', self.event_name)
        print('Event content: ', self.event_content)
        print('Author: ', self.event_owner)
        print('Event start date: ', self.event_fromdate)
        print('Event end date: ', self.event_todate)
        print('Event has been deleted: ', self.isdelete)
        print('Event is public: ', self.ispublic)
        print('Event location: ', self.event_location)
        print('Event time create: ', self.event_timecreate)
        print('Event time update: ', self.event_lasttime_update)
        print('Update infor by: ', self.event_user_update)
