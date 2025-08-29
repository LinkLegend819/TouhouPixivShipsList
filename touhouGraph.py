f = open('touhouPixivShips.txt', 'r', encoding="utf-8")
data = []
temp = ""
for line in f:
    if line.find("\\") != -1:
        temp = line[:-1]
    else:
        temp = line
    if temp != '':
        temp = temp.split(" ")
        try:
            temp[1]
            data.append(temp)
        except:
            continue
f.close()

temp = ""
for pair in data:
    temp = pair[2].split("x")
    temp2 = 1
    for val in temp:
        temp2 *= int(val)
    pair[2] = temp2