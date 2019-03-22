#问题1
# 一年360天，每天进步1‰，累计进步多少呢？
# 一年365天，每天退步1‰，累计剩下多少呢？
#DayDayUpQ1.py
dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("向上:{:.2f}, 向下:{:.2f}".format(dayup, daydown))