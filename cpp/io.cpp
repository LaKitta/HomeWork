#include <iostream>
#include <fstream>
#include <vector>

int main()
{
    std::ifstream file ("text.txt");
    //std::ofstream file ("text.txt", std::ios::app);

    std::vector<std::string> names;
    //names.push_back("ABC");
    //names.push_back("BCA");
    //names.push_back("CBA");

    std::string input;


    //read from file method 1
    /*
    while(file >> input)
    {
        names.push_back(input);
    }
    */
    //file.get(); getline(file, string);

    for(std::string name : names)
    {

        std::cout << name << "\n";

    }

    file.close();



    return 0;


}