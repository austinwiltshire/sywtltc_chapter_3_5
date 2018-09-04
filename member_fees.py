#suggestions are to use a strong type to represent a verified SQL string to clean up all the verification.
#and use types to find out whats wrong with the calculation on age bug

import test_helpers
import validation
import Member


def calculate_fee(Member: Member) -> int:
    """
    Fees for members under 18 are 6 dollars, fees for over 18 dollars are 20 dollars. Fees for
    members over 65 are only 9 dollars. Veterans get a 15% discount on top of their price.
    Finally, members who've been here for more than 5 years get another dollar off."""

    base_fee = Member.get_age_fee()
    veteran = Member.veteran_status()
    if veteran is True:
        base_fee = base_fee * .85
    tenure = Member.tenure_status()
    if tenure > 5:
        base_fee = base_fee - 1

    return base_fee
