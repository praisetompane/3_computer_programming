/*
    for rotations
        foreach index
            newIndex = index - 1
            if newIndex >= 0
                newArray[newIndex] = array[index]
            else
                newArray[lastIndex] = array[index]
*/
def rotLeft(a: Array[Int], d: Int): Array[Int] = {
        

        //Example of calculating a future state once
        def calculateTargetIndex(currentIndex: Int, rotationsLeft: Int): Int = {
                val decrement = 1
                val newIndex = currentIndex - decrement
                if(rotationsLeft <= 0) currentIndex
                else {
                    if(newIndex < 0) calculateTargetIndex(a.length - decrement, rotationsLeft - decrement)
                    else calculateTargetIndex(newIndex, rotationsLeft - decrement)
                }
        }

        val newArray = new Array[Int](a.length)
        
        a.zipWithIndex.foreach{
            case(value: Int, index: Int) =>  newArray(calculateTargetIndex(index, d)) = value
        }

        newArray
}

