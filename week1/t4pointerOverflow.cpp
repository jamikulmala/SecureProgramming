#include <iostream>

#include <iostream>

int main() {
    const int size = 5;
    int* arr = new int[size];

    // Accessing beyond the bounds of allocated memory causes pointer overflow
    int* p = &arr[size];

    std::cout << "Value at p: " << *p << std::endl;

    return 0;

}