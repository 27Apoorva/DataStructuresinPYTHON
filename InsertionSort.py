def InsertionSort(data):
	for i in range(1,len(data)):
		temp=data[i]
		print 't',temp
		j=i
		while j>0 and temp<data[j-1]:
			print 'j',j

			data[j]=data[j-1]
			print 'd',data
			j-=1
		data[j]=temp
		print data

data=[5,10,4,2,7,1]
InsertionSort(data)
print data