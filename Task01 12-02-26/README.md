# 🔍 Task 1 - Network Port Scanning
📅 Date: 12 Feb 2026

---

## 🎯 Objective 🎯
To scan the local network using Nmap, identify open ports, and analyze scanning traffic using Wireshark.

---

## 🛠️ Tools Used 🧰
- 🐧 Kali Linux
- 📡 Nmap
- 🦈 Wireshark

---

## 🧪 Steps Performed 🧪

### 1️⃣ Find Local IP Range 🌐
- Used `ip a` to identify the local network range.

---

### 2️⃣ Perform Nmap TCP SYN Scan ⚡
- Executed TCP SYN scan using:

```bash
sudo nmap -sS <IP_RANGE>/24 -oN nmap_results.txt

    💾 Saved scan output in text format.

3️⃣ Capture Traffic with Wireshark 🦈

    Started Wireshark with root privileges:

sudo wireshark

    📶 Selected active network interface (wlan0/eth0).

    ▶️ Started packet capture.

    🔁 Ran Nmap scan while capturing traffic.

4️⃣ Filter Nmap Traffic 🔎

    Applied the following display filter to isolate SYN scan packets:

tcp.flags.syn == 1 && tcp.flags.ack == 0

    ✅ Displayed only Nmap scanning traffic.

5️⃣ Save Filtered Capture 💾

    Exported displayed packets.

    Saved file as:

nmap_only_capture.pcapng
