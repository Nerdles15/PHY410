//Create a program that calculates the factorial of an unsigned int if int < 20
//Create a function called factorial that does this.

#include <iostream>
#include <cmath>

//factorial function, has to output as LONG otherwise breaks down at n=13
long factorial(unsigned int n) {

	if (n > 1 && n < 20){
		return n * factorial(n - 1);
	} else {
		return 1;
	}

}

//stirling function
long stirling(unsigned int n) {

	if (n >= 20) {
		return n * log(n) - n;
	} else {
		return 0;
	}
}

int main(void) {

	unsigned int n;

	std::cout << "Enter an integer below 20, and I will give you another one: \n";
	std::cout << "Enter an integer 20 or above, and Stirling will give you another one: ";
	std::cin >> n;

	if (n < 20 || n == 0) {
		std::cout << n << " factorial " << "= " << factorial(n) << "\n";	
	} else {
		//std::cout << "Please input an integer BELOW 20...abort, retry...\n";
		std::cout << "Stirling's approximation of " << n << " is roughly " << stirling(n) << "\n";
	}

}