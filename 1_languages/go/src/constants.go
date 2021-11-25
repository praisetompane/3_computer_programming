package main

import "fmt"

const NeverToChange = "世界"
const pi = 3.14

func main() {

	fmt.Printf("NeverToChange: %v ", NeverToChange)
	fmt.Println()
	fmt.Printf("pi is: %v", pi)
	fmt.Println()

	pi := 1.1 //Expected to be invalid, but works. const must be declared in the scope??? See example below
	fmt.Printf("pi is: %v", pi)

	const euler_number = 2.71828
	fmt.Printf("Euler number: %v", euler_number)

	euler_number := pi //invalid as expected
	fmt.Printf("New Euler number: %v", euler_number)
}
