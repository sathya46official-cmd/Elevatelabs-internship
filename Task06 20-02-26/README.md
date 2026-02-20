# 🔐 Task 6 – Password Strength Analysis Using Python

## 🎯 Objective

To create multiple passwords with varying complexity levels and evaluate their security using a custom-built Python Password Strength Checker.

The goal of this task is to understand how password length, character diversity, entropy, and brute-force resistance impact overall password security.

---

## 🛠 Tools Used

- Python 3
- Kali Linux
- Git & GitHub

---

## 📁 Project Structure

```
Task6_2026-02-20/
│
├── password_checker.py   # Main password strength evaluation program
├── test_samples.py       # Script to test multiple passwords automatically
├── results.txt           # Output report from test execution
└── README.md             # Project documentation
```

---

## 🔎 Project Overview

This project consists of two main components:

### 1️⃣ Password Strength Checker (`password_checker.py`)

The program evaluates a password based on:

- Length of password
- Presence of:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&* etc.)
- Entropy calculation (randomness measurement)
- Search space calculation
- Estimated brute-force crack time

The tool generates:

- Strength Score (0–100)
- Classification (Weak / Moderate / Strong)
- Entropy (in bits)
- Estimated Crack Time
- Security Feedback

---

### 2️⃣ Automated Testing Script (`test_samples.py`)

This script:

- Creates multiple passwords with varying complexity
- Tests each password using the password checker
- Displays:
  - Score
  - Classification
  - Entropy
  - Crack time
- Verifies expected classifications

The output is saved as:

```
results.txt
```

---

## 🧪 Sample Passwords Tested

| Password | Expected Complexity |
|----------|--------------------|
| abc | Weak |
| 12345678 | Weak |
| Password | Moderate |
| Password123 | Strong |
| Pass123! | Very Strong |
| MyP@ssw0rd!2024 | Very Strong |
| Coffee&Tea@Morning! | Very Strong |
| (empty string) | Weak |

---

## 📊 Observations

- Short passwords with only letters or digits had very low entropy.
- Passwords with mixed character types significantly increased score.
- Special characters increased search space.
- Longer passphrases showed extremely high entropy and crack resistance.
- Entropy increases exponentially with length.

---

## 🔐 Key Security Concepts Learned

### ✔ Password Strength
Depends on length, character variety, and randomness.

### ✔ Brute Force Attack
An attacker tries all possible combinations until the correct password is found.

### ✔ Dictionary Attack
Uses common passwords and leaked wordlists instead of all combinations.

### ✔ Entropy
Measured in bits. Higher entropy means more randomness and stronger security.

### ✔ Search Space
Total possible password combinations based on character set and length.

### ✔ Crack Time Estimation
Estimated time required for an attacker attempting 1 billion guesses per second.

---

## 📌 Conclusion

- Length plays a more important role than complexity alone.
- Passwords with mixed character types are stronger.
- Long passphrases provide superior security.
- Weak passwords can be cracked instantly using modern hardware.
- Strong passwords drastically increase brute-force attack time.

---

## 🎓 Learning Outcome

- Implemented a password strength evaluation system in Python.
- Understood entropy and search space mathematically.
- Analyzed password resistance to brute-force attacks.
- Compared weak and strong passwords using real metrics.
- Gained practical understanding of authentication security.

---

⚠️ Note: This is an educational project. Do not test real passwords in public tools.
