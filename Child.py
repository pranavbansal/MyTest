"""Open a file, read its content, search for a pattern 
and display result on terminal"""

data = open('myfile.txt', 'r') # Open a file
data1 = data.readline() # read its content
data.close()

def stringtolistconversion(string): #Function for split string into string
    buddy = list(string.split(' '))
    return buddy


data2 = stringtolistconversion(data1) #Calling function 
# print(data2)
# print(data2[3])

if "Pranav" in data2: # search for a pattern
    print("Pranav") # display result on terminal
else:
    print("Not Pranav") # display result on terminal


