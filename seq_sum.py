import sys
#nums=list(map(int, input().split()))
nums=[3,3,4,13,23,13,4,5,23] #testovaci input, SMAZAT!
x=0
h=0
largestPrime=-sys.maxsize - 1
largestListLen=0 #largest list size
largestListIndex=-1
isSeq=False
previousSeq=False
equalLen=False
max=len(nums)-1
candidates=[[]]
equalLenCandidates=[] #součet prvků posloupností se stejnou délkou
#candidates[0].append(1)
#candidates[2].append(1)

def primetest(n):
    n=abs(n)
    for i in range(2,n+1):
        if n==1:
            return False
        if i==n:
            return True
        if n%i==0:
            return False

for i in range(0,max):
    previousSeq=isSeq
    isSeq=nums[i+1]>=nums[i] and primetest(nums[i+1])==True and primetest(nums[i])==True
    if isSeq:
        candidates[x].append(nums[i])
    if not isSeq and previousSeq: 
        #alternativne taky if isSeq==False and previousSeq: 
        #skoncila sekvence, pridavam posledni prvek:
        candidates[x].append(nums[i])
        x+=1
        candidates.append([])
    #nejvetsi prvocislo pro jednoprvkové posloupnosti
    if primetest(nums[i]) and nums[i]>largestPrime:
        largestPrime=nums[i]

if isSeq:
    candidates[x].append(nums[max])

# to same jen pro poslední prvek
if primetest(nums[max-1]) and nums[max-1]>largestPrime:
        largestPrime=nums[max]
        
#vybiram nejdelsi list:
for g in range(0,x+1):
    if len(candidates[g])==largestListLen:
        equalLen=True #dostal jsem dvě a více stejně dlouhých posloupností
        equalLenCandidates.append(candidates[largestListIndex])
        equalLenCandidates.append(candidates[g])
    if len(candidates[g])>largestListLen:
        largestListLen=len(candidates[g])
        largestListIndex=g
        if equalLen:
            equalLen=False
            equalLenCandidates.clear()

#check jestli je největších stejně dlouhých posloupností více -  bubble sort???
if equalLen:
    z = len(equalLenCandidates)
    print(z)

if len(candidates[0])==0:
    #nenalezena žádná nejednotková posloupnost, printuji největší prime integer
    print(len(candidates))
    print(largestPrime)
    #print results:
else:
    print(candidates)
    
if largestPrime==-sys.maxsize - 1:
    print("0")
    print("0")


print("++Control Outputs++")
print("largest sequences of equal lenght:")
print(equalLenCandidates)
print("lenght of the longest sequence:")
print(largestListLen)
print("does largest sequences of equal lenght even exist?")
print(equalLen)
