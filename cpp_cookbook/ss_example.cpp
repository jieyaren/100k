#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	stringstream ss;

	ss << "there are " << 9 << "apple in my cart";
	cout << ss.str() << endl;
	ss.str("");
	ss << showbase << hex << 16;
	cout << "ss = " << ss.str() << endl;
	ss.str("");
	ss << 3.14;
	cout << "ss = " << ss.str() << endl;
}
