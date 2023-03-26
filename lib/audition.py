
class Audition:

    all = []

    def __init__(self, actor, location, hired, role):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role = role
        role.auditions.append(self)
        Audition.all.append(self)


   

    # Audition#role returns an instance of role associated 
    # with this audition.
    @property
    def instance_role(self):
            return self.role


    # Audition#call_back() will change the the hired attribute to True.
    def call_back(self):
        self.hired = True

    # @property
    # def call_back(self):
        # return self._hired

    # @call_back.setter
    # def call_back(self, new_hire):
        # if (new_hire == False):
            # self._hired = True
        # else:
            # self._hired = True
