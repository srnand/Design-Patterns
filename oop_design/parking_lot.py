import collections
class LinkedList(object):
	def __init__(self,spot=None):
		self.spot=spot
		self.next=None

class Vehicle(object):
	def __init__(self,size=None,license=None):
		self._size=size
		self._license=license
		self._spot=None

	def park(self,spot):
		self._spot=spot

	def unpark(self):
		self._spot=None

	def findParkingSpot(self):
		return self._spot

	def getSize(self):
		return self._size

class Bus(Vehicle):
	def __init__(self,license=None):
		super(Bus,self).__init__(3,license)

class Bike(Vehicle):
	def __init__(self,license=None):
		super(Bike,self).__init__(1,license)

class Car(Vehicle):
	def __init__(self,license=None):
		super(Car,self).__init__(2,license)

class Spot(object):
	def __init__(self,row=None,col=None,size=None):
		self.row=row
		self.col=col
		self.size=size
		self._fill=False
		self.vehicle=None

	def fillSpot(self,vehicle):
		self._fill=True
		self.vehicle=vehicle

	def UnfillSpot(self):
		self._fill=False
		self.vehicle=None

class Lot(object):
	__instance=None

	@staticmethod
	def getInstance():
		if not Lot().__instance:
			Lot()
		return Lot().__instance

	def __init__(self):
		Lot.__instance=self

		self._availableSpotsSmall=LinkedList(Spot())
		self._availableSpotsMed=LinkedList(Spot())
		self._availableSpotsLarge=LinkedList(Spot())

		self._headSmall=self._availableSpotsSmall
		self._headMed=self._availableSpotsMed
		self._headLarge=self._availableSpotsLarge

		for i in range(1,6):
			for j in range(1,6):
				self._availableSpotsSmall.next=LinkedList(Spot(i,j,1))
				self._availableSpotsSmall=self._availableSpotsSmall.next

				self._availableSpotsMed.next=LinkedList(Spot(i,j,2))
				self._availableSpotsMed=self._availableSpotsMed.next

				self._availableSpotsLarge.next=LinkedList(Spot(i,j,3))
				self._availableSpotsLarge=self._availableSpotsLarge.next

		self._occupiedSpots=collections.defaultdict(tuple)

	def findSpotAndPark(self,vehicle):
		size=vehicle.getSize()

		if size==1:
			spot=self._headSmall.next
			self._headSmall.next=self._headSmall.next.next

		elif size==2:
			spot=self._headMed.next
			print spot,"SPOT"
			self._headMed=self._headMed.next.next

		elif size==3:
			spot=self._headLarge.next
			self._headLarge.next=self._headLarge.next.next

		self._occupiedSpots[(spot.spot.row,spot.spot.col,spot.spot.size)]=vehicle

		spot.spot.fillSpot(vehicle)
		vehicle.park(spot.spot)

		return spot.spot

	def Unpark(self,spot):
		vehicle = self._occupiedSpots[(spot.row,spot.col,spot.size)]
		del self._occupiedSpots[(spot.row,spot.col,spot.size)]
		vehicle.unpark()


		if spot.size==1:
			self._availableSpotsSmall.next=LinkedList(Spot(spot.row,spot.col,1))
			self._availableSpotsSmall=self._availableSpotsSmall.next

		elif spot.size==2:
			self._availableSpotsMed.next=LinkedList(Spot(spot.row,spot.col,2))
			self._availableSpotsMed=self._availableSpotsMed.next

		elif spot.size==3:
			self._availableSpotsLarge.next=LinkedList(Spot(spot.row,spot.col,3))
			self._availableSpotsLarge=self._availableSpotsLarge.next

if __name__ == '__main__':
	lot=Lot.getInstance()

	car=Car("MNBV123")
	lot.findSpotAndPark(car)
	print car.findParkingSpot()
	lot.Unpark(car.findParkingSpot())
	print car.findParkingSpot()