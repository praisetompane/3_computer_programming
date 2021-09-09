# imprecise but fun way to think about these

What can you offer me, what's your solution?:
* We can do things => Declarative

# There is a lot of things to do, what's your solution?:
* We can do these things at the same toime => Concurrent Declarative

    * value: define mathematical functions
       easier to reason about and test

# There is too much going on from doing things at the same time, to finish all the things we need to do, thus WE are running out of resources, What is your solution?:
* We want to do these things at the same time ONLY when we need to => Lazy Declarative

    * value: adds dataflow concurrency
       retains declarative properties
       allows/adds flexible and incremental execution

# We are doing lots of things at the same time, but we forget after we are done, thus have have to redo them when we need them, We are running out of resources,
## What is your solution?
* We want to do these things at the same time ONLY when we need to ans save the result of our work => Stateful 

    * value: explicit state
       allows programs whose behavior can change over time
       IF correcly done(i.e. using encapsulation, invariants),
            can reason easily and test like declarative ones
# We are doing lots of things at the same time and saving our results everywhere and stepping over each otherm it is a mess!
## What is your solution?
* We want to do these things at the same time ONLY when we need to and save the result of our work in an organised way separate from each other => Object Orientated

    * value:  gives us object orientated programming(OOP)
        OOP := programming style, for stateful programming with data abstractions.
        allows ease of use of powerful techniques
            - polymorphism
            - inheritance
            ...
# We are doing lots of things at the same time and saving our results in an organised way separate from each other,but there is some resource we HAVE to share[read and write to].
## What is your solution?
* Shared State Concurrent
    * value:  combines stateful and concurrent
        IF correcly done    
            with techniques for mastering interleaving
                techniques := {monitoring, transactions}
        benefits of Stateful and Concurrent

