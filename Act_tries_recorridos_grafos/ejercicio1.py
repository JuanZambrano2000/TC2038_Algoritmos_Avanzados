class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
trie = Trie()
with open("aliceWonderland.txt", "r", encoding='utf-8') as book:
    for line in book:
        for word in line.split():
            trie.insert(word)

search_words = ["Alice", "rabbit", "watch", "programacion", "tea", "queen", "king", "cat", 
                "Cheshire", "gryphon", "mock", "turtle", "hatter", "dormouse", "caterpillar", 
                "he", "ejemplo", "poison", "eat", "hola"]
start_with_words = ["Alice", "rab", "wat", "hol", "te", "que", "kin", "ca", "zwq", "gry",
                    "mock", "tur", "hat", "dor", "turtl", "hatt", "ejem", "poi", "ea", "hoqw"]

for word in search_words:
    print(f"Search of word: {word}: ", trie.search(word))

for wordSW in start_with_words:
    print(f"Starts with : {wordSW}", trie.starts_with(start_with_words))