letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ["~","`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", ".", ",", ]
upper = []
lower = []

for letter in letters:
    upper.append(letter.upper())

for letter in letters:
    lower.append(letter.lower())
    
general = upper+lower+symbols+numbers

# for gen in general:
print(len(general))

a = 1
int(a)

b = 0
int(b)

print(*upper[b:a] + *lower[b:a])        #cant figure it out 
a = a + 1
b = b + 1
print(*upper[b:a])
a = a + 1
b = b + 1
print(*upper[b:a])
