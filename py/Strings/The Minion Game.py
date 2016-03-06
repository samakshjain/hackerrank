# Enter your code here. Read input from STDIN. Print output to STDOUT
gameString = raw_input()
vowels = 'AEIOU'
stuart_score = 0
kevin_score = 0
gameStringLength = len(gameString)
for i in range(gameStringLength):
    if gameString[i] in vowels:
        kevin_score +=  (gameStringLength-i)
    else:
        stuart_score += (gameStringLength-i)
        
if (stuart_score > kevin_score):
    print "Stuart", stuart_score
elif(stuart_score < kevin_score):
    print "Kevin", kevin_score
else:
    print "Draw"