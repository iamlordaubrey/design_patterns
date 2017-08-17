# Design Patterns (Python 3.*)

### What?
It's a model solution to a common design problem. It describes the problem and a general approach to solving it

### Why?
To ensure that our work is **consistent**, **reliable** and **understandable**

### Categories
Creational (creating things (objects))
- Factory
- Builder
- Singleton

Structural (design relationships between objects)
- Adapter
- Facade
- Composite

Behavioural (object interaction and responsibility)
- Command
- Observer
- Strategy

Others categories are:
Concurrency patterns (multi-threaded systems)

### SOLID Principles of Object Oriented Design
- Single responsibility: A class should have only one responsibility
- Open-closed: A class should be open for extension (usually by inheritance) but closed for modification
- Liskov subsitution: Sub-classes should be able to stand-in for their parents without breaking anything
- Interface segregation: Many specific interfaces are better than one do-it-all interface (in Python: Abstract-based classes combined with multiple inheritance)
- Dependency Inversion: Program towards abstraction, not implementations (implementations can vary, abstractions should not)
