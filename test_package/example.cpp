#include <iostream>
#include "fmt/format.h"

int main() {
    std::string message = fmt::format("The answer is {}", 42);
    std::cout<<message<<"\n";
}
