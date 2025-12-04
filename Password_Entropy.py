import math

def calculate_entropy(password):
    """
    Calculates the password entropy in bits using a common character set approach.
    R (Character Set Size) is approximated based on the types of characters found.
    
    R = 26 (lowercase) + 26 (uppercase) + 10 (digits) + 33 (symbols) = 95 max
    """
    
    # Initialize the size of the character set (R)
    R = 0
    
    # Define character groups for checking
    # Note: R is an *approximation*. If a group is present, we add its total size.
    
    # 1. Lowercase letters (a-z) - 26 characters
    if any(c.islower() for c in password):
        R += 26
        
    # 2. Uppercase letters (A-Z) - 26 characters
    if any(c.isupper() for c in password):
        R += 26
        
    # 3. Digits (0-9) - 10 characters
    if any(c.isdigit() for c in password):
        R += 10
        
    # 4. Symbols/Punctuation (e.g., !@#$%^&*...) - approx. 33 characters
    # We check for any character that is not letter or digit.
    if any(not c.isalnum() for c in password):
        R += 33
        
    # L is the length of the password
    L = len(password)
    
    # Calculate Entropy (E = L * log2(R))
    if R == 0:
        return 0 # Handle empty or non-standard passwords
    
    entropy = L * math.log2(R)
    
    # Return the entropy and the calculated character set size (R)
    return entropy, R

# --- Main Execution ---
if __name__ == "__main__":
    test_password = input("Enter the password to check entropy: ")
    
    entropy, charset_size = calculate_entropy(test_password)
    
    print("\n--- Entropy Results ---")
    print(f"Password Length (L): {len(test_password)}")
    print(f"Character Set Size (R): {charset_size}")
    print(f"Entropy (bits): {entropy:.2f}") # Displaying to two decimal places
    
    # Interpretation for the user
    if entropy >= 100:
        strength = "Very Strong"
    elif entropy >= 80:
        strength = "Strong"
    elif entropy >= 60:
        strength = "Moderate"
    else:
        strength = "Weak"
        
    print(f"Estimated Password Strength: {strength}")