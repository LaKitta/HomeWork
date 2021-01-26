#ifndef USER_H
#define USER_H
#include <iostream>
#include <string>
#include <vector>

class User
{
    std::string status = "Silver"; 
    static int usr_count;
    public:
        std::string f_name = "default";
        std::string l_name = "default";
        static void get_usr_count();
        void set_status(std::string status);
        void get_status();
        //Constructor
        User();
        User(std::string f_name, std::string l_name);
        ~User();  
        virtual void output();        
};

class Teacher : public User
{
    public:
        std::vector<std::string> lessons = {"A", "B", "C"};
        void output_lessons();
        void output();
};
#endif