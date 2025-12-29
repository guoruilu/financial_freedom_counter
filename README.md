# 财富自由计算器

## 第一版
Prompt：

用python写一个“财富自由计算器”的代码，计算过程如下： 初始（第0年）有ORIG_MONEY的钱，每年的年利率是R，每年的消费是C，要求迭代计算ORIG_MONEY可以用多少年，即到第几年的时候会用完。 以第一年为例，需要从ORIG_MONEY中取C元出来使用，那么第一年结束后C元全部用完，而(ORIG_MONEY-C)元会变成(ORIG_MONEY-C)*(1+R)。那么第二年再从(ORIG_MONEY-C)*(1+R)元中取出C元，重复上述过程。