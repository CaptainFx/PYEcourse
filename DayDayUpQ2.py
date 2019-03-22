#问题2
# 一年360天，每天进步5‰和1%，累计进步多少呢？
# 一年365天，每天退步5‰和1%，累计剩下多少呢？
#DayDayUpQ2.py
dayfactor1 = 0.005
dayup1 = pow(1+dayfactor1, 365)
daydown1 = pow(1-dayfactor1, 365)
dayfactor2 = 0.01
dayup2 = pow(1+dayfactor2, 365)
daydown2 = pow(1-dayfactor2, 365)
print("5‰的力量，向上:{:.2f}, 向下:{:.2f}".format(dayup1, daydown1))
print("1%的力量，向上:{:.2f}, 向下:{:.2f}".format(dayup2, daydown2))