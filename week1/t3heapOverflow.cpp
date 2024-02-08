#include <iostream>

int main()
{
    for(int i = 0; i < 1000000; i++){
        int* ptr = new int[8];
    }
    // dynamically allocates memory for an array of 8 integers a million times, but doesnt release the memory
    // which leads to potential heap overflow

    return 0;
}