from stack_and_queue.stack import Stack


def validate_brackets(str):
    brackets_type = {"{": "}", "[": "]", "(": ")"}
    open_brackets = ["{", '[', '(']
    closed_brackets = ["}", ']', ')']
    open_stack = Stack()


    for a in str:
        if a in open_brackets:
            open_stack.push(a)
        if a in closed_brackets:
                if open_stack.is_empty():
                     return False
                
                last_open_stack=open_stack.pop()
                if (brackets_type[last_open_stack] !=a ):
                     return False


    if open_stack.is_empty():
         return True


    return False            
