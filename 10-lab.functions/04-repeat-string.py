string = input()
n = int(input())

def repeat(string, times):
    result = []
    for time in range(times):
        result.append(string)

    return "".join(result)

print(repeat(string, n))