class FlattenIterator:
    def __init__(self, nested_list):
        self.nested_list = nested_list
    
    def __iter__(self):
        self.stack = [iter(self.nested_list)]
        return self
    
    def __next__(self):
        while self.stack:
            current_iter = self.stack[-1]
            try:
                element = next(current_iter)
                if isinstance(element, list):
                    self.stack.append(iter(element))
                else:
                    return element
            except StopIteration:
                self.stack.pop()
        
        raise StopIteration

nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
    

for num in flat:
    print(num)