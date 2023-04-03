def named(**kwargs):
	print(kwargs)

named(named="Bob", age=25)

details = {"name": "Bob", "age" : 25}
named(**details)

def both (*args, **kwargs):
	print(args)
	print(kwargs)

both(1,3,5, name="Bob", age=25)
