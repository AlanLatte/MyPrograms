#include <iostream>
/*
						TASK:
						1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/

int logic(int range){
	int sum=0;
	for (size_t i = 0; i < range; i++) {
		if (i%3==0){
			sum+=i;
		}else if (i%5==0){
			sum+=i;
		}
	}
	return sum;
}

int main(int argc, char const *argv[]) {
	int range=1000;
	std::cout << logic(range) << '\n';
}
