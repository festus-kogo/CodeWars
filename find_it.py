# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
# Find the odd int

seq = [7]
seq = [0]
seq = [1,1,2]
seq = [0,1,0,1,0]
seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]

# seq = list(set(seq))

for i in list(set(seq)):
    # print(i)
    if (seq.count(i) % 2) != 0:
        print(i)

def find_it(seq):
    for i in list(set(seq)):
        # print(i)
        if (seq.count(i) % 2) != 0:
            # print(i)
            return i
    

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])) # 5
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5])) # -1
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])) # 5