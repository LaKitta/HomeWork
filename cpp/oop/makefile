usr: main.o user.o
	g++ main.o user.o -o usr

main.o: main.cpp
	g++ -c main.cpp -std=c++11

user.o: user.cpp
	g++ -c user.cpp -std=c++11

clean:
	rm user.o main.o math.exe