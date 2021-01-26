#include <iostream>
#include <string>

class User
{
    std::string status = "Silver"; 
    static int usr_count;
    public:
        std::string f_name;
        std::string l_name;
        static void get_usr_count()
        {
            std::cout << usr_count << "\n";
            //return usr_count;
            //return 0;
        }
        void set_status(std::string status)
        {
            this->status = status;
        }
        void get_status()
        {
            std::cout << status << "\n";
            //return status;
        }
        //Constructor
        User()
        {
            std::cout << "Constructor\n";
            usr_count++;
        }
        User(std::string f_name, std::string l_name)
        {
            this->f_name = f_name;
            this->l_name = l_name; 
            std::cout << "COnstructor\n";
        }
        ~User()
        {
            std::cout << "Destructor\n";
            usr_count--;
        }
          
};

int User::usr_count = 0;

int main()
{
    /*
    User me;
    me.f_name = "ABC";
    me.f_name = "BCA";
    me.get_status();
    me.set_status("Poor");
    me.get_status();
    */
    //User me("ABC", "BCA");
    User u1, u2;
    User::get_usr_count();
    //std::cout << User::get_usr_count() << "\n";
    u1.~User();
    User::get_usr_count();
    //std::cout << User::get_usr_count() << "\n";
    return 0;
}