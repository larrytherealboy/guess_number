#產生一個隨機整數1~100(不要印出來), 讓使用者重複輸入數字去猜
#猜對的話, 印出 "終於猜對了!"
#猜錯的話, 要告訴他 比答案大/小

import random
r = random.randint(1, 100)
 
while True:
	num = input('請猜數字: ')
	num = int(num)
	if r == num:
		print('你猜對了!')
		break
	elif r >= num:
		print('比答案小')
	else:
		print('比答案大')


