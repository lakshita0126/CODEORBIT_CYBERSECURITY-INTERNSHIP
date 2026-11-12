
print("======================================")
print("      CAESAR CIPHER ENCRYPTION TOOL")
print("======================================")

text = input("Enter the text: ")
shift = int(input("Enter the shift key: "))

encrypted = ""
decrypted = ""

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        encrypted += new_char

    elif ch >= 'a' and ch <= 'z':
        new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        encrypted += new_char

    else:
        encrypted += ch

for ch in encrypted:
    if ch >= 'A' and ch <= 'Z':
        new_char = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        decrypted += new_char

    elif ch >= 'a' and ch <= 'z':
        new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        decrypted += new_char

    else:
        decrypted += ch


print("\n========== RESULTS ==========")

print("Original Text  :", text)
print("Shift Key      :", shift)
print("Encrypted Text :", encrypted)
print("Decrypted Text :", decrypted)

print("=============================")
