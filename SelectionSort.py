def SelectionSort(data):
	for i in range (len(data)):
		min=i
		for j in range(i+1,len(data)):
			if data[j]<data[min]:
				min=j
		swap(data,min,i)
		print data # For visualisation
def swap(data,a,b):
	temp=data[a]
	data[a]=data[b]
	data[b]=temp

if __name__ == '__main__':
	data=[5,10,4,2,7,1]
	SelectionSort(data)
	#print data