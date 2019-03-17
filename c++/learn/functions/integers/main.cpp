#include <iostream>
#include <cstdlib>

int sumOfNums(int x, int y){
  return x+y;
}

int main(int argc, char const *argv[]) {
  std::cout << sumOfNums(100, 10) << '\n';
  return 0;
}
