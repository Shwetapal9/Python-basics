# Count the number of vowels in a word

word = input("Enter a word")
vowels = {'a', 'e' , 'i' , 'o' , 'u'}

results = {}
for c in word:
    if c in vowels:
        results[c] = results.get(c,0) + 1

for k, v in results.items():
    print(k, " is present", v, " times")