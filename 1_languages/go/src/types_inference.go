package main

import "fmt"

var base int = 0

func main() {
	int_inferred := base

	fmt.Printf("Type inferred from Right Hand Side's type. Type: %T , value: %v", int_inferred, int_inferred)
	fmt.Println()

	constant_precision_inferred_type_int := 1//i.e 1's precision
	fmt.Printf("Type inferred from Right Hand Side's constant precision. Type: %T, value: %v", constant_precision_inferred_type_int, constant_precision_inferred_type_int) 
	fmt.Println()

	constant_precision_inferred_type_float := 1.1//i.e 1.1's precision
	fmt.Printf("Type inferred from Right Hand Side's constant precision. Type: %T, value: %v", constant_precision_inferred_type_float, constant_precision_inferred_type_float) 
	fmt.Println()

	constant_precision_inferred_type_complex := 1.1 + 90i//i.e highest constant's precision
	fmt.Printf("Type inferred from Right Hand Side's constant precision. Type: %T, value: %v", constant_precision_inferred_type_complex, constant_precision_inferred_type_complex) 
	fmt.Println()

}
