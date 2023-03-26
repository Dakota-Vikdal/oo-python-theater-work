import ipdb
from lib import *

# Test your code below...
role1 = Role("Peter Pan")
role2 = Role("Captain Hooke")



dakota = Audition("Dakota", "Denver, CO", True, role1)
nathalie = Audition("Nathalie", "Florida", False, role2)
destin = Audition("Destin", "Colorado", True, role2)





# the below line allows us to stop & try stuff!
ipdb.set_trace()