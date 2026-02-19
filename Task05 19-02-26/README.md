# 🔎 Task 5 - Network Traffic Analysis using Wireshark

## 🎯 Objective
Capture live network traffic and analyze different network protocols using Wireshark.

## 🛠 Tool Used
- Wireshark
- Kali Linux

## 🔧 Steps Performed

1. Opened Wireshark with root privileges.
2. Selected the active network interface (eth0) to start packet capturing.
3. Generated network traffic by opening websites such as:
   - YouTube
   - ChatGPT  
   using the Firefox browser.
4. Stopped the capture after generating sufficient traffic.
5. Applied protocol-based filters in Wireshark to identify:
   - DNS packets
   - TCP packets
   - TLS packets
6. Initially, ICMP packets were not captured because normal web browsing does not generate ICMP traffic.
7. Restarted the capture process and manually generated ICMP traffic using the following command in terminal:

   ```bash
   ping google.com
   ```

8. Successfully captured ICMP Echo Request and Echo Reply packets.
9. Applied individual display filters for each protocol:
   - `dns`
   - `tcp`
   - `tls`
   - `icmp`
10. Exported the filtered packets separately using:

    ```
    File → Export Specified Packets → Displayed
    ```

11. Saved each filtered protocol capture in `.pcapng` format.

---

## 📊 Protocols Identified
- DNS
- TCP
- ICMP
- TLS

---

## 📌 Observations
- DNS packets were used for domain name resolution.
- TCP packets handled reliable communication between systems.
- ICMP packets were generated during ping operations.
- TLS packets were observed for secure web communication.

---

## 🎓 Learning Outcome
- Understood how network packets are captured.
- Learned how to filter and analyze specific protocols.
- Gained hands-on experience with live traffic analysis.
- Understood the role of ICMP in network diagnostics.
