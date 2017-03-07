//Create program that inputs a filename from command line containing list of students
//and computes a class average by passing a pointer to the vector to a function "calculate_average"
//Source code


#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "StudentRecord.h"

StudentRecord::StudentRecord( std::string lastname, std::string firstname, float score){

	lastname_ = lastname;
	firstname_ = firstname;
	score_ = score;

}
StudentRecord::~StudentRecord(){}
void StudentRecord::print() const {

	std::cout << firstname_ << " " << lastname_ << " got a score of: " << score_ << "." << std::endl;

};
std::string StudentRecord::firstname() {return firstname_;}
std::string StudentRecord::lastname() {return lastname_;}
float StudentRecord::score() const {return score_;}

//bool StudentRecord::operator<( StudentRecord const & right) const {
//
//	StudentRecord retval( score < right.score);
//}
//bool StudentRecord::operator>( StudentRecord const & right) const {
//
//	StudentRecord retval( score > right.score);
//}

/*bool input ( std::istream & in ) {   
    std::string line;   
    std::getline( in, line, ',');   
    firstname_ = line;   
    std::getline( in, line, ',');   
    lastname_ = line;   
    std::getline( in, line );   
    score_ = std::atof( line.c_str() );   
    if ( line == "")      
   		return false;   
    else     
    	return true; 
}
*/
