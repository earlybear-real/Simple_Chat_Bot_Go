package main

import "fmt"

func main() {
	fmt.Println("Hello! My name is Aid.")
	fmt.Println("I was created in 2023.")
	fmt.Println("Please, remind me of your name.")

	var name string
	// reading a name
	fmt.Scan(&name)

	fmt.Println("What a great name you have, " + name + "!")
}
