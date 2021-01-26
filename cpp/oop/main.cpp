#include "user.h"

int main()
{
    /*
    User me;
    me.f_name = "ABC";
    me.f_name = "BCA";
    me.get_status();
    me.set_status("Poor");
    me.get_status();
    //User me("ABC", "BCA");
    User u1, u2;
    User::get_usr_count();
    //std::cout << User::get_usr_count() << "\n";
    u1.~User();
    User::get_usr_count();
    //std::cout << User::get_usr_count() << "\n";
    */
    Teacher teacher1;
    //teacher1.output_lessons();
    //teacher1.get_status(); 
    User& usr1 = teacher1;
    usr1.output();
    return 0;
}