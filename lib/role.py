from .audition import Audition

class Role:

    def __init__(self, character_name, auditions = []):
        self.name = character_name
        self.auditions = auditions

    @property
    def auditions_role(self):
        return [ a for a in Audition.all if a.role == self ]


# Role#actors returns a list of names from the actors associated 
# with this role.
    @property
    def actors_names(self):
        return [a.actor for a in self.auditions if a.role == self]

# Role#locations returns a list of locations from the 
# auditions associated with this role.
    @property
    def locations(self):
        return [ l.location for l in self.auditions if l.role == self ]

# returns the first instance of the audition that was hired for this role 
    @property
    def lead(self):
        variable = [ a.hired for a in self.auditions ]
        if ( variable[0] == True):
            return variable[0]
        else:
            print("no actor has been hired for this role")

    
    # Role#understudy returns the second instance of the audition that was 
    # hired for this role or returns a string 'no actor has been hired for 
    # understudy for this role'.

    @property
    def lead(self):
        variable = [ a.hired for a in self.auditions ]
        if ( variable[1] == True):
            return variable[1]
        else:
            print("no actor has been hired for understudy for this role")


    



    
        