package main

/*
	bool

	string

	int int8 int16 int32 int64
	unit uint8 uint16 uint32 uint64 uintptr

	float32, float64

	complex64 complex128

	byte //alias for uint8

	rune	//alias for int
			//represent Unicode code point

	=================================
	intX, uintX, floatX, ...typeX => x is bytes

	int, uint and uintptr size depends on system word size
		i.e. they are 32bytes on 32bit systems and
			 		  64bytes on 64bit systems
*/
import (
	"fmt"
	"math/cmplx"
)

var (
	healthy          bool       = true
	name             string     = "ababa"
	age              int        = 1000000
	cash_on_hand     float32    = 100000000
	square_root_of_i complex128 = 10 + 2i

	square_root_of_negative complex128 = cmplx.Sqrt(-5)
	maxInt                  uint64     = 1<<64 - 1 //what is this?
	age_in_binary           string     = "11110100001001000000"
	zero_in_binary          byte       = 00000000 //2^19+ 2^18+ 2^17+ 2^16+ 2^14+ 2^9+ 2^6
	days_to_exam            rune
)

func main() {
	fmt.Printf("type: %T age in 32 bit binary format %32b\n", age, age)
	fmt.Printf("type: %T square_root_of_negative	%v\n", square_root_of_negative, square_root_of_negative)
	fmt.Printf("type: %T maxInt %v\n", maxInt, maxInt)
}
