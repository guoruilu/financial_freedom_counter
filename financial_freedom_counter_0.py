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


wealth_free_trace(700_0000, 0.015, 30_0000)