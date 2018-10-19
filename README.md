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

