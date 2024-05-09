# https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/python

def print_array(arr):
    #your code here
    arr1 = []
    print(f"Input ==> {arr}")
    print(f"Input type ==> {type(arr)}")

    for i in arr:
        if type(i) is str:
            arr1.append(i)
        else:
            arr1.append(str(i))

    temp = ",".join(arr1)
    return f"\"{temp}\""


arr = ["h","o","l","a"]
arr = [2,4,5,2]
arr = [2]
arr = ['2', '4', '5', '2']
print(f"{print_array(arr)}")
# print(f"{type(print_array(arr))}")