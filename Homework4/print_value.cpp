//Input text file and index on command line, prints students record at index given
//Be able to handle an index larger than number of students given

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include "StudentRecord.h"



int main(int argc, char * argv[]) {
	std::ifstream input(argv[1]);
	int index = std::atoi(argv[2]);

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

	if (index < studentrecord.size()){

		StudentRecord person = studentrecord[index];
		std::cout << "The chosen one is: " << person.lastname() << ", and they got: " << person.score() << ".\n" << std::endl;

	} else {
		std::cout << "I'm sorry, that data appears to have been erased from my memory...\n" << std::endl;
	}

}