from datetime import datetime
birthday = datetime(1999,6,14,22,00)
print(birthday)
print('%s 年%s 月%s 日'%(birthday.year,birthday.month,birthday.day))
print('{0:%Y}-{0:%m}-{0:%d} {0:%a}'.format(birthday))
print('{0:%b}.{0:%d} {0:%Y}'.format(birthday))
print('{0:%d}{1:} {0:%b} {0:%Y}'.format(birthday,['st','nd','rd','th'][birthday.day%10-1 if birthday.day%10<=3 else 3]))