class Minstack:
    """Stack supporting constant-time retrieval of its minimum value."""

    def __init__(self):
        """Initialize the value stack and its matching minimum stack."""
        self.stack = []
        self.minstack = []
    
    def push(self, val):
        """Push ``val`` onto the stack."""
        self.stack.append(val)
        
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        
    def pop(self):
        """Remove the top value from the stack."""
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
    def top(self):
        """Return the top value without removing it."""
        return self.stack[-1]
    def getmin(self):
        """Return the smallest value currently in the stack."""
        return self.minstack[-1]