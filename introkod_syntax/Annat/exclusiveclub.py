age = int(input('How old are you? '))

if age < 18:
    print('You are too young.')

if age > 30:
    print('You are too old.')

if age >= 18:
    answer = input('Have you had anything to drink today or taken something? Yes or no: ')
    if answer == "no":
        print('You got to be turned up')
    else:
        print('Please answer yes or no.')

    if answer == "yes":
        input('So you telling me you turned up or what?')

        


    



