age = int(input('How old are you? '))

if age < 18:
    print('You are too young.')

if age > 79:
    print('You are too old.')

if age >= 18:
    answer = input('Okey, but have you had anything to drink today? Yes or no: ')
    if answer == "yes":
        print('Put the vehicle in park and step out')

    elif answer == "no":
        print('Alright, drive safe.')
    else:
        print('Please enter yes or no.')


    



