s = 0
for i in range(2, 8):
    if i == 3:
        continue
    if i == 6:
        break
    s = s + i
print(s)
git --version