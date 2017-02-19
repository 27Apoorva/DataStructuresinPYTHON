def BubbleSort(data):
	swapp=1
	for i in range(len(data)):
		if (swapp==0):
			return
		for j in range(len(data)-1,i,-1):
			#print i,j
			if data[j]<data[j-1]:
				swap(data,j,j-1)
				print data
				swapp=1
def BubbleSort_descending(data):
	for i in range(len(data)):
		for j in range(len(data)-1,i,-1):
			print j,j-1
			if data[j]>data[j-1]:
				swap(data,j,j-1)
def swap(data,a,b):
	temp=data[a]
	data[a]=data[b]
	data[b]=temp
if __name__ == '__main__':
	data=[5,10,4,2,7,1]
	d1=[1,2,4,5,7]
	print BubbleSort(d1)
	#print d1