#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

using std::cin;
using std::cout;

void start_game();
void print_vector(std::vector<int>);

int main()
{
    int choose;
    srand(time(NULL));

    while (true)
    {
        cout << "Please choose\n0.Quit\n1.Start\n";
        cin >> choose;

        switch (choose)
        {
        case 0:
            return 0;
        case 1:
            start_game();
            break;
        }
    }
}

void start_game()
{
    int random = rand() % 101; // random number within [0 - 100]
    cout << random << std::endl;

    cout << "Guess" << std::endl;

    int guess;
    std::vector<int> guesses;

    do
    {
        cin >> guess;
        guesses.push_back(guess);

        if (guess > random)
        {
            cout << "Too high\n";
        }
        else if (guess < random)
        {
            cout << "too low\n";
        }
        else
        {
            break;
        }

    } while (true);

    print_vector(guesses);
}

void print_vector(std::vector<int> vector)
{
    for (int i = 0; i < vector.size(); i++)
    {
        cout << vector[i] << "\t";
    }
    cout << "\n";
}