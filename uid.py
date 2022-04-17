import string
import random
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")

def gen():
	length = 10
	alphabets_count = 5
	digits_count = 5
	characters_count = alphabets_count + digits_count
	if characters_count > length:
		print("Characters total count is greater than the password length")
		return
	password = []
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))
	for i in range(digits_count):
		password.append(random.choice(digits))
	random.shuffle(password)
	return ("".join(password))