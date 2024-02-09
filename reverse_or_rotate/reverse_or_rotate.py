# https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/python

def rotate_str(chk, pos):
    return chk[pos:] + chk[0:pos]

def get_chnks(my_str, sz):
    arr = []

    for i in range(len(my_str) // sz):
        # print(f"{i * sz}:{sz * (i + 1)}")
        arr.append(my_str[(i * sz):sz * (i + 1)])
    
    return arr

def sum_digits_cubes(chnk):
    total = 0

    for i in chnk:
        total += int(i) ** 3
    
    return total

def rev_rot(strng, sz):
    # your code
    if sz <= 0 or strng == "" or sz > len(strng):
        return ""
    else:    
        chunks = get_chnks(strng, sz)
        # print(f"Chunks => {chunks}")
        chunks1 = []

        # Loop through the chunks
        for i, v in enumerate(chunks):

            if sum_digits_cubes(v) % 2 == 0: # reverse that chunk
                # print(f"Reversed => {v[::-1]}")
                chunks1.append(v[::-1])
            elif sum_digits_cubes(v) % 2 == 1:
                chunks1.append(rotate_str(v, 1)) # rotate the chunk
                # print(f"{v} is rotated to => {rotate_str(v, 1)}")
            else:    
                chunks1.append(v)            

        return "".join(chunks1)



        

