#include <iostream>
#include <string>

struct User
{
    std::string f_name;
    std::string l_name;
    void set_status(std::string status)
    {
        this->status = status;
    }
    void get_status()
    {
        std::cout << status << "\n";
        //return status;
    }
    private:
        std::string status = "Silver"; 
};

int main()
{
    User me;
    me.f_name = "ABC";
    me.f_name = "BCA";
    me.get_status();
    me.set_status("Poor");
    me.get_status();
    return 0;
}