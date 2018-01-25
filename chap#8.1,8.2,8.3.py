#8.1
def make_shirt(size, message):
    print("The size of shirt is "+size.upper()+".")
    print("The message printed on the shirt is "+message+".\n")

make_shirt('XL','sunshine on the beach')
make_shirt(size = 'XL',message = 'sunshine on the beach')


#8.2
def make_shirt(size = 'large',message = 'I love python'):
    print("The size of my shirt is "+size+" and "+message+".\n")
make_shirt()
make_shirt('meduim')
make_shirt('small','I alse love Java')

#8.3
def describe_city(city, country = 'Pakistan'):
    print(city+" is in "+country+".")
describe_city('Karachi')
describe_city('Multan')
describe_city('beijing','China')

