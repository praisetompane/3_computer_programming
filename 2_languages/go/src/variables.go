package main

import (
	"fmt"
)

var c, python, java bool //var declars list of variables

var happy, sad, dance = true, true, "no!" //types inferred

var age, cars_count int = 15, 1

func main() {
	var i int
	fmt.Println(i, c, python, java)
	fmt.Println(happy, sad, dance)
	fmt.Println(age, cars_count)

	temperature := 30 //declares and assigns. NB: only available in function
	fmt.Println(temperature)
}
