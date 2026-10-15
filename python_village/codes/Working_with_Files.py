# save the given text as file.txt

f = open("file.txt", "r")
l = f.readlines()
f.close()
o = open("o.txt", "w")

for i in range(0, len(l)):
    if i % 2 == 1:
        o.write(l[i])
o.close()

