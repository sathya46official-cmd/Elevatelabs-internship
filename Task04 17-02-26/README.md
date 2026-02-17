# 🔥 Task 4 - Firewall Configuration using UFW

## 🎯 Objective
Configure and test firewall rules using UFW on Kali Linux.

## 🛠 Tools Used
- Kali Linux
- UFW (Uncomplicated Firewall)
- OpenSSH Server

## 🔧 Configuration Steps
1. Installed UFW
2. Enabled firewall
3. Set default policies:
   - Deny incoming
   - Allow outgoing
4. Installed and started SSH service
5. Allowed port 22 for SSH

## 🧪 Testing Phase

### Test 1: SSH Allowed
Successfully connected from Windows host to Kali VM.

### Test 2: SSH Blocked
Removed rule for port 22.
Connection attempt failed as expected.

## 📌 Result
Firewall correctly allowed and blocked traffic based on configured rules.

## 🎓 Learning Outcome
- Understood firewall rule management
- Learned inbound vs outbound filtering
- Tested live network traffic blocking
