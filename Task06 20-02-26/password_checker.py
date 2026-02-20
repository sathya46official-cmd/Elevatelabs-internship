"""
Password Strength Checker
A Python-based educational tool that evaluates password security based on
industry-standard security concepts including length, character variety,
entropy, and brute-force resistance.

Author: Cybersecurity Student
Purpose: Internship Task - Authentication Security Demonstration
"""

import math

# ============================================================================
# CONSTANTS
# ============================================================================

# Character set definitions
SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Character set sizes for search space calculation
LOWERCASE_SIZE = 26
UPPERCASE_SIZE = 26
DIGITS_SIZE = 10
SPECIAL_SIZE = 32

# Attack rate assumption for brute-force calculations
ATTACK_RATE = 1_000_000_000  # 1 billion attempts per second

# Score thresholds for password classification
WEAK_THRESHOLD = 40
MODERATE_THRESHOLD = 60
STRONG_THRESHOLD = 80

# Length thresholds for scoring
MIN_LENGTH_BASIC = 6
MIN_LENGTH_GOOD = 8
MIN_LENGTH_EXCELLENT = 12

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

def analyze_character_composition(password: str) -> dict:
    """
    Analyzes the types of characters present in the password.
    
    Args:
        password: The password string to analyze
        
    Returns:
        Dictionary containing:
        - length: Password length
        - has_uppercase: True if contains A-Z
        - has_lowercase: True if contains a-z
        - has_digits: True if contains 0-9
        - has_special: True if contains special characters
        - character_types_count: Number of character types present (0-4)
    """
    # Initialize analysis results
    has_uppercase = False
    has_lowercase = False
    has_digits = False
    has_special = False
    
    # Check each character in the password
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digits = True
        elif char in SPECIAL_CHARACTERS:
            has_special = True
    
    # Count how many character types are present
    character_types_count = sum([
        has_uppercase,
        has_lowercase,
        has_digits,
        has_special
    ])
    
    return {
        'length': len(password),
        'has_uppercase': has_uppercase,
        'has_lowercase': has_lowercase,
        'has_digits': has_digits,
        'has_special': has_special,
        'character_types_count': character_types_count
    }


def calculate_strength_score(analysis: dict) -> int:
    """
    Calculates a numerical strength score based on password characteristics.
    
    Args:
        analysis: Dictionary from analyze_character_composition()
        
    Returns:
        Integer score between 0 and 100
        
    Scoring breakdown:
        - Length >= 12: +30 points
        - Length >= 8: +20 points
        - Length >= 6: +10 points
        - Has uppercase: +15 points
        - Has lowercase: +15 points
        - Has digits: +15 points
        - Has special characters: +25 points
    """
    score = 0
    
    # Award points based on length
    length = analysis['length']
    if length >= MIN_LENGTH_EXCELLENT:
        score += 30
    elif length >= MIN_LENGTH_GOOD:
        score += 20
    elif length >= MIN_LENGTH_BASIC:
        score += 10
    
    # Award points for character type diversity
    if analysis['has_uppercase']:
        score += 15
    if analysis['has_lowercase']:
        score += 15
    if analysis['has_digits']:
        score += 15
    if analysis['has_special']:
        score += 25
    
    # Ensure score stays within valid range
    return min(max(score, 0), 100)


def classify_password(score: int) -> str:
    """
    Classifies password into strength categories based on score.
    
    Args:
        score: Integer score from calculate_strength_score()
        
    Returns:
        String classification: "Weak", "Moderate", "Strong", or "Very Strong"
    """
    if score < WEAK_THRESHOLD:
        return "Weak"
    elif score < MODERATE_THRESHOLD:
        return "Moderate"
    elif score < STRONG_THRESHOLD:
        return "Strong"
    else:
        return "Very Strong"



def calculate_character_set_size(analysis: dict) -> int:
    """
    Calculates the total character set size based on character types present.
    
    Args:
        analysis: Dictionary from analyze_character_composition()
        
    Returns:
        Integer representing total character set size
    """
    character_set_size = 0
    
    if analysis['has_lowercase']:
        character_set_size += LOWERCASE_SIZE
    if analysis['has_uppercase']:
        character_set_size += UPPERCASE_SIZE
    if analysis['has_digits']:
        character_set_size += DIGITS_SIZE
    if analysis['has_special']:
        character_set_size += SPECIAL_SIZE
    
    # Return at least 1 to avoid division by zero
    return max(character_set_size, 1)


def calculate_search_space(analysis: dict) -> int:
    """
    Calculates the total number of possible password combinations.
    
    Args:
        analysis: Dictionary from analyze_character_composition()
        
    Returns:
        Integer representing search space size
    """
    character_set_size = calculate_character_set_size(analysis)
    length = analysis['length']
    
    # Handle edge case of zero-length password
    if length == 0:
        return 0
    
    # Calculate search space: character_set_size ^ length
    return character_set_size ** length


def calculate_entropy(length: int, character_set_size: int) -> float:
    """
    Calculates password entropy in bits using the log2 formula.
    
    Args:
        length: Password length
        character_set_size: Size of character set used
        
    Returns:
        Float representing entropy in bits
        
    Formula: entropy = length × log2(character_set_size)
    """
    # Handle edge cases
    if length == 0 or character_set_size <= 1:
        return 0.0
    
    # Calculate entropy using log2
    entropy = length * math.log2(character_set_size)
    return entropy


def estimate_crack_time(search_space: int) -> dict:
    """
    Estimates time required for brute-force attack.
    
    Args:
        search_space: Total number of possible combinations
        
    Returns:
        Dictionary containing:
        - seconds: Raw time in seconds
        - human_readable: Formatted string with appropriate time unit
    """
    # Calculate crack time in seconds
    crack_time_seconds = search_space / ATTACK_RATE
    
    # Convert to human-readable format
    if crack_time_seconds < 60:
        human_readable = f"{crack_time_seconds:.2f} seconds"
    elif crack_time_seconds < 3600:
        minutes = crack_time_seconds / 60
        human_readable = f"{minutes:.2f} minutes"
    elif crack_time_seconds < 86400:
        hours = crack_time_seconds / 3600
        human_readable = f"{hours:.2f} hours"
    elif crack_time_seconds < 31536000:
        days = crack_time_seconds / 86400
        human_readable = f"{days:.2f} days"
    elif crack_time_seconds < 31536000000:  # Less than 1000 years
        years = crack_time_seconds / 31536000
        human_readable = f"{years:.2f} years"
    else:
        # For very large numbers, use scientific notation
        years = crack_time_seconds / 31536000
        human_readable = f"{years:.2e} years"
    
    return {
        'seconds': crack_time_seconds,
        'human_readable': human_readable
    }



def generate_feedback(analysis: dict, classification: str) -> list:
    """
    Generates actionable feedback for the user based on password analysis.
    
    Args:
        analysis: Dictionary from analyze_character_composition()
        classification: String classification from classify_password()
        
    Returns:
        List of feedback strings
    """
    feedback = []
    
    # Check for short password
    if analysis['length'] < MIN_LENGTH_GOOD:
        feedback.append(f"Password is too short. Use at least {MIN_LENGTH_GOOD} characters ({MIN_LENGTH_EXCELLENT}+ recommended).")
    
    # Check for missing character types
    if not analysis['has_uppercase']:
        feedback.append("Add uppercase letters (A-Z) for better security.")
    
    if not analysis['has_lowercase']:
        feedback.append("Add lowercase letters (a-z) for better security.")
    
    if not analysis['has_digits']:
        feedback.append("Add numbers (0-9) to increase complexity.")
    
    if not analysis['has_special']:
        feedback.append("Add special characters (!@#$%^&*) for maximum security.")
    
    # Add classification-specific feedback
    if classification == "Very Strong":
        feedback.append("Outstanding! This password has excellent security characteristics.")
    elif classification == "Strong":
        feedback.append("Great! This password has strong security characteristics.")
    elif classification == "Moderate":
        feedback.append("This password is moderate. Consider the suggestions above.")
    else:
        feedback.append("This password is weak. Please strengthen it using the suggestions above.")
    
    return feedback



def get_password_input() -> str:
    """
    Handles user input for password entry.
    
    Returns:
        The password string entered by the user (without modification)
    """
    print("\nEnter a password to check its strength:")
    password = input("> ")
    return password


def display_results(password: str, analysis: dict, score: int, 
                   classification: str, search_space: int, 
                   entropy: float, crack_time: dict, feedback: list) -> None:
    """
    Formats and displays all password analysis results to the user.
    
    Args:
        password: The original password (will be masked in display)
        analysis: Dictionary from analyze_character_composition()
        score: Integer score from calculate_strength_score()
        classification: String from classify_password()
        search_space: Integer from calculate_search_space()
        entropy: Float from calculate_entropy()
        crack_time: Dictionary from estimate_crack_time()
        feedback: List of strings from generate_feedback()
    """
    # Calculate character set size for display
    character_set_size = calculate_character_set_size(analysis)
    
    # Display header
    print("\n" + "=" * 60)
    print("PASSWORD STRENGTH ANALYSIS")
    print("=" * 60)
    
    # Display password info (masked for security)
    print(f"\nPassword: {'*' * len(password)}")
    print(f"Length: {analysis['length']} characters")
    
    # Display character composition
    print("\nCharacter Composition:")
    print(f"  {'✓' if analysis['has_uppercase'] else '✗'} Uppercase letters (A-Z)")
    print(f"  {'✓' if analysis['has_lowercase'] else '✗'} Lowercase letters (a-z)")
    print(f"  {'✓' if analysis['has_digits'] else '✗'} Digits (0-9)")
    print(f"  {'✓' if analysis['has_special'] else '✗'} Special characters (!@#$%^&*...)")
    
    # Display strength score and classification
    print(f"\nStrength Score: {score}/100")
    print(f"Classification: {classification}")
    
    # Display security metrics
    print("\nSecurity Metrics:")
    print(f"  - Character Set Size: {character_set_size}")
    print(f"  - Search Space: {search_space:,}")
    print(f"  - Entropy: {entropy:.2f} bits")
    print(f"  - Estimated Crack Time (brute-force): {crack_time['human_readable']}")
    
    # Display feedback
    print("\nFeedback:")
    for item in feedback:
        print(f"  • {item}")
    
    print("\n" + "=" * 60)



def main() -> None:
    """
    Main program flow - orchestrates the entire password checking process.
    Allows users to check multiple passwords in a loop.
    """
    # Display welcome message
    print("=" * 60)
    print("WELCOME TO PASSWORD STRENGTH CHECKER")
    print("=" * 60)
    print("\nThis tool evaluates password security based on:")
    print("  • Length")
    print("  • Character variety (uppercase, lowercase, digits, special)")
    print("  • Entropy (information-theoretic security)")
    print("  • Brute-force attack resistance")
    print("\nNote: This is an educational tool. Never enter real passwords!")
    
    # Main loop for checking multiple passwords
    while True:
        # Get password input
        password = get_password_input()
        
        # Perform analysis
        analysis = analyze_character_composition(password)
        score = calculate_strength_score(analysis)
        classification = classify_password(score)
        search_space = calculate_search_space(analysis)
        character_set_size = calculate_character_set_size(analysis)
        entropy = calculate_entropy(analysis['length'], character_set_size)
        crack_time = estimate_crack_time(search_space)
        feedback = generate_feedback(analysis, classification)
        
        # Display results
        display_results(password, analysis, score, classification, 
                       search_space, entropy, crack_time, feedback)
        
        # Ask if user wants to check another password
        print("\nWould you like to check another password? (yes/no)")
        choice = input("> ").strip().lower()
        
        if choice not in ['yes', 'y']:
            print("\nThank you for using Password Strength Checker!")
            print("Remember: Use strong, unique passwords for each account!")
            break



# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
