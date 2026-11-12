
print("===================================")
print("     PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_+=<>?/"

# Check each character
for ch in password:

    if ch >= 'A' and ch <= 'Z':
        has_upper = True

    elif ch >= 'a' and ch <= 'z':
        has_lower = True

    elif ch >= '0' and ch <= '9':
        has_digit = True

    elif ch in special_chars:
        has_special = True

# Calculate score
score = 0

if length >= 8:
    score += 1

if length >= 12:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

# Display results
print("\n----- PASSWORD ANALYSIS -----")

print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Numbers:", has_digit)
print("Special Characters:", has_special)

print("\nPassword Strength:")

if score <= 2:
    print("VERY WEAK")

elif score <= 3:
    print("WEAK")

elif score <= 4:
    print("MODERATE")

elif score <= 5:
    print("STRONG")

else:
    print("VERY STRONG")

print("Score:", score, "/ 6")
print("-----------------------------")
