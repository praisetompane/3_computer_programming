/*
	all go programs are made up of packages
*/
package main //entry point for all go programs

import (
	"fmt"
	"math/rand" //convention: last element of imprt path is the package name(i.e. rand is the package name here)
)

func main() {
	fmt.Println("random number :", rand.Int())
}
