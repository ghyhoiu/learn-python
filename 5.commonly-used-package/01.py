# 使用前应该先导入
import calendar
Cal_1 = calendar.calendar(2017)
print(type(Cal_1))
# 由此结果可知,cal是一个字符串
print(Cal_1)
# 也可以对参数进行修改,使日历的形状更加美观
Cal_2 = calendar.calendar(2017, w=3, l= 3, c=5)
print(Cal_2)
# isleap 可以判断是否为闰年
print(calendar.isleap(2020))
# leapdays
# 输入必须是前面的年份大于后面的年份,否则会输出-1
print(calendar.leapdays(1000, 2000))
# month
print(calendar.month(2018, 6))
# monthrange
print(calendar.monthrange(2018,6))
# 注意,返回值会是一个元祖,所以开始的元素是从0开始计数,
# monthcalendar
print(calendar.monthcalendar(2018,6))
# prcal:直接打印日历,同理prmonth:直接打印月的日历
calendar.prcal(2018)
# 获取周几
print(calendar.weekday(2018,7,6))