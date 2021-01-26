#include <iostream>

class Position
{
    public:
        int x = 10, y = 10;
        //Operator overloading
        //std::ostream& operator << (std::ostream& output, Position pos){}
        //std::istream& operator >. (std::istream& input, Position &pos){}
        Position operator + (Position pos)
        {
            Position new_pos;
            new_pos.x = x + pos.x;
            new_pos.y = y + pos.y;
            return new_pos;
        }
        void get_pos()
        {
            std::cout << "Corx =" << x << " Cory = " << y << "\n"; 
        }

};

int main()
{
    Position pos1, pos2;
    Position pos3 = pos1 + pos2;
    pos3.get_pos();

    return 0;
}