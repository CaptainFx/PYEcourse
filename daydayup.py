dayup = 1.0
dayfactor = 0.01
AdayUp = pow(dayup + dayfactor, 365)
print(AdayUp)


def dayUp(df):
    dayup = 1.0
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


while dayUp(dayfactor) < AdayUp:
    dayfactor += 0.001

print("{:.3f}".format(dayfactor))