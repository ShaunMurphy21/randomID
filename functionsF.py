import random
import string
import json

chars = string.ascii_letters + '123456789'
chars0 = string.ascii_letters
numbers = string.digits
x = []

def address_Gen():
    address1 = ''.join(random.choice(string.digits)for i in range(2))
    address2 = ''.join(random.choice(chars)for i in range(6))
    addy = address1 + ' ' + address2.upper() + ' GARDENS'
    return addy

def postGen():
	post1 = ''.join(random.choice(chars0)for i in range(2))
	post2 = ''.join(random.choice(numbers)for i in range(2))
	post3 = ''.join(random.choice(chars0)for i in range(2))
	postcode = post1.upper() + post2.upper() + post3.upper()
	return postcode
	
def ranEmail():
	for i in range(10):
		x.append('@' + ''.join(random.choice(chars0.lower())for i in range(5)) + '.com')	
	name = json.loads(open('names.json').read())
	b = (random.choice(name)) + ''.join(random.choice(numbers)for i in range(3)) + (random.choice(x))
	return b

def phone():
    num = '077' + ''.join(random.choice(string.digits)for i in range(8))	
    return num


def printID():
	x = address_Gen()+ '\n' +postGen()+ '\n'+ranEmail()+'\n'+phone()
	return x























