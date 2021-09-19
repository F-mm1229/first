import random

omikuzi = [
            "あ"   if i < 2 else
            "中吉"   if 2 <= i < 10 else
            "小吉"   if 10 <= i < 20 else
            "吉"     if 20 <= i < 40 else
            "末吉"   if 40 <= i < 50 else
            "凶"     if 50 <= i < 55 else
            "中凶"   if 55 <= i < 59 else
            "大凶"   for i in range(61)]

print(random.choice(omikuzi) + "だよ！")