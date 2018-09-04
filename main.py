import member_fees
import validation
import test_helpers
import Member

if __name__ == '__main__':
    VALID_INPUT = False
    while not VALID_INPUT:
        print("Enter your name")
        NAME = input()
        try:
            MEMBER_ID = test_helpers.lookup_member_id(NAME)
            PURCHASER = Member.Member(MEMBER_ID)
            if PURCHASER:
                VALID_INPUT = True
            else:
                print("Please enter a valid name")
        except KeyError:
            print("Please enter a name of someone who is a previous customer")

#        VALID_INPUT = not validation.has_sql_in_it(NAME)

#        if not VALID_INPUT:
#            print("Don't put protected sql characters in your name!")

    print("Fees for user", NAME, "are $", member_fees.calculate_fee(PURCHASER))

    # WTF
    # I plug this in with "Donald Duck", who's 20 and is a veteran. His prices should be
    # 20 * .15 = 17
    # but instead I get 16?!?!?
    # But when I put in "Roger Rabbit", who's also 20 years old but has long tenure, his
    # prices are correct at  20 (over 18) - 1 (has tenure) = 19 dollars?
