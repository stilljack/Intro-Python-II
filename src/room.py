# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    name = ""
    description = ""

    #
    # * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    #   which point to the room in that respective direction.

    n_to = ""
    s_to = ""
    w_to = ""
    e_to = ""



    def __init__(self, name, description):
        self.name = name
        self.description = description

