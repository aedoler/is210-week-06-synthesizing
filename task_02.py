#!user/bin/env python
# -*- coding: utf-8 -*-
"""lists and tuples"""


def prepare_email(appointments):
    """Inserts name and appointment time into message
    Arguments:
        appointments(list): Name and time of appointments expressed as
        individual tuples.

     Returns:
        Formatted string with name and appointment time inserted
        in the proper locations.
    Examples:
        APPVAL = [('Wiley', 'Monday, March 16'),
          ('Jack', 'Tuesday, March 17')]
        prepare_email(APPVAL)
        >>>['Dear Wiley,\nI look forward to meeting with you
        on Monday, March 16.\nBest,\nMe', 'Dear Jack,\nI look forward
        to meeting with you on Tuesday, March 17.\nBest,\nMe']
    """
    message = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    outlist = []

    for item in appointments:
        outlist.append(message.format(item[0], item[1]))

    return outlist


APPVAL = [('Wiley', 'Monday, March 16'),
          ('Jack', 'Tuesday, March 17')]
prepare_email(APPVAL)
