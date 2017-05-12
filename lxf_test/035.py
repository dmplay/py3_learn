# -*- coding: utf-8 -*-
from datetime import datetime,timedelta,timezone

def showTime():
    now = datetime.now()
    print(now)
    dt = datetime(2015, 4, 19, 12, 20)
    print(dt)
    print(dt.timestamp())
    t = 1429417200.0
    print(datetime.fromtimestamp(t))
    print(datetime.utcfromtimestamp(t))
    cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday)
    now = datetime.now()
    print(now.strftime('%a, %b %d %H:%M'))
    now = datetime.now()
    print(now + timedelta(hours=10))
    print(now + timedelta(days=2, hours=12))

def showUtc():
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_dt)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    print(bj_dt)
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt)
    tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
    print(tokyo_dt2)

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    re_utc = re.compile(r'^utc-(\d{3,8})$')
    
    return dt.timestamp()
    
if __name__=='__main__':
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1
