package main

import "fmt"

func main() {
	fmt.Println("Hello! My name is Aid.")
	fmt.Println("I was created in 2023.")
	fmt.Println("Please, remind me of your name.")

	var name string
	fmt.Scan(&name)

	fmt.Println("What a great name you have, " + name + "!")
	fmt.Println("Let me guess your age.")
	fmt.Println("Enter remainders of dividing your age by 3, 5 and 7.")

	// reading all remainders
	var age int
	var remainder3 int
	var remainder5 int
	var remainder7 int

	fmt.Scan(&remainder3)
	fmt.Scan(&remainder5)
	fmt.Scan(&remainder7)

	age = (remainder3*70 + remainder5*21 + remainder7*15) % 105

	fmt.Printf("Your age is %d; that's a good time to start programming!\n", age)
}
