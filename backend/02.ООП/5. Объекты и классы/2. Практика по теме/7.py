class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        if is_encrypt:
            original_text = text.lower()
            cipher_text = []
            for char in original_text:
                if char in self.alphabet:
                    index = self.alphabet.index(char)
                    new_index = (index + shift) % len(self.alphabet)
                    cipher_text.append(self.alphabet[new_index])
                else:
                    cipher_text.append(char)
            return ''.join(cipher_text)
        else:
            cipher_text = text.lower()
            original_text = []
            for char in cipher_text:
                if char in self.alphabet:
                    index = self.alphabet.index(char)
                    new_index = (index - shift) % len(self.alphabet)
                    original_text.append(self.alphabet[new_index])
                else:
                    original_text.append(char)
            return ''.join(original_text)

# Пример использования
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 
