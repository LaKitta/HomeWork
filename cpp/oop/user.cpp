#include "user.h"

int User::usr_count = 0;

void User::get_usr_count()
{
    std::cout << usr_count << "\n";
    //return usr_count;
    //return 0;
}
void User::set_status(std::string status)
{
    this->status = status;
}
void User::get_status()
{
    std::cout << status << "\n";
    //return status;
}
//Constructor
User::User()
{
    std::cout << "Constructor\n";
    usr_count++;
}
User::User(std::string f_name, std::string l_name)
{
    this->f_name = f_name;
    this->l_name = l_name; 
    std::cout << "COnstructor\n";
}
User::~User()
{
    std::cout << "Destructor\n";
    usr_count--;
}

void Teacher::output_lessons()
{
    for(std::string lesson : lessons)
    {
        std::cout << lesson << "\t";
    }
    std::cout << "\n";
}

void User::output()
{
    std::cout << "User\n";
}

void Teacher::output()
{
    std::cout << "Teacher\n";
}