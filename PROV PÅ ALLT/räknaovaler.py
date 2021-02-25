a_string = "Do not worry about your difficulties."
lowercase = a_string.lower()

vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
print(vowel_counts)