#include <iostream>
#include "stack.hpp"

using namespace std;

int main() {
    Stack stack;

    stack.push(1);
    stack.push(2);
    stack.push(8);
    stack.push(7);
    stack.push(5);
    
    stack.pop(); 
    stack.pop(); 

    cout << stack.isEmpty() << endl;
    cout << stack.peek() << endl;
}
