def wealth_free_trace(ORIG_MONEY, R, C):
    if ORIG_MONEY * R >= C:
        print(f"永远花不完")
        return None  # 表示永远花不完

    money = ORIG_MONEY
    year = 0

    print(f"第0年初：{money:.2f}")

    while money > 0:
        year += 1
        money -= C
        print(f"\n第{year}年 消费后：{money:.2f}")

        if money <= 0:
            print(f"第{year}年结束，钱用完")
            break

        money *= (1 + R)
        print(f"第{year}年 年末计息后：{money:.2f}")
    
    return year

def required_orig_money_iter(R, C, Y_expect):
    """
    使用逐年反推的方式计算所需初始资金
    """
    money = 0.0  # 第 Y 年消费后剩余

    for _ in range(Y_expect):
        # 反推到上一年年初
        money = money / (1 + R) + C

    return money



# wealth_free_trace(1000_0000, 0.015, 10_0000)
money = required_orig_money_iter(0.015, 30_0000, 50)
wealth_free_trace(money, 0.015, 30_0000)