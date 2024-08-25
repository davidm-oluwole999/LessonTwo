string1 = input("Enter the string:  ")

vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for i in string1:
    if i in vowels:
        vowels[i] += 1

print (vowels)

# Find if the string entered by the user is a pangram or not

string2 = input("Enter the number:")

count = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "0":0}

for a in string2:
    if a in count:
        count[a] += 1

pangram = True
for count1 in count.values():
    if count1 == 0:
        pangram = False

if pangram:
    print("The entered string is a pangram.")
else:
    print("The entered string is not a pangram.")