#suggestions are to use a strong type to represent a verified SQL string to clean up all the verification.
#and use types to find out whats wrong with the calculation on age bug

import test_helpers
import validation

def calculate_fee(member_id, age, veteran_status):
    """
    Fees for members under 18 are 6 dollars, fees for over 18 dollars are 20 dollars. Fees for
    members over 65 are only 9 dollars. Veterans get a 15% discount on top of their price.
    Finally, members who've been here for more than 5 years get another dollar off."""

    if age < 18:
        base_fee = 6
    elif age > 65:
        base_fee = 9
    else:
        base_fee = 20

    if veteran_status:
        base_fee = base_fee * .85

    tenure = test_helpers.lookup_member_tenure(member_id)

    if tenure > 5:
        base_fee = base_fee - 1

    return base_fee

def lookup_fee(name):
    """ Calculates a fee based on a name """

    assert not validation.has_sql_in_it(name), "make sure name doesn't have sql injection"

    veteran_status = test_helpers.is_veteran(name)
    age = test_helpers.lookup_age(name)
    member_id = test_helpers.lookup_member_id(name)

    return calculate_fee(age, member_id, veteran_status)

VALID_INPUT = False
while not VALID_INPUT:
    print("Enter your name")

    NAME = input()
    VALID_INPUT = not validation.has_sql_in_it(NAME)

    if not VALID_INPUT:
        print("Don't put protected sql characters in your name!")

print("Fees for user", NAME, "are", lookup_fee(NAME))

#WTF
# I plug this in with "Donald Duck", who's 20 and is a veteran. His prices should be
# 20 * .15 = 17
# but instead I get 16?!?!?
# But when I put in "Roger Rabbit", who's also 20 years old but has long tenure, his
#prices are correct at  20 (over 18) - 1 (has tenure) = 19 dollars?
