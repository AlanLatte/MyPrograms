#include <iostream>



int main ()
{
  int *a = new int(10);
  int *data = summary(*a);
  std::cout << *data << '\n';
}

int summary(int(*arg1)){
  return *arg1;
}
