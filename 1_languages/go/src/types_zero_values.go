package main

import "fmt"

/*
	0 for numeric values = {int, rune, float32, ...}
	"" for string values
	0+0i for imaginary numeric values
*/

var (
	age              int
	name             string
	height           rune
	cash_on_hand     float32
	imaginary_number complex128
)

func main() {
	fmt.Println(age)
	fmt.Println(name)
	fmt.Println(height)
	fmt.Println(cash_on_hand)
	fmt.Println(imaginary_number)
}
