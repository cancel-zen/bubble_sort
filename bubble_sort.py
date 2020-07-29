def bubble_sort(array=[]):
    for i in range(len(array)-1): #进行n-1轮排序，i由0开始
        for j in range(len(array)-1-i):#每一轮比较前面n-i个
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
my_array=[]
bubble_sort(my_array)
print(my_array)
