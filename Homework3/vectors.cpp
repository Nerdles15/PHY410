//write program to take 2D input vectors, loops over to find pair
//with minimum magnitude. Print to screen.

#include <iostream>
#include <cmath>

int main(void) {

	std::cout << "Please enter vector pairs (xi, yi) and I'll tell you the smallest magnitude entered.\n" << std::endl;
	std::cout << "Type '!q' to exit...or realistically anything that isn't a vector...\n" << std::endl;
	float xi = 0., yi = 0.;
	float xmin, ymin, tmag, minmag = 10000000000;
	while ( std::cin >> xi >> yi ) {
		std::cout << "Vectors entered are: " << xi << ", " << yi << "\n" << std::endl;
		float tmag = sqrt(xi * xi + yi * yi);
		std::cout << "Vector magnitude is: " << tmag << ".\n" << std::endl;

//set a temporary magnitude, run loop that checks if currently input mag is less than temp
//if temporary magnitude less than current, replaces current.		
		if ( tmag < minmag ) {
			minmag = tmag;
		}
		std::cout << "Your smallest magnitude vector is: " << minmag << ".\n" << std::endl;
	}

}