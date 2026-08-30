def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = i
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
 


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = i
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor


def median_of_list(elements):
    list = []
    count = 0
    for num in elements:
       
        list.append(num)
        insertion_sort(list)
        n = len(list)
        if n%2== 0:
            median = (list[n//2 - 1] + list[n//2])/2
        else:
            median = list[n//2]
        print(f"the median of the list is : {median}")
    count += 1

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5]
    median_of_list(elements)

