#gets the integers the user enters into a list, making sure they're integers

numbers=list()                            #create an empty list to add to

while len(numbers)<10:                    #keep going through the following loop until the length 
    num=input("Enter an integer: ")       #of the list is less than 10 (on the 9th run through 
    try:                                  #the 10th integer gets added to the list)
        fnum=int(num)
        numbers.append(fnum)              #use a try/except to test if the input is an integer
    except:                               #if the input isn't an integer, the user is told and 
        print('Invalid input')            #the while loop continues.  If it is, it's appended to 
        continue                          #the list.

#calculates mean

sum=0                                     #set the variable sum to 0

for item in numbers:                      #iterate through the list, adding the items to sum
    sum=sum+item
mean=sum/len(numbers)                     #calculate the mean, store in variable mean

#calculates variance and standard deviation

squaresums=0                              #set the variable squaresums to 0

for item in numbers:                      #iterate through the list, adding the square of the difference
    squaresums=squaresums+(item-mean)**2  #between the item and the mean
var=squaresums/len(numbers)               #calculate the population variance, store in variable var
std=(var)**0.5                            #calculate the population standard deviation, store in std

#calculates the max and min

maxsofar=numbers[0]                       #set the max of the list to the first item in the list
minsofar=numbers[0]                       #set the min of the list to the first item in the list

for item in numbers:                      #iterate through the list, asking if the item is greater
    if item>=maxsofar:                    #than the current set max. If so, replace maxsofar variable.
        maxsofar=item
for item in numbers:                      #iterate through the list, asking if the item is less
    if item<=minsofar:                    #than the current set min. If so, replace minsofar variable.
        minsofar=item
    
print("Your numbers are: ", numbers)                        #print list of integers
print("The minimum of your numbers is: ", minsofar)         #print min
print("The maximum of your numbers is: ", maxsofar)         #print max
print("The range of your numbers is: ", maxsofar-minsofar)  #print range by taking max minus min
print("The mean of your numbers is: ", mean)                #print mean
print("The variance of your number is :",var)               #print variance
print("The standard deviation of your numbers is: ",std)    #print standard deviation