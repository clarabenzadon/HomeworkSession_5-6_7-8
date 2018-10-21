string = input("Enter a string of characters")
finalstring = ""
prestring = ""
pre = "a"

for c in string:
    if c>= pre:
        prestring += c
    else:
        if len(prestring) > len(finalstring):
            finalstring = prestring
        prestring = c
    pre = c

print("The longest string of characters in alphabetical order is:" +finalstring )
