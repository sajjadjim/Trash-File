#include <iostream>   
#include <string>

int main() {
    // Creating and initializing strings
    std::string str1 = "Hello";
    std::string str2 = "World";
    
    // Concatenation
    std::string str3 = str1 + " " + str2;
    std::cout << "Concatenated string: " << str3 << std::endl;

    // Accessing characters
    char firstChar = str1[0];
    std::cout << "First character of str1: " << firstChar << std::endl;

    // String length
    std::cout << "Length of str3: " << str3.length() << std::endl;

    // Substring
    std::string subStr = str3.substr(6, 5); // "World"
    std::cout << "Substring of str3: " << subStr << std::endl;

    // String comparison
    if (str1 == "Hello") {
        std::cout << "str1 is equal to 'Hello'" << std::endl;
    }

    // String search
    size_t pos = str3.find("World");
    if (pos != std::string::npos) {
        std::cout << "'World' found at position: " << pos << std::endl;
    }

    return 0;
}
