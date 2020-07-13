// pass_fail reports whether a grade is passing or failing
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	fmt.Print("Enter a grade: ")
	// Set up a "buffered reader" that gets text from the keyboard
	reader := bufio.NewReader(os.Stdin)
	// Return everything the user has typed, up to where they pressed the Enter
	// key

	// use the blank identifier as a placeholder for the error value
	grade, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	if grade == 100 {
		fmt.Println("Perfect!")
	} else if grade >= 60 {
		fmt.Println("You pass.")
	} else {
		fmt.Println("You fail!")
	}
	fmt.Println(input)
}
