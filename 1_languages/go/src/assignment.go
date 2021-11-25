package main

import "fmt"

var initial int = 0

func main() {

	fmt.Printf("initial: %v ", initial)
	fmt.Println()
	initial := 90
	fmt.Printf("Initial reassinged: %v ", initial)
	fmt.Println()
}