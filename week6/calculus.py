n = 100
numbers = [i for i in range(2,n)]
print( numbers)
results = []
ls = []
for n in numbers:
    #print "numbers = ", numbers
    if n not in ls:
        results.append(n)
        #print "num = ", n
        
        for i in numbers:
            if i % n == 0:
                ls.append(i)
# print( "results = ",results )           
# print( "len = ",len(results) )

#################################################
rfast = 0.3
rslow = 0.4

nfast = 1
nslow = 1000
yr = 1

while nslow > nfast:
    nfast = (nfast + nfast)*0.7
    nslow = (nslow + nslow)*0.6
    yr +=1
    print ("yr = ", yr ,"nslow = ", nslow, "nfast = ", nfast)
    