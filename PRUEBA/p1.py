from array import array


array=[]

while True:
    try:
        array.append(input())

        for i in range(len(array)):
            print(array[i])



        
    except EOFError:
        break

