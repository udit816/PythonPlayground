# accept a credit card number
cc_number = input("Enter a credit card number: ")
print(f"Entered CC number is: {cc_number}")
num_list = list(cc_number)
print(f"Credit Card number converted to list: {num_list}\n")

# Luhn algorithm
# 1. Remove the rightmost digit from the card number. 
# This number is called the checking digit, and it will be excluded from most of our calculations.
checking_digit = int(num_list.pop())
print(f"1. Removed the rightmost digit from the card number: {checking_digit}\n")

# 2. Reverse the order of the remaining digits.
reversed_num = num_list[::-1]
print(f"2. Reverse the order of the remaining digits: {reversed_num}")

# 3. Take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. 
# If any of the results are greater than 9, subtract 9 from those numbers.
doubled = []
for counter, digit in enumerate(reversed_num):
    if counter % 2 == 0:
        double = int(digit) * 2
        print(f"Doubled the digit at Index {counter}: {double}")
        if double > 9:
            minus_nine = double - 9
            print(f"Since doubled digit is greater than 9 subtracted 9 from it: {minus_nine}")
            doubled.append(minus_nine)
            print(f"Final number appended to list: {doubled}")
        else:
            doubled.append(double)
            print(f"Doubled number less than 9, directly appended to list: {doubled}")
    else:
        doubled.append(int(digit))
        print(f"List appended at odd Index {counter}: {doubled}")

# 4. Add together all of the results and add the checking digit.
sum = 0
for i in doubled:
    sum = sum + int(i)
print(f"Sum of all digits: {sum}")
sum = sum + checking_digit
print(f"Sum of all digits plus checked digit: {sum}")


#5 . If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.
if sum % 10 == 0:
    print("Valid Card Number")