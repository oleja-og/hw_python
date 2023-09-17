import datetime as dt
class Note:


    def __init__(self, id = 1,header = "header", body = "body",date = f"{dt.datetime.now()}"):
        self.id = id
        self.header = header
        self.body = body
        self.date = date





