#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <memory>
#include <vector>
#include "StudentRecord.h"
#include "StudentRecordPhysics.h"
#include "StudentRecordLiterature.h"
#include "StudentRecordHistory.h"



//call main function
int main(int argc, char * argv[]) {
  std::ifstream file(argv[1]);
  std::vector<std::shared_ptr<StudentRecord>> physcores, litscores, hisscores, records;

  //define class averages
  double pavg = 0.0;
  double lavg = 0.0;
  double havg = 0.0;

  while(!file.eof()) {

    std::string line;
    std::getline(file, line, '\n');
    if (line == "") {

      break;
    } else{

      std::stringstream buf(line);
      std::string token;
      std::getline(buf, token, ',');
      std::string student;
      std::getline(buf, student, '\n');
      std::stringstream records(student);

      if(token == "Physics") {

        std::shared_ptr<StudentRecord> phystudent (new StudentRecordPhysics);
        phystudent -> input(records);
        phystudent -> print();
        physcores.push_back(phystudent);
        pavg += phystudent -> score();

      } else if(token == "Literature") {

        std::shared_ptr<StudentRecord> litstudent (new StudentRecordLiterature);
        litstudent -> input(records);
        litstudent -> print();
        litscores.push_back(litstudent);
        lavg += litstudent -> score();

      } else if(token == "History") {

        std::shared_ptr<StudentRecord> hisstudent (new StudentRecordHistory);
        hisstudent -> input(records);
        hisstudent -> print();
        hisscores.push_back(hisstudent);
        havg += hisstudent -> score();

      } else {

        std::cout << "Can't understand record, please try again." << std::endl;
        break;
      }
    }
  }


  
  std::cout << "\nClass Physics average: " << pavg/physcores.size() << "." << std::endl;
  std::cout << "\nClass Literature average: " << lavg/litscores.size() << "." << std::endl;
  std::cout << "\nClass History average: " << havg/hisscores.size() << "." << std::endl;

  return 0; 
}
