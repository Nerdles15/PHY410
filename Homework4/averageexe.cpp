//Create program that inputs a filename from command line containing list of students
//and computes a class average by passing a pointer to the vector to a function "calculate_average"
//Executable


#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include "StudentRecord.h"


float calculate_average(std::vector<StudentRecord> studentrecord){

	float total=0;
	int size=studentrecord.size();
	for (int i; i<studentrecord.size(); ++i) {

		total += studentrecord[i].score();

	}
	return total/size;
}

int main(int argc, char * argv[]) {
	std::ifstream input(argv[1]);

	std::vector<StudentRecord> studentrecord;
	float score(0);

	while ( !input.eof() ) {

		std::string line;

		std::getline( input, line, '\n');

		if (line != "") {

			std::stringstream buf(line);

			std::string token;
			std::getline( buf, token, ',');
			std::string lastname_ = line;
			std::getline( buf, token, ',');
			std::string firstname_ = line;
			std::getline( buf, token);
			float score = std::atof( token.c_str() );

			StudentRecord sr(lastname_, firstname_, score);
			studentrecord.push_back(sr);
			//std::cout /*<< firstname_ << " "*/ << lastname_ << " got a " << score << ".\n" << std::endl;
			// ^ checks if input values are read correctly
			//***correct odd issue where all info is saved under each name independently
		}

	}

	float avg=calculate_average(studentrecord);

	std::cout << "The average here is: " << avg << ".\n" << std::endl;

}