# Design-Patterns
## Structural Design Patterns
### Adapter Design Pattern:
* To call different call methods of classes, I have created a adapter class which calls the methods of the respective classes.
* But still, we have to make instances of the classes in the main function and set their respective attributes as function pointers of the classes that they will call, which is not that cool!
* You can also access attributes of the classes from the adapter, even if the attributes are private!

### Facade Design Pattern:
* To call different call methods of classes via a adapter, I have created a facade class which calls the adapter and which futher calls methods of the respective classes.
* Here, we do not have to make instances of the classes in the main function but in facade design class, from where we call the adapter, which is cool!
* You can also access attributes of the classes from the facade, from the adapter, even if the attributes are private!

### Observer Design Pattern:
* Observer Pattern lets us keep track of any changes in the instance values we are observing.
* Observer class has one update method which is to be overridden to print the change notification after the change is made in the setattr method.
* Observable class lets us manage our adding, removing observers which is used as a parent class to the Adapter method to add observers to the adapters. Pretty Cool!

### Singleton Design Pattern:
* Singleton Pattern is useful when you need a single instance of any class, and every other thing goes around with that only instance.
* In the Parking Lot example, we only need one instance of the lot class, so we can use the singleton design pattern there. 
* We have to make a static getInstance method to retrieve the only created instance whenever we need to.

