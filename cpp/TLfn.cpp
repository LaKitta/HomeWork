#include <string>
#include <iostream>

//templatized function
template <typename T>
void swap(T &a, T &b)
{
    T tmp = a;
    a = b;
    b = tmp;
}

//overloading
template <typename T>
void swap(T a[], T b[], int size)
{
    
}
int main()
{
    int a = 10, b = 20;
    swap(a, b);

    std::string s_a = "ABC", s_b = "CBA";
    swap(s_a, s_b);

    std::cout << a << " " << b << "\n";
    std::cout << s_a << " " << s_b << "\n";

    return 0;

}