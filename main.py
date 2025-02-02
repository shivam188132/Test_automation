from pynput.keyboard import Controller, Key
import time

# Initialize the controller
keyboard = Controller()

# Define the Python code with correct syntax and indentation
code = '''
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


'''

# Split the code into lines
code_lines = code.splitlines()

# Give yourself a few seconds to click on the window where you want to type the code
time.sleep(5)

# Function to type text accurately
def type_text(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.01)  # Adjust delay for faster typing

# Function to type the code line by line
def type_code():
    for line in code_lines:
        keyboard.press(Key.home)
        keyboard.release(Key.home)
        time.sleep(0.01)
        
        type_text(line)
        
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)

# Ensure no keys are left pressed
def cleanup():
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.alt)
    keyboard.release(Key.enter)

# Start typing the code
try:
    type_code()
finally:
    cleanup()  # Ensure cleanup happens even if an error occurs
