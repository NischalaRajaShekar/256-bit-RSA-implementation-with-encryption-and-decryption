import os
import random
import math
import sys

#Function to prepend 128 zeros in the input text file
def prependZeros(mainFile, zero):
    f1 = open(mainFile, 'r')
    f2 = open("newFile.txt","w")
    for i in range(128):
        f2.write(zero)
    f2.write(f1.read())
    f1.close()
    f2.close()

#Function to check if the number generated is Prime
def isPrime(a):
    return all( a % i for i in range(2,a))

#Function to generate prime number within a provided range
def generatePrime(min,max):
    primeNum = [i for i in range(min,max) if isPrime(i)]
    num = random.choice(primeNum)
    return num

#function to check if leftmost values of 'p' and 'q' are set
def check_pq(pBi):
    while (pBi != '11'):
        p = generatePrime(2,100)
        pBi = bin(p)[2:4]
    return p

#Euclid's algorithm to determine gcd
def gcd(a,b):
    while (b != 0):
        a, b = b, a % b
    return a

#Extended Euclidean algorithm 
def euclidAlgo(emod, phiN):
    if (phiN == 0):
        return (1,0)
    (q,r) = (emod//phiN, emod%phiN)
    (s,t) = euclidAlgo(phiN, r)
    return (t, s-(q*t))

#Extended Euclidean algorithm to find multiplicative inverse of two numbers
def multiplicativeInverse(e, phi):
    inv = euclidAlgo(e,phi)[0]
    if (inv < 1):
        inv += phi
    return inv

#Function to decrypt the encrypted file using RSA decryption
def decryptFunction(cipherFile):
    encryptedCopy = open("encryptFile.txt","r+")
    encryptCopy1 = encryptedCopy.readline().strip()
    encryptCopy = encryptCopy1.split(" ") 
    decryptionFile = open(decryptFile,"w")
    decryptList =[]
    readvariables = open("variableValues.txt","r+")
    readvariables1 = readvariables.readline()
    n = int(readvariables1)
    readvariables2 = readvariables.readline()
    d = int(readvariables2)
    
    #read values from the file and decrypt with 'd' and n
    for i in encryptCopy:
        a = int(i)
        decrypt = chr((a ** d) % n)
        decryptList.append(decrypt)

    #remove padded zeros and newline characters to make printable ASCII
    end = len(decryptList)
    for i in decryptList[128:end]:
        decryptionFile.write(i)
    decryptionFile.close()
    encryptedCopy.close()
    return decryptionFile

#Read command line arguments for encrypt and decrypt
if (sys.argv[1] == '-e'):
    inputFile = sys.argv[2]
    outputFile = sys.argv[3]
if (sys.argv[1] == '-d'):
    outputFile = sys.argv[2]
    decryptFile = sys.argv[3]
    decryptFunction(outputFile)
    exit()
    
readFile = open(inputFile,"r+")
copyFile = open("copyFile.txt","w")
for i in readFile:
    copyFile.write(i)
copyFile.close()
copyFile = open("copyFile.txt","r+")
newFile = copyFile.read()
#Read the input file and append newline characters until a length of 128 multiple
remainderBits = len(newFile) % 128
if remainderBits != 0:
    for i in range(128 - remainderBits):
        writeFile = open("copyFile.txt","a")
        writeFile.write("\n")
    writeFile.close()
readFile.close()
copyFile.close()

#Calculate prime numbers 'p' and 'q'
pBi = 0
qBi = 0
p = check_pq(pBi)
e = 65537
g = gcd((p-1),e)
while (g != 1):
    p = check_pq(0)
    g = gcd((p-1),e)
    
q = check_pq(qBi)
while (q == p):
    q = check_pq(0)
    
gQ = gcd((q-1),e)
while (gQ != 1):
    q = check_pq(0)
    gQ = gcd((q-1),e)

#Generate phi(n), n and d
phiOf_n = (p-1)*(q-1)
n = p*q
d = multiplicativeInverse(e, phiOf_n)

variable = open("variableValues.txt","w+")
variable.write(str(n) + "\n")
variable.write(str(d))
variable.close()

prependZeros("copyFile.txt","0")
os.remove("copyFile.txt")

#Encryption of the input file using RSA encryption
finalText = open("newFile.txt","r+")
asciiConv = finalText.read()
cipherFile = open(outputFile,"w+")
encryptionList = []
for i in asciiConv:
    cipher = (ord(i)**e) % n
    cipherFile.write(str(cipher))
    encryptionList.append(cipher)
cipherFile.close()

copyOfEncryptList = open("encryptFile.txt","w+")
for i in encryptionList[:]:
    copyOfEncryptList.write(str(i) + " ")
copyOfEncryptList.close()




