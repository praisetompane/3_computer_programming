package main

import (
	"fmt"
)

var a, b, z int

func main() {
	a_float := float64(a)
	//b_float float64 := b //fails, type conversion MUST be explicit
	b_float := float64(b)
	z_string := string(z)

	y := 1234
	y_string := string(y)
	y_string_alt := fmt.Sprintf(y_string)

	fmt.Println(a_float)
	fmt.Println(b_float)
	fmt.Println(z_string)
	fmt.Println(y_string)
	fmt.Println(y_string_alt)

}