/*
			Task:
			3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
#include <iostream>
///////////////////////////////////////////////////////////////////////////////
void    print_prime_factors( int    n )
{
    for ( int i = 2; i*i <= n; ++i )
    {
        if  (
                n % i   ==  0
            )
        {
            std::cout   << i
                        << ' ';

            while( n % i    ==  0 )
            {
                n   /=  i;
            }
        }//if
    }

    if( n != 1 )
    {
        std::cout   <<  n;
    }

    std::cout   <<  std::endl
                <<  "finish"
                <<  std::endl
                <<  std::endl;
}
///////////////////////////////////////////////////////////////////////////////
int     main()
{
    for(;;)
    {
        int     n{};
        std::cout   <<  "n = ";
        std::cin    >>  n;

        print_prime_factors(n);
    }//for
}
