# Source https://www.codewars.com/kata/563b662a59afc2b5120000c6/python
# Growth of a Population

p0 = 1000
percent = 2
aug = 50
p = 1200

def nb_year(p0, percent, aug, p):
    count = 0
    percentage = percent / 100

    while True:
        # print(p0)
        p0 += int(p0 * percentage) + aug
        # print(count)
        count += 1

        if p0 == p or p0 > p:
            # print(p0)
            break
    return count

print(nb_year(p0, percent, aug, p)) # 3
print(nb_year(1500, 5, 100, 5000)) # 15
print(nb_year(1500000, 2.5, 10000, 2000000)) # 10
print(nb_year(1500000, 0.25, 1000, 2000000)) # 94