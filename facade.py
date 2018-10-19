class A:
	_name="A"
	def call_A(self):
		print "You have called A!"

class B:
	def call_B(self):
		print "You have called B!"

class C:
	def call_C(self):
		print "You have called C!"

class Adapter(object):
	_initialised=False	#private class variable

	def __init__(self, obj, **adapted_methods):
		self.obj=obj
		for key, value in adapted_methods.items():
			function = getattr(self.obj,value)
			self.__setattr__(key,function)

		self._initialised=True

	def __getattr__(self,attr):
		return getattr(self.obj,attr)

	def __setattr__(self,key,value):
		if not self._initialised:
			super(Adapter,self).__setattr__(key,value)
		else:
			setattr(self.obj,key,value)

class Facade:
	adapters=None

	@classmethod
	def create_adapters(facade):
		facade.adapters=[Adapter(A(),call='call_A'),Adapter(B(),call='call_B'),Adapter(C(),call='call_C')]
		print "Created Adapters for A, B and C!"

	@classmethod
	def summon_adapters(facade):
		for adapter in facade.adapters:
			adapter.call()

if __name__ == '__main__':
	Facade.create_adapters()
	Facade.summon_adapters()

