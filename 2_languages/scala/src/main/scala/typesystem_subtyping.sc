/*
    Bill Venners
    https://www.youtube.com/watch?v=vuTFg5g_f6w
*/
trait Fruit
trait Plum extends Fruit
trait Apricot extends Fruit
trait Pluot extends Plum with Fruit

/*
    def: is-a-subtype-of relationship

        Fruit
        ^
        |
        |is-a-subtype-of
        |
        Plum

            is-a-subtype-of
        Plum -----------------> Fruit

        -----------------> = =>(function arrow): function from Plum to Fruit
        
        is-a-subtype-of relationship attributes:
            - conversion from a subtype to supertype is implicitly applied(by compiler, runtime, etc)
            - conversion of subtype to supertype does not NEED to change memory
            - transitive and reflexive
                transitive: the lowest subtype of type is also the subtype of all its supertypes
                reflexive: a type is a substype of itself
*/

println("In interesting way to think about, from Bill Venners")
//Plum => Fruit
def plumToFruit(plum:Plum):Fruit = plum
def eat(fruit:Fruit):Unit = println("Yum")

println("Given a Plum I can")
eat(plumToFruit(new Plum{}))

println("Or Given a Plum I can")
eat(new Plum{})// NB: The subtype relationship(i.e. function) implicitly converts the Plum to a Fruit

