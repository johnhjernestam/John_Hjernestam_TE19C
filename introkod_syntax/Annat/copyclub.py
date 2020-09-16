age = int(input('How old are you? '))

if age < 18:
    print('You are too young.')

if age > 30:
    print('You are too old.')

if age >= 18:
    answer = input('Have you had anything to drink today or taken something? Yes or no: ')
    if answer == "yes":
        print('Put the vehicle in park and step out with your hands on top of your head now!')

    elif answer == "no":
        print('Alright, drive safe.')
    else:
        print('Please answer yes or no.')