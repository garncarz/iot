MAX_TRIES = 100
MANY_RECORDS = 10000

try:
    from .settings_local import *
except ImportError:
    pass
