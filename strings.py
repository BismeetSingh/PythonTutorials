

message="Hello world"
print(message)

#Length of the string
print(len(message))

#Quotes and escaping
var1="AI'\s world"
print(var1)


#Multiline text
var="""AI will take over the world
and that day will never come"""
print(var)



#Slicing
#First character
print(message[0])
#Last character
print(message[len(message)-1])
#Range
print(message[0:5])
print(message[:5])
print(message[6:])

#Index  error
print(message[11])