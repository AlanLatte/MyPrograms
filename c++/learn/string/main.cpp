#include <string>
#include <iostream>

string name;
std::cout << "Enter your name" << flush;
cin >> name;
getline(cin,name);

if (name = "")
{
	cout 	<< "Empty name"
				<< "assigning default\n";
	name = "John";
}
else
{
	std::cout << "Thank you, " << '\n'
	<< "for running"
	<< "this simple program!" << endl;
}
