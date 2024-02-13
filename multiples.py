# print out multiples of 3 up to 200
# now using the same loop, lets see if we can print out the multiples of 5

for count in range(3,200,3):
    if count % 3 == 0:
        print(count)
    elif count % 5==0:
        print(count)
