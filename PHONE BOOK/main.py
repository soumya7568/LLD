class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold child nodes
        self.is_end = False  # Indicates if this node represents the end of a contact name
        self.contact_info = []  # List to hold contact information for this node

class Phonebook:
    def __init__(self):
        self.root = TrieNode()  # Root node of the Trie

    def add_contact(self, name: str, number: str) -> None:
        """Adds a contact to the phonebook."""
        current_node = self.root
        for char in name:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()  # Create new node if char not found
            current_node = current_node.children[char]
        current_node.is_end = True  # Mark the end of the contact name
        current_node.contact_info.append((name, number))  # Store the contact information

    def search_contact(self, prefix: str) -> list:
        """Returns all contacts starting with the given prefix."""
        current_node = self._find_node(prefix)
        if current_node is None:
            return []  # No contacts found with the prefix
        return self._get_all_contacts(current_node)

    def _find_node(self, prefix: str) -> TrieNode:
        """Finds the node corresponding to the end of the prefix."""
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None  # Prefix not found
            current_node = current_node.children[char]
        return current_node  # Node corresponding to the end of the prefix

    def _get_all_contacts(self, node: TrieNode) -> list:
        """Recursively retrieves all contact names and numbers from the given node."""
        contacts = []
        if node.is_end:
            contacts.extend(node.contact_info)  # Add the contact information if it's a valid contact

        for child_node in node.children.values():
            contacts.extend(self._get_all_contacts(child_node))  # Explore children nodes

        return contacts

# Example Usage
if __name__ == "__main__":
    phonebook = Phonebook()
    phonebook.add_contact("Alice", "123-456-7890")
    phonebook.add_contact("Alfred", "234-567-8901")
    phonebook.add_contact("Bob", "345-678-9012")
    phonebook.add_contact("Charlie", "456-789-0123")
    
    print("Contacts starting with 'Al':", phonebook.search_contact("Al"))
    print("Contacts starting with 'B':", phonebook.search_contact("B"))
    print("Contacts starting with 'Ch':", phonebook.search_contact("Ch"))
