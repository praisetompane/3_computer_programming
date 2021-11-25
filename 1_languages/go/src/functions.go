package main

import "fmt"

func add(a int, b int) int {
	return a + b
}

func substract(a, b int) int { //shorthand: shared type can be added to ONLY the last function parameter
	return a - b
}

func swap(a, b string) (string, string) { //can return multiple values
	return b, a
}

func main() {
	fmt.Println(add(1, 2))
	fmt.Println(substract(2, 3))
	fmt.Println(swap("Apple", "Pear"))
}
