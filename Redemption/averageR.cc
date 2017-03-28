#include "StudentRecordPhysicsR.h"
#include "StudentRecordHistoryR.h"
#include "StudentRecordLiteratureR.h"
#include <iostream>
#include <fstream>

float calulate_average( std::vector<std::shared_ptr<StudentRecord> > const & records ) {
  float avg = 0.0;
  if ( records.size() == 0 ) {
    std::cout << "Error... none given" << std::endl;
    return avg;
  }
  for ( auto const & rec : records ) {
    avg += rec->score();
  }
  avg /= records.size();
  return avg; 
}

//sorting function based on shared pointers
bool lessthan( std::shared_ptr<StudentRecord> const &left, std::shared_ptr<StudentRecord> const & right) { return *left < *right;}

int main(int argc, char * argv[]){

//error check
  if ( argc < 2 ) {
    std::cout << "How to use for dummies, type: " << argv[0] << " filename.txt" << std::endl;
    return 0;
  }
  std::ifstream fin( argv[1] );


//create individual shared pointer vectors for each class, sort input based on class
  std::vector<std::shared_ptr<StudentRecord> > records, physics, literature, history;
  bool valid = true;
  while( valid ) {
    std::string line;
    std::getline( fin, line, ',');
    if ( line == "" ) 
      break;

    if ( line == "Physics" ) {
      std::shared_ptr<StudentRecord> irecord( new StudentRecordPhysics() );
      valid = irecord->input(fin);
      if ( valid ) {
	records.push_back( irecord );
	physics.push_back( irecord );
      }
      else
	break;
    } else if ( line == "Literature" ) {
      std::shared_ptr<StudentRecord> irecord( new StudentRecordLiterature() );
      valid = irecord->input(fin);
      if ( valid ) {
	records.push_back( irecord );
	literature.push_back( irecord );
      }
      else
	break;
    } else if ( line == "History" ) {
      std::shared_ptr<StudentRecord> irecord( new StudentRecordHistory() );
      valid = irecord->input(fin);
      if ( valid ) {
	records.push_back( irecord );
	history.push_back( irecord );
      }
      else
	break;
    } else {
      std::cout << "Invalid input, ignoring" << std::endl;
      continue;
    }

  }

  std::cout << "Initializing sorting hat..." << std::endl;

//sort the results, print 4 lists sorted by grade:

//sorted physics list
  std::cout << "\nPrinting sorted total grades, Physics, lowest -> highest..." << std::endl;
  std::sort( physics.begin(), physics.end(), lessthan );
  for ( std::shared_ptr<StudentRecord> const & phy : physics ) {
    phy->print(std::cout);
  }

//sorted history list
  std::cout << "\nPrinting sorted total grades, History, lowest -> highest..." << std::endl;
  std::sort( history.begin(), history.end(), lessthan );
  for ( std::shared_ptr<StudentRecord> const & his : history ) {
    his->print(std::cout);
  }

//sorted literature list
  std::cout << "\nPrinting sorted total grades, Literature, lowest -> highest..." << std::endl;
  std::sort( literature.begin(), literature.end(), lessthan );
  for ( std::shared_ptr<StudentRecord> const & lit : literature ) {
    lit->print(std::cout);
  }

//sorted total list
  std::sort( records.begin(), records.end(), lessthan );
  std::cout << "\nPrinting everyone's sorted total grades, lowest -> highest..." << std::endl;
  for ( std::shared_ptr<StudentRecord> const & rec : records ) {
    rec->print( std::cout );
  }

  std::cout << std::endl;

//print total average for each class
  std::cout << "Total average : " << calulate_average( records ) << std::endl;
  std::cout << "Physics average : " << calulate_average( physics ) << std::endl;
  std::cout << "Literature average : " << calulate_average( literature ) << std::endl;
  std::cout << "History average : " << calulate_average( history ) << std::endl;
}
