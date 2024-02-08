#include <iostream>
#include <string>

int main()
{
    char example[8] = ""; // 8 bytes long string buffer

    std::string example_word = "qwertyuiop"; // say we are trying to copy the first 8 letters of word to the buffer

    for(int i = 0; i <= 8; i++) {
        example[i] = example_word[i];
    }

    std::cout << example; // the for loop is executed 9 times wich causes off by one overflow when trying to access example[8]

    return 0;
}