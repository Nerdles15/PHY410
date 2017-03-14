#include "StudentRecordLiterature.h"

StudentRecordLiterature::StudentRecordLiterature(){};
StudentRecordLiterature::~StudentRecordLiterature() {};

void StudentRecordLiterature::print( std::ostream & out ) const  {
  out << "\nLiterature scores weighted: " << lastname_ << ", " << firstname_
      << ", analytic score: " << scores_[0] << ", creative score: " << scores_[1] <<  ", commentary score: " << scores_[2]
      << "\nOverall total: " << score() << std::endl;
}

bool StudentRecordLiterature::input( std::istream & in )  {
  double analytic = 0.0;
  double creative = 0.0;
  double commentary = 0.0;
  // First add name (last,first)
  std::string line;
  std::getline( in, line, ',');
  lastname_ = line;
  std::getline( in, line, ',');
  firstname_ = line;
  // Now get each score. Literature has three, with weights 0.4, 0.4, 0.2
  std::getline( in, line, ',' );
  analytic = std::atof(line.c_str())*0.4;
  std::getline( in, line, ',' );
  creative = std::atof(line.c_str())*0.4;
  std::getline( in, line );
  commentary = std::atof(line.c_str())*0.2;
  scores_.push_back(analytic);
  scores_.push_back(creative);
  scores_.push_back(commentary);
  if ( line == "") 
    return false;
  else {
    compute_score();
    return true;
  }
}
