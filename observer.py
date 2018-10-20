from observer_pattern import Observer, Observable

class A(object):
	_name="A"
	def call_A(self):
		print "You have called A!"

class B(object):
	def call_B(self):
		print "You have called B!"

class C(object):
	def call_C(self):
		print "You have called C!"


class MyObserver(Observer):
	def update(self, obj, *args, **kwargs):
		print "Hello! There is something new to observe!"
		print "{0}:{1}:{2}".format(obj,args,kwargs)

class Adapter(Observable):
	_initialised=False	#private class variable

	def __init__(self, obj, **adapted_methods):
		super(Adapter,self).__init__()

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
			self.notify_observer(key=key, value=value)

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

	@classmethod
	def monitor(facade,observer):
		facade.adapters[0].add_observer(observer)
		print "Added Observer"

	@classmethod
	def change_name(facade, newName):
		facade.adapters[0]._name=newName

if __name__ == '__main__':
	myObserver = MyObserver()

	Facade.create_adapters()
	# Facade.summon_adapters()
	Facade.monitor(myObserver)
	Facade.change_name("New Name: AA")

