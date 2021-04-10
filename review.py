data=[]
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，共有',len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) #sum+len + len(d)
print('每一筆留言平均長度是',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('共有',len(new),'個留言，少於100字') #印一次要放出面
print(new[0])
print('------------')
print(new[1])

good = []
for d in data:
	if 'good' in d:
			good.append(d)

print('共有',len(good),'提到good')
print(good[0])

