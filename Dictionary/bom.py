import random as rnd 

antal_kast = 100000
sidor = 6

# Create the dictionary to store the results of each roll of the dice.
kast = {}

#Loop for rolling the dice antal_kast times
for r in range(antal_kast):
    tärnings_kast = rnd.randint(1, sidor)
    if tärnings_kast in kast:
        # Add to the count for this number.
        kast[tärnings_kast] += 1
    else:
        # Record the first roll result for this number.
        kast[tärnings_kast] = 1

# Print how many times each number was rolled
for tärnings_kast in range(1, 7):
    print("Nummer", str(tärnings_kast), "kastades", str(kast[tärnings_kast]), "gånger.")

#How many times the 3 was rolled
# print("The number three was rolled", str(rolls[3]), "times.")

#Average roll between all of them
# sum = 0
# for roll_result in rolls:
    # sum += roll_result * rolls[roll_result]
# print("The average roll result was", str(sum/antal_kast))

# The number rolled most often.
# print(str(max(rolls, key=rolls.get)), "is the most common roll result.")