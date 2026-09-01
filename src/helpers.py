# This file contains code that is intended to be utilized across different modules.

from datetime import datetime

def make_timestamp() -> str:
    '''
    Create a timestamp that can be used in filenames.

    Example:
        20260901_130512
    '''

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    return timestamp