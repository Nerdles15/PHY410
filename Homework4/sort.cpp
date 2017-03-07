//Reads input file and sorts the results


#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "StudentRecord.h"


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

	std::sort(studentrecord.begin(), studentrecord.end());
	std::ofstream sorted;
	sorted.open("sorted.txt");
	for(int i; i<studentrecord.size(); ++i){

		sorted << studentrecord[i].score() << std::endl;
	}
	sorted.close();

}