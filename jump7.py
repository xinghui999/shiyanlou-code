for i in range(1,101):
	flag=0
	temp=i
	if temp%7==0:
		flag=1
	else:
		while temp>0:
			if temp%10==7:
				flag=1
				break
			temp=temp//10
	if flag==0:
		print(i)	
