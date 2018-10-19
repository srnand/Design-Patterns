class A:
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

	def __setattr__(self,key,value):
		if not self._initialised:
			super(Adapter,self).__setattr__(key,value)
		else:
			setattr(self.obj,key,value)

if __name__ == '__main__':
	adapters=[Adapter(A(),call='call_A'),Adapter(B(),call='call_B'),Adapter(C(),call='call_C')]

	for adapter in adapters:
		adapter.call()
	