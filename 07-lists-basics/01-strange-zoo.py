tail = input()
body = input()
head = input()

meerkat = [tail, body, head]

#           0      1     2
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)