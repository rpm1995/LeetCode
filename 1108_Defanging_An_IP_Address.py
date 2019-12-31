class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        new_string = ""
        
        for char in address:
            if char != ".":
                new_string += char
            else:
                new_string += "[.]"
        
        return new_string
