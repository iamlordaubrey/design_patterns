### Observer Pattern

* Define a one-to-many dependency between objects so when one object changes state, all its dependents are notified and updated automatically.
* Encapsulate the core (or common / engine) components in a Subject abstraction, and the variable (or optional / user interface) components in an Observer hierarchy.
* The "View" part of Model-View-Controller.

Define an object that is the "keeper" of the data model and / or business logic (the Subject).
Delegate all "view" funcitionality to decoupled and distinct Observer objects.
Observers register themselves with the Subject as they are created.
Whenever the Subject changes, it broadcasts to all registered Observers that it has changed; Each Observer queries the Subject for that subset of the Subject's state that it is responsible for monitoring.


#### Structure

- Subject
	- Observer
	- Observer
	- Observer