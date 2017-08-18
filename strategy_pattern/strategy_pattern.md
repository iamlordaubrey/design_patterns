### Strategy Pattern

Presents different potential solutions to the same problem, and allows ther program choose the most suitable one.

- Client (program to an interface, not an implementation)
	- Abstraction <<interface>> (O - open for extension, closed for modification)
		- Implementation 1
		- Implementation 2
		- Implementation 3

#### Structure

The interface entity could be an abstract base class

- Client
	- Context
	(**strategy**)
		- Interface
			- Implementation 1
			- Implementation 2
			- Implementation 3