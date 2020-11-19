vokaler = ['a', 'e', 'i', 'o', 'u'] 

s = 0

text = "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater"

for v in text:
    if v in vokaler:
        s += 1
print(s)