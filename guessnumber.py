try:
    guess = eval(input())
    if guess > 66 or guess < 66:
        print("猜错了")
    else:
        print("猜对了")
except:
    print("输入的不是数字")