

df = open("dictionary.txt", "r")
dft = open("dft", "w")

for x in range(74):
    data = df.readline()
    data += ':' + ('%d' %(x+1)) + '_'
    dft.write(data)

dft.close()