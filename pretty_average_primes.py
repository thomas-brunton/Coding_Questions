from pathlib import Path

#Test data was retrieved from https://www.cemc.uwaterloo.ca/contests/computing/2019/index.html?fbclid=IwAR0ZZiB69k31Mi8LRRVKT6hQ1GfeRHuupnC5AVyEsniaVV2ofy2sB7al1iY

#Previous calculations for what numbers are prime or not
primeNums = {}
notPrimeNums = {}

def prettyAveragePrimes(inputNum):
    highestNum = inputNum * 2
    primes = getPrimes(highestNum, highestNum, highestNum)
    return primes

def getPrimes(num1, num2, highestNum):
    if num1 + num2 == highestNum:
        return (num1, num2)
    elif num1 == 0 or num2 == 0:
        return None

    set1 = getPrimes(findPrimeNum(num1 - 1), findPrimeNum(num2), highestNum)
    if set1 is not None:
        return set1
    else:
        set2 = getPrimes(findPrimeNum(num1), findPrimeNum(num2 - 1), highestNum)
        if set2 is not None:
            return set2
        else:
            set3 = getPrimes(findPrimeNum(num1 - 1), findPrimeNum(num2 - 1), highestNum)
            if set3 is not None:
                return set3

def findPrimeNum(num):
    if isPrime(num):
        return num

    return findPrimeNum(num-1)

def isPrime(num):
    #Return true/false if we have already calculated whether the number is prime or not
    if num in primeNums:
        return True
    elif num in notPrimeNums:
        return False

    isPrime = True
    divider = num
    while divider > 1:
        if divider != num and num % divider == 0:
            isPrime = False
        divider -= 1

    #Save calculation of whether number is prime for later use
    if isPrime == True:
        primeNums[num] = num
    else:
        notPrimeNums[num] = num

    return isPrime

inputFile = open("all_data\\s2\\s2.1-02.in", 'r')
firstLine = inputFile.readline()
for line in inputFile:
    print(prettyAveragePrimes(int(line)))
inputFile.close()
