my_string = 'hello'
print(my_string)

my_string = "hello"
print(my_string)

my_string = '''hello'''
print(my_string)

my_string = """hello"""
print(my_string)


#format string in python
name = "teerapat"
print(f"hello {name}".format())

print('name[-1]', name[-1])


print('name[1:5]', name[1:5])


print('name[5:2]', name[5:-2])

del my_string


my_string = "game"
# print(my_string)

count = 0
for letter in 'hello world':
    if letter == 'l':
        count +=1
print(count, 'letters found')

print( 'a' in 'programming')

print('pr' not in 'programming')


print('len(my_string) = ', len(my_string))

string = 'teerapat'

print('list(enumerate(string))', list(enumerate(string)))

print('He said , "What\'s is there"')

#formatting integers
print("Binary representation of {0} is {0:b}".format(12))

