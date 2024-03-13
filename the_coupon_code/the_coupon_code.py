# https://www.codewars.com/kata/539de388a540db7fec000642/train/python
import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
     #Code here!
#     print(f"entered_code => {entered_code} of type {type(entered_code)}")
#     print(f"correct_code => {correct_code} of type {type(entered_code)}")
    
#     if str(entered_code) == str(correct_code):
#         print(f"Entered code, {correct_code}, is correct!")
#     else:   
#         print(f"Entered code, {correct_code}, is incorrect!")
    
    print("**************************************************************************")

    print(f"raw current_date => {current_date} type => {type(current_date)}")
    print(f"raw expiration_date => {expiration_date} type => {type(expiration_date)}")

    current_date1 = datetime.datetime.strptime(str(current_date).replace(',', ''), '%B %d %Y') # September 5, 2014 => 2014-09-05 00:00:00 to format
    expiration_date1 = datetime.datetime.strptime(str(expiration_date).replace(',', ''), '%B %d %Y') # September 5, 2014 => 2014-09-05 00:00:00 to format

    print(f"current_date1 => {current_date1} => type {type(current_date1)}")
    print(f"expiration_date1 => {expiration_date1} => type {type(expiration_date1)}")
    
    # print(f"{current_date1} <= {expiration_date1} {current_date1 <= expiration_date1}")

    if str(entered_code) == str(correct_code):
        if current_date1 == expiration_date1:
            # print(f"Coupon is valid, return => {True}")
            print(f"{current_date1} is equal to {expiration_date1}")
            print(f"{current_date1}")
            print(f"{expiration_date1}")
            # print(f"Coupon is valid, return => {True}")
            return True
        elif current_date1 < expiration_date1:
            # print(f"Coupon is invalid, return => {False}")
            print(f"{current_date1} is less than {expiration_date1}")
            print(f"{current_date1}")
            print(f"{expiration_date1}")
            return True
        
        else:
            # print(f"Coupon is invalid, return => {False}")
            print(f"{current_date1} is greater than {expiration_date1}")
            print(f"{current_date1}")
            print(f"{expiration_date1}")
            return False
    
    print(f"{entered_code}")
    print(f"{correct_code}")
    print("entered_code is invalid!")
    return False


print(check_coupon('123','123','September 5, 2014','October 1, 2014')) # True
# print(check_coupon('123a','123','September 5, 2014','October 1, 2014')) # False

# print(check_coupon('2','2','September 5, 2014','September 25, 2014')) # True
# print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015")) # True
# print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015")) # False
