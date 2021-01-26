# program to display only odd numbers

list = enumerate([20, 11, 9, 66, 4, 89, 44])
for idx, num in list:
    # Skipping the iteration when number is even
    if num%2 == 0:
        continue
    # This statement will be skipped for all even numbers
    print(idx, num)