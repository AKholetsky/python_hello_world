candy = 5

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

string2 = "Hello"
string1 = "World!rrrtrer"

min_len = min(len(string1), len(string2))
result = ""

for i in range(0, min_len):
    result += string1[i] + string2[i]
    
result += (string1[min_len:] if len(string2) == min_len else string2[min_len:])
    
print(result)

ls = True

some = "some" if ls else "any"

print(some)