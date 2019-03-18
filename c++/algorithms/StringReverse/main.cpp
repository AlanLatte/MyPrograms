#include <iostream>
#include <string>
std::string stringReverse(std::string mystr) {
	int lenString = mystr.length();
	std::string newString;
	for (int i = lenString; i >= 0; i--) {
		newString.push_back(mystr[i]);
	}
	return newString;
}


int main(int argc, char const *argv[]) {
	std::string mystr;
	std::cin >> mystr;
	std::cout << stringReverse(mystr) << '\n';
	return 0;
}
