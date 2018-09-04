""" We don't have the database integrated yet, so just use these test helpers for now """


def lookup_member_id(name: str) -> int:
    """
    Temporary test function to look up names. Will replace this when we integrate with the
    database.
    """

#    assert not has_sql_in_it(name), "make sure name doesn't have sql injection"

    return {
        "Micky Mouse": 10,
        "Roger Rabbit": 20,
        "Donald Duck": 30,
        "Bugs Bunny": 40,
        "Daffy Duck": 50,
    }[name]

def lookup_member_tenure(member_id: int) -> int:
    """ Temporary test function to map ids to tenure. """

    return {
        10: 2, #micky has been here 2 years
        20: 10, #roger's been here for 10 years
        30: 2, #donald has been here 2 years
        40: 12, #bugs bunny has been here for 12
        50: 5, #daffy has been here for 5 years
    }[member_id]


def lookup_age(member_id: int) -> int:
    """
    Temporary test function to look up ages Will replace this when we integrate with
    the database.
    """

#    assert not has_sql_in_it(name), "make sure name doesn't have sql injection"

    return {
        10: 17,
        20: 20,
        30: 20,
        40: 70,
        50: 35,
    }[member_id]


def is_veteran(member_id: int) -> bool:
    """ Temporary test function to see if a member is a veteran """

#    assert not has_sql_in_it(name), "make sure name doesn't have sql injection"

    return {
        10: False,
        20: False,
        30: True,
        40: False,
        50: False,
    }[member_id]
