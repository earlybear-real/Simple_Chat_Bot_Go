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

	var rem3, rem5, rem7, age int
	fmt.Scan(&rem3, &rem5, &rem7)

	age = (rem3*70 + rem5*21 + rem7*15) % 105

	fmt.Printf("Your age is %d; that's a good time to start programming!\n", age)
	fmt.Println("Now I will prove to you that I can count to any number you want.")

	// read a number and count to it here
	var inputNum int
	fmt.Scan(&inputNum)

	for i := 0; i <= inputNum; i++ {
		fmt.Println(i, "!")
	}

	fmt.Println("Congratulations, have a nice day!")
}
