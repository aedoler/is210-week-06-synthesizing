#!user/bin/env python
# -*- coding: utf-8 -*-
"""Dividing families by table at party"""


def get_party_stats(families, table_size=6):
    """Return total number of guests and tables needed.
    Arguments:
        families: each familiy as list
        table_size(int): size of table - 6
    Returns:
        total number of guests and tables needed
    Examples:
    GUEST_LIST = [['Jan'], ['Jill', 'Jack', 'Bob'], ['Jen', 'Alan'], ['Nick']]
    get_party_stats(GUEST_LIST)
    >>>(7, 4)
    """

    total_guests = 0
    total_tables = 0
    for family in families:
        total_guests += len(family)  # total_guests = total_guests + len(family)
        total_tables += -(-len(family) // table_size)

    return (total_guests, total_tables)


GUEST_LIST = [['Jan'], ['Jill', 'Jack', 'Bob'], ['Jen', 'Alan'], ['Nick']]

get_party_stats(GUEST_LIST)
