s1 = str(input('Enter a word : '))
s2 = str(input('Enter a word : '))
print(s1)
for i in range(len(s1)):
    if s1[i] != s2[i]:
        print(s2[:i+1] + s1[i+1:])
