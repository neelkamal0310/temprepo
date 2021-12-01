string = input()
result = ''

for ind, char in enumerate(string, 1):
    if ind % 2 == 0:
        temp = ord(char) + 5
    else:
        temp = ord(char) + 13
    if temp > 122 or temp > 90:
        temp -= 26
    result += chr(temp)

print(result)
