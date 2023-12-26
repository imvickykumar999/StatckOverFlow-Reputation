test_dict = [False, False, True, False, False, True]
lastpos = -1
truepos = [-1]*len(test_dict)
for i in reversed(range(len(test_dict))):
    if test_dict[i]:
        lastpos = i
    truepos[i] = lastpos

for i in range(len(test_dict)):
    print(i, truepos[i])