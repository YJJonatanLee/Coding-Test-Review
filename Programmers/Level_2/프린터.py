from collections import deque

def solution(priorities, location):
    
    printer = [i for i in range(0,len(priorities))]
    
    priorities_queue = deque(priorities)
    printer_queue = deque(printer)
    printer_stack = []

    while priorities_queue:
        
        imp_doc = max(priorities_queue)

        while priorities_queue[0] != imp_doc:
            priorities_queue.append(priorities_queue.popleft())
            printer_queue.append(printer_queue.popleft())

        priorities_queue.popleft()
        printer_stack.append(printer_queue.popleft())

    answer = printer_stack.index(location) + 1
    return answer
