max_number = 10

user_input = input('Enter file numbers to delete:\n')
print()


numbers = user_input.split()
try:
    numbers = [int(number) for number in numbers]
    if all(number <= max_number for number in numbers):
        for number in numbers:
            print('Delete', number)

      
    else:
        print()
        print('Wrong format')
        print()


except:
    print()
    print('Wrong format')
    print()