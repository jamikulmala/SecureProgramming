#include <iostream>
#include <cstring>

int main()
{
    char example[8] = ""; // 8 bytes long string buffer

    strcpy(example, "override with this"); // the function overrides the buffer with value that is bigger than 8 bytes and causes vulnerability

    return 0;
}