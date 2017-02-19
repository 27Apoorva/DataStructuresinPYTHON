def MergeSort(data):
	if len(data)>1:
		mid=len(data)/2
		left=data[:mid]
		right=data[mid:]
		MergeSort(left)
		MergeSort(right)
		i=j=k=0
		while i<len(left) and j <len(right):
			if left[i]>right[j]:
				data[k]=left[i]
				i+=1
			else:
				data[k]=right[j]
				j=j+1
			k=k+1
		while  i<len(left):
			data[k]=left[i]
			i+=1
			k+=1
		while j<len(right):
			data[k]=right[j]
			j+=1
			k+=1
			
if __name__ == '__main__':
	data=[5,10,4,2,7,1]
	MergeSort(data)
	print data