import uuid

class Client:
    def __init__(self, name, adress, email,celphone,uid = None):
        self.name = name
        self.adress = adress
        self.email=email
        self.celphone=celphone
        self.uid = uid or uuid.uuid4()

    
    def to_dict(self):
        return vars(self)

    
    @staticmethod
    def schema():
        return ['name','adress','email','celphone','uid']