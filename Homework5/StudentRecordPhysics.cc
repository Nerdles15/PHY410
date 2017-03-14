#include "StudentRecordPhysics.h"

StudentRecordPhysics::StudentRecordPhysics(){};
StudentRecordPhysics::~StudentRecordPhysics() {};

void StudentRecordPhysics::print( std::ostream & out  ) const  {
  out << "\nPhysics scores weighted: " << lastname_ << ", " << firstname_
      << ", homework score: " << scores_[0] << ", lab score: " << scores_[1]
      << "\nOverall total: " << score() << std::endl;
}

bool StudentRecordPhysics::input( std::istream & in )  {
  double homework = 0.0;
  double lab = 0.0;
  // First add name (last,first)
  std::string line;
  std::getline( in, line, ',');
  lastname_ = line;
  std::getline( in, line, ',');
  firstname_ = line;
  // Now get each score. Physics has two
  std::getline( in, line, ',' );
  homework = std::atof(line.c_str())*0.8;
  std::getline( in, line );
  lab = std::atof(line.c_str())*0.2;
  scores_.push_back(homework);
  scores_.push_back(lab);
  if ( line == "") 
    return false;
  else {      
    compute_score();                     // Make sure to call compute_score in input!
    return true;
  }
}
