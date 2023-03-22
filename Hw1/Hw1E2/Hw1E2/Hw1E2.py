import numpy as np

#alphabet to number key
alphaToNum = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

stringIn = input("Input Message to code: ").upper() #message input
n = int(input("Choose n: ")) #n input

#key input
key = []
for i in range(n):
    for j in range(n):
        key.append(int(input(f"Enter key value for[{i}][{j}]: ")))
key = np.array(key).reshape((n,n))
print(f"\nthis is your key:\n{key}\n")

#conversion from alpha to number
uncoded = []
for char in stringIn:
    for i in range(27):
        if(alphaToNum[i] == char):
            uncoded.append(i)
#filling extra spaces with zeroes
while(len(uncoded)%n != 0):
    uncoded.append(int(0))

#reshaping of array
m = int(len(uncoded)/n) #calculating number of columns
uncoded = np.array(list(uncoded)) #turn into array
uncoded = uncoded.reshape(m, n) #reshape array
print(f"this is your uncoded numbers:\n{uncoded}")

#coding and flattening
coded = (np.matmul(uncoded[:m],key)).flatten()
print(f"\nThis is your cryptogram:\n{coded}\n")

#inversing key
yek = np.linalg.inv(key)
print(f"Inverse key for decoding:\n{yek}\n")

#reshaping and decoding coded
coded = coded.reshape((m,n))
uncodedNew = np.matmul(coded[:m],yek)
print(f"decoded numbers:\n{uncodedNew}\n")

#flatten and convert from num to alpha
uncodedNew = uncodedNew.flatten()
stringOut = []
for num in uncodedNew:
    for i in range(27):
        if(i == num):
            stringOut.append(alphaToNum[i])
stringOut = "".join(stringOut)
print(f"Decoded Message: {stringOut}")