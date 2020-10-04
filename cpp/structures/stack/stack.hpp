#include <iostream>

using namespace std;

class Stack {
    private:
        int top;
        int stack[];

    public:
        Stack() {
            top = -1;
        }

        bool isEmpty() {
            return top == -1;
        }

        void push(int e) {
            top++;
            stack[top] = e;
        }

        void pop() {
            if(isEmpty()){
                cout << "This stack is empty" << endl;
                return;
            }

            stack[top] = 0; 
            top--;
        }

        int peek() {
            if (isEmpty()) {
                cout << "This stack is empty" << endl;
                return 0;
            }

            return stack[top];
        }
};

