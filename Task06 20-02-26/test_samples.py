"""
Simple test script to verify password_checker works with sample passwords
"""

from password_checker import (
    analyze_character_composition,
    calculate_strength_score,
    classify_password,
    calculate_search_space,
    calculate_character_set_size,
    calculate_entropy,
    estimate_crack_time,
    generate_feedback
)

# Test passwords from README
test_passwords = [
    ("abc", "Weak"),
    ("Password123", "Strong"),  # 65 points = Strong (60-79)
    ("MyP@ssw0rd!2024", "Very Strong"),  # 100 points = Very Strong (80+)
    ("12345678", "Weak"),
    ("Coffee&Tea@Morning!", "Very Strong"),  # 85 points = Very Strong
    ("", "Weak"),
    ("Pass123!", "Very Strong"),  # 90 points = Very Strong
    ("Password", "Moderate")  # 50 points = Moderate (40-59)
]

print("Testing Password Strength Checker with sample passwords...\n")

for password, expected_classification in test_passwords:
    print(f"Testing: '{password}' (Expected: {expected_classification})")
    
    # Perform analysis
    analysis = analyze_character_composition(password)
    score = calculate_strength_score(analysis)
    classification = classify_password(score)
    search_space = calculate_search_space(analysis)
    character_set_size = calculate_character_set_size(analysis)
    entropy = calculate_entropy(analysis['length'], character_set_size)
    crack_time = estimate_crack_time(search_space)
    feedback = generate_feedback(analysis, classification)
    
    # Verify classification
    if classification == expected_classification:
        print(f"  ✓ Classification: {classification}")
    else:
        print(f"  ✗ Classification: {classification} (Expected: {expected_classification})")
    
    print(f"  Score: {score}/100")
    print(f"  Length: {analysis['length']}")
    print(f"  Entropy: {entropy:.2f} bits")
    print(f"  Crack Time: {crack_time['human_readable']}")
    print()

print("All tests completed!")
