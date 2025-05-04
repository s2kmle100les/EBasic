import EBasic

while True:
	text = input('basic > ')
	result, error = EBasic.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)