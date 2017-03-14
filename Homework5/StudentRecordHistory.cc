#include "StudentRecordHistory.h"

StudentRecordHistory::StudentRecordHistory(){};
StudentRecordHistory::~StudentRecordHistory() {};

void StudentRecordHistory::print( std::ostream & out ) const  {
  out << "\nHistory scores weighted: " << lastname_ << ", " << firstname_
      << ", exam 1: " << scores_[0] << ", exam 2: " << scores_[1]
      << "\nOverall total: " << score() << std::endl;
}

bool StudentRecordHistory::input( std::istream & in )  {
  double exam1 = 0.0;
  double exam2 = 0.0;
  // First add name (last,first)
  std::string line;
  std::getline( in, line, ',');
  lastname_ = line;
  std::getline( in, line, ',');
  firstname_ = line;
  // Now get each score. History has two, higher weighted .6, lower .4
  std::getline( in, line, ',' );
  exam1 = std::atof(line.c_str());
  std::getline( in, line );
  exam2 = std::atof(line.c_str());

  //weigh exam scores appropriately
  if(exam1 >= exam2) {

    exam1 = 0.6*exam1;
    exam2 = 0.4*exam2;
  } else {

    exam1 = 0.4*exam1;
    exam2 = 0.6*exam2;
  }

  scores_.push_back(exam1);
  scores_.push_back(exam2);

  if ( line == "") 
    return false;
  else {
    compute_score();
    return true;
  }
}
