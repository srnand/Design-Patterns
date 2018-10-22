import collections
import enum
import bisect

class ElevatorFactory(object):
	def moveUp(self):
		raise NotImplementedError
	def moveDown(self):
		raise NotImplementedError
	def addNewDestination(self,destination):
		raise NotImplementedError
	def direction():
		raise NotImplementedError
	def getStatus():
		raise NotImplementedError

class ControlSystemFactory(object):
	def pickup(self,loc):
		raise NotImplementedError
	def destination(self):
		raise NotImplementedError
	def step(self):
		raise NotImplementedError

class ElevatorStatus(enum.Enum):
	ElevatorActive=1
	ElevatorInActive=2

class ElevatorDirection(enum.Enum):
	Up=1
	Down=2
	Hold=3

class Elevator(ElevatorFactory):
	def __init__(self,cf=1):
		self._current_floor=cf
		self._destination=[]

	def addNewDestination(self,destination):
		bisect.insort(self._destination,destination)

	def currentFloor(self):
		return self._current_floor

	def moveUp(self):
		self._current_floor+=1

	def moveDown(self):
		self._current_floor-=1

	def direction(self):
		if len(self._destination)==0:
			return ElevatorDirection.Hold
		else:
			if self._destination[0]>self._current_floor:
				return ElevatorDirection.Up
			elif self._destination[0]<self._current_floor:
				return ElevatorDirection.Down
	def getStatus(self):
		if len(self._destination)>0:
			return ElevatorStatus.ElevatorActive
		else:
			return ElevatorStatus.ElevatorInActive

class ControlSystem(ControlSystemFactory):
	def __init__(self, maxElevators, maxFloors):
		self._elevators=[]
		self._pickups=[]
		self._maxElevators=maxElevators
		self._maxFloors=maxFloors

		for i in range(self._maxElevators):
			self._elevators.append(Elevator())

	def pickup(self,loc):
		bisect.insort(self._pickups,loc)

	def printElevatorQueue(self):
		for i in self._elevators:
			print i

	def step(self):
		print self._pickups
		for elevator in self._elevators:
			if elevator.getStatus()==ElevatorStatus.ElevatorInActive:
				if self._pickups:
					elevator.addNewDestination(self._pickups.pop())

			elif elevator.getStatus()==ElevatorStatus.ElevatorActive:
				if elevator.direction()==ElevatorDirection.Up:
					elevator.moveUp()
					currentFloor=elevator.currentFloor()
					print self._pickups,currentFloor
					pos=bisect.bisect_left(self._pickups,currentFloor)
					elevator.addNewDestination(self._pickups.pop(pos))
					print elevator._destination

				elif elevator.direction()==ElevatorDirection.Down:
					elevator.moveDown()
					currentFloor=elevator.currentFloor()
					pos=bisect.bisect_left(self._pickups,currentFloor)
					elevator.addNewDestination(self._pickups.pop(pos-1))

if __name__ == '__main__':
	controlSystem = ControlSystem(2,10)
	controlSystem.pickup(3)
	controlSystem.pickup(6)
	controlSystem.pickup(8)
	controlSystem.pickup(9)
	controlSystem.step()
	controlSystem.step()
	controlSystem.printElevatorQueue()


