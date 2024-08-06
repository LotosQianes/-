def merge_sort(arr):
	#基准情况:当数组长度小于等于1时,可以直接认为已排序
	if len(arr) <= 1:
		return arr

	#计算数组中间值索引
	mid = len(arr) // 2
	#切分数组为两半,并递归地对切分后的数组进行排序
	left_half = merge_sort(arr[:mid])
	right_half = merge_sort(arr[mid:])
	#返回已排序数组的归并结果
	return merge(left_half, right_half)

def merge(left, right):
	merged = []		#存储已排序归并结果的数组
	left_index = 0		#左边数组遍历的指针
	right_index = 0		#右边数组遍历的指针
	#当两数组中都有未处理的元素时,进行循环
	while left_index < len(left) and right_index < len(right):
		#如果左边元素小于等于右边元素(比较元素比较了遍历另一个列表的所有元素)
		if left[left_index] <= right[right_index]:
			#将左边元素添加到已排序归并结果中,并向前移动左数组指针
			merged.append(left[left_index])
			left_index += 1
		else:
			#反之,将右边元素添加到已排序归并结果中,并向前移动右数组指针
			merged.append(right[right_index])
			right_index += 1

	#如果某一个数组已经处理完,将另一个数组中剩余元素添加到已排序的归并结果中
	merged += left[left_index:]
	merged += right[right_index:]
	#返回归并结果
	print(merged)
	return merged


number = [9,2,5,3,6,1,7,4,8,0,11,12,14,19,16] 
merge_sort(number)