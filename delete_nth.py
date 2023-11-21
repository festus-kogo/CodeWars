# codewars.com/kata/554ca54ffa7d91b236000023/train/python
# Delete occurrences of an element if it occurs more than n times

def delete_nth(order, max_e):
    # code here
    order2 = order
    print(f"list: {order2}")
    print(f"set: {set(order2)}")
    for i in set(order2):
        if order2.count(i) > max_e:
            # order2.reverse()
            # order2.remove(i)
            # order2.reverse()
            if i in order2:
                order2.reverse()
                order2.remove(i)
                order2.reverse()

    return order2

# print(delete_nth([20,37,20,21], 1)) # [20, 37, 21]
# print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2]
print(delete_nth([1,2,3,1,1,2,1,2,3,3,2,4,5,3,1], 3))
# [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1]
# [1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 4, 5]
lst = [1,2,3,1,1,2,1,2,3,3,2,4,5,3,1]
print(lst.count(1))