class Observer(object):
	def update(self, obj, *args, **kwargs):
		raise NotImplementedError

class Observable(object):
	def __init__(self):
		self._observers=[]
	
	def add_observer(self, observer):
		self._observers.append(observer)

	def remove_observer(self, observer):
		self._observers.remove(observer)

	def notify_observer(self, *args, **kwargs):
		for obs in self._observers:
			obs.update(self,*args,**kwargs)
