
def bubbleSort( number ):
    n = len( number )

    for i in range( n - 1 ) :
        flag = 0

        for j in range(n - 1) :
            
            if number[j] > number[j + 1] : 
                tmp = number[j]
                number[j] = number[j + 1]
                number[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return number

el = [4,62,39,53,71,12,18,93,21] 

result = bubbleSort(el)

print (result)