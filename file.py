#1 countdown - Create a function that accepts a number as an input. return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(i):
    result = []
    for i in range(i, -1, -1):
        result.append(i)
    return result

print(countdown(5))




#2 Print and Return - create a function that will receive a list with two numbers. Print the first value and return the second. (ex: print_and_return([1,2]) should print 1 and return 2)

def pAndR(num1,num2):
    print(num1)
    return num2

print(pAndR(1,2))


#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.(ex: first_plus_length([1,2,3,4,5]) should return 6 (first value:1 + length:5)

def sumAndLen(i):
    return i[0] + len(i)

print(sumAndLen([1,2,3,4,5]))


#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False (EX: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]) (EX: values_greater_than_second([3]) should return False)

def greaterSecond(i):
    if len(i) < 2:
        return False
    else:
        secondVal = i[1]
        newList = []
        for num in i:
            if num > secondVal:
                newList.append(num)
        print(len(newList))
        return newList
    
print(greaterSecond([5,2,3,2,1,4]))



#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value. (EX: length_and_value(4,7) should return [7,7,7,7]) (EX:  length_and_value(6,2) should return [2,2,2,2,2,2])


def length_and_value(a,b): #a = length & b = value
    result=[] #make a new list for the result
    for i in range(a): #for loop for range of a (length)
        result.append(b) #add b to the new list = to a (length)
    return result #return result

print(length_and_value(6,2)) #call to the function













