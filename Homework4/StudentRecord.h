//Class header for StudentRecord

#ifndef StudentRecord_h
#define StudentRecord_h

#include <iostream>
#include <sstream>

class StudentRecord {

	public:
		StudentRecord( std::string lastname = "", std::string firstname = "", float score = 0.);

		~StudentRecord();

		void print() const;
		std::string lastname();
		std::string firstname();
		float score() const;

		bool operator<( StudentRecord const & right) const {

			return(score() < right.score());
		}
		bool operator>( StudentRecord const & right) const {

			return(score() > right.score());
		}


	private:
		std::string lastname_;
		std::string firstname_;
		float score_;

};

#endif