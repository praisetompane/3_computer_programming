/*
	package public interface is defined using
		names that start with capital letter
		i.e. Pi instead of pi for math pi function
*/
package main

import (
	"fmt"
	"math"
)

func main() {
	//fmt.Println(math.pi) does not run
	fmt.Println(math.Pi)
}
