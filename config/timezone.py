import pytz
from datetime import datetime

JAKARTA_TZ = pytz.timezone('Asia/Jakarta')

def ID_timezone():
    return datetime.now(JAKARTA_TZ)