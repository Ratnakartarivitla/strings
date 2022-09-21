# task - 13 strings
# strings and its operations - shall we start

s = "This is my name"
#upper()
print(s.upper())
#lower()
print(s.lower())
#count
print(s.count('name'))
#startswith
print(s.startswith("This"))
#endswith
print(s.endswith('name'))
#find
print(s.find('is')) # it return the index of is in string
#format
string = "i am {}".format('ratnakar') #we can make this statement dynamic using loops
#index
print(s.index('is'))


#isalnum
text = "test123"
print(text.isalnum()) #it contains both numbers and characters
#isdigit
a = "1234"
print(a.isdigit())
#split()
v = s.split()
print(v)
#join
v1= " ".join(v)
print(v1)
#strip
s1 = "    why so serious    "
print(s1.strip())
#lstrip rstrip
print(s1.lstrip())
print(s1.rstrip())
#title
print(s.title())
#replace
s3 = "i am apple"
print(s3.replace("apple","wartermelon"))

