class TrieNode:
    """Represent one node in a character trie."""

    def __init__(self):
        """Initialize an empty node."""
        self.children = {}
        self.is_end = False
        
class Trie:
    """Store strings for exact and prefix lookups."""

    def __init__(self):
        """Initialize an empty trie."""
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert ``word`` into the trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
    
    def search(self, word):
        """Return whether ``word`` was inserted as a complete word."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix):
        """Return whether any inserted word starts with ``prefix``."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True