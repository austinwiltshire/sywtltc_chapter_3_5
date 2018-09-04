import test_helpers


class Member(object):
    def __init__(self, member_id):
        self._member_id = member_id
        self._veteran = False
        self._tenured = False

    def get_age_fee(self) -> int:
        """Return base fee based on age"""
        age = test_helpers.lookup_age(self._member_id)
        assert age >= 0, "You must be born to enter the movie"
        assert age <= 124, "You can't be the oldest person alive"
        if age <= 18:
            base_fee = 6
        elif age >= 65:
            base_fee = 9
        else:
            base_fee = 20
        return base_fee

    def veteran_status(self) -> bool:
        """Lookup if our member is a veteran"""
        vet_status = test_helpers.is_veteran(self._member_id)
        if vet_status is True:
            return True
        else:
            return self._veteran

    def tenure_status(self) -> bool:
        """Find out if a member is eligible for tenure discount"""
        years = test_helpers.lookup_member_tenure(self._member_id)
        if years > 5:
            return True
        else:
            return self._tenured
