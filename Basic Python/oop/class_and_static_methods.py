class ClassTest:
	def instance_method(self):
		print(f"instancemethod {self}")

	@classmethod
	def class_method(cls):
		print(f"called classmethod {cls}")

	@staticmethod
	def static_method():
		print("Called static method")


test = ClassTest()
test.instance_method()
ClassTest().instance_method()
ClassTest.class_method()
ClassTest.static_method()
