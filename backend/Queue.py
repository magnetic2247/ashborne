"""
MIT License

Copyright (c) 2022 Adrien Genevieve
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
"""Not that anyone will ever or ever would want to use this"""

# Queues
class Queue:
    # Constructor
    def __init__(self, max_len=float("inf")):
        self.file = []
        self.max_len = max_len
        
    # Append
    def push(self, v):
        if len(self.file) < self.max_len:
            self.file.append(v)
            return self
        else: raise OverflowError("Queue Full")
        
    # Remove
    def pop(self):
        if self.file == []: return
        return self.file.pop(0)
    
    # Top Element
    def top(self):
        if self.file == []: return None
        return self.file[0]
    
    # e m p t i n e s s
    def isempty(self):
        return self.file == []
    
    # print
    def __str__(self):
        return str(self.file)
    
    # length
    def __len__(self):
        return len(self.file)
    
    # compare
    def __eq__(self, v):
        if type(v)==File:
            return self.file == v.file
