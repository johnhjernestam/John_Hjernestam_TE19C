x = "hej jag heter anton"

vokaler = 0

for i in x:
    if(i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u' or i == 'A' or i == 'I' or i == 'E' or i == 'O' or i == 'U'):
        vokaler += 1
print(vokaler)