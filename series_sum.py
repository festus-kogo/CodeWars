# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

# Sum of the first nth term of Series


#     Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

def series_sum(n):
    # Happy Coding ^_^

    if n == 1:
        return round(n, 2)

print(series_sum(1))