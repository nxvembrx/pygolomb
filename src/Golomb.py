def Streaks(sequence):
    streaks = {}
    streak = 1
    i = 0
    while(sequence[0] == sequence[len(sequence) - 1]):
        if(i > len(sequence)):
            return dict()
        sequence = sequence[1:] + sequence[0]
        i += 1
        
    if(sequence[len(sequence) - 1] == "1"):
        sequence += "0"
    else:
        sequence += "1"
        
    for i in range(0, len(sequence) - 1):
        if(sequence[i] == sequence[i + 1]):
            streak += 1
        else:
            try:
                streaks[streak].append(i)
            except:
                streaks[streak] = [i]
            streak = 1
    return streaks


def Distance(s1, s2):
    distance = 0
    for i, j in zip(s1, s2):
        if(i != j):
            distance += 1
    
    return distance


def Golomb(sequence):
    result = [True, True, True]
    print('Counting ones and zeroes...') 
    z = sequence.count("0")
    o = sequence.count("1")
    
    print('Done.')
    print('Zeroes: ' + str(z) + '\n Ones: ' + str(o))
          
    if(abs(z - o) > 1):
        result[0] = False
    
    streaks = Streaks(sequence)
    strnum = list(streaks)
    
    print('Checking second postulate...')
    
    if (streaks):
        for i in range(0, len(strnum) - 1):
            if(abs(strnum[i] - strnum[i + 1]) != 1):
                result[1] = False
                break
            if(len(streaks[strnum[i]]) != 2 * len(streaks[strnum[i + 1]])):
                if(len(streaks[strnum[i]]) != 1 and len(streaks[strnum[i + 1]]) != 1):
                    result[1] = False
                    break
    else:
        result[1] = False
    
    print('Done.')
        
    sequence2 = sequence[1:]+sequence[:1]
    ham = Distance(sequence,sequence2)  
    print('Hamming distance')  
    for i in range(2,len(sequence)- 1):
        sequence2 = sequence[i:]+sequence[:i]
        if(ham!=Distance(sequence,sequence2)):
            result[2] = False  
        print('Shift No.' + str(i)) 
        print('Distance: ' + str(Distance(sequence,sequence2))) 
    return result