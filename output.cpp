
#include <iostream>
#include <vector>
#include <string>

class TestClass {
public:
    TestClass(const std::string& name, int value) : name(name), value(value) {}

    void display() const {
        std::cout << "Name: " << name << ", Value: " << value << std::endl;
    }

    int multiply(int factor) const {
        return value * factor;
    }

private:
    std::string name;
    int value;
};

int main() {
    // Creating an object of TestClass
    TestClass obj("Sample", 42);

    // Displaying the object's properties
    obj.display();

    // Using a loop to perform some operations
    std::vector<int> results;
    for (int i = 1; i <= 5; ++i) {
        results.push_back(obj.multiply(i));
    }

    // Printing the results
    std::cout << "Results of multiplication:" << std::endl;
    for (int result : results) {
        std::cout << result << " ";
    }
    std::cout << std::endl;

    // Conditional statement to check a condition
    if (obj.multiply(2) > 50) {
        std::cout << "The product is greater than 50." << std::endl;
    } else {
        std::cout << "The product is 50 or less." << std::endl;
    }

    return 0;
}



  