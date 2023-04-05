
testNum = 30

for i in range(1, testNum) :
    with open(r"test" + str(i) + ".out", 'r') as f:
        for line in f :
            data_line = line.strip("\n").split()
            if int(data_line[0]) < 0:
                print("error ! " + str(i))