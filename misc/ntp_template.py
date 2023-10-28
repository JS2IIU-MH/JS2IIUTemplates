''' date and time response from ntp server
    $ pip install ntplib
'''

import datetime
from time import ctime
import ntplib

NTP_SVR = 'ntp.nict.jp'
NTP_SVR_VERSION = 4

client = ntplib.NTPClient()
res = client.request(NTP_SVR, NTP_SVR_VERSION)

ntptime = datetime.datetime.strptime(ctime(res.tx_time), "%a %b %d %H:%M:%S %Y")

print(ntptime.strftime('%Y/%m/%d %H:%M:%S'))
