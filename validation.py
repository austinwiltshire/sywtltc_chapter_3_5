"""
The architect says we have to be careful with sql, so we use this quick
verification for now.
"""

def has_sql_in_it(str_):
    """
    A really basic check to see if some sql is in a string. We should replace this with a better
    check when we integrate the database.
    """

    return any(keyword in str_ for keyword in ["select", ";", "drop", "join"])
