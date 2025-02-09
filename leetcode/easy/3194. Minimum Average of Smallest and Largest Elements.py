class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        decrypted_dict = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        used_chars = set()
        index = 0

        for char in key:
            if char != ' ' and char not in used_chars:
                decrypted_dict[char] = alphabet[index]
                used_chars.add(char)
                index += 1
                if index == 26:
                    break
                
        return ''.join(decrypted_dict.get(char, ' ') for char in message)
