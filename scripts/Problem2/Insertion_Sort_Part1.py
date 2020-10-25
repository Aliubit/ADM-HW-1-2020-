# Insertion Sort - Part 1

def insertionSort(arr):
    is_sorted = False
    my_var = arr[-1]
    index = 2

    while index <= len(arr):
        if arr[-index] > my_var:
            arr[-index + 1] = arr[-index]
            print(format_print(arr))
        elif arr[-index] < my_var:
            arr[-index + 1] = my_var
            print(format_print(arr))
            is_sorted = True
            break
        index += 1

    if not is_sorted:
        try:
            if arr[0] > my_var:
                arr[1] = arr[0]
                arr[0] = my_var
        except IndexError:
            pass
        print(format_print(arr))

    return arr


def format_print(arr):
    temp_list = []
    for var in arr:
        temp_list.append(str(var))
    return ' '.join(temp_list)


m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)