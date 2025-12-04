# .py-tools
A repository for basic security utility scripts
his repository contains basic Python scripts and tools developed for security analysis and foundational knowledge demonstration, essential for any aspiring Security Operations Center (SOC) Analyst.This specific project demonstrates proficiency in basic Python scripting and understanding of Cryptographic principles (Entropy).

🔑Project 1: Password Entropy Calculator
This script calculates the theoretical strength (entropy) of a password, helping to assess the effectiveness of password policies and the security of user credentials.

🎯 Goal:To demonstrate an understanding of password strength calculation and foundational Python scripting capabilities, which are key requirements for analyzing and triaging security incidents.

⚙️ Technology Used:
Language: Python 3
Libraries: math💻 

Entropy Calculation Logic:  Password entropy (E) is measured in bits and is calculated using the following formula: E = L . log2 (R) 
Where: 
L(Length): The total number of characters in the password.
R(Character Set Size): The number of unique characters available to be used. The script approximates R by checking for the presence of four character groups:
Lowercase (26)
Uppercase (26)
Digits (10)
Symbols (~33)
Thresholds: A password with > 80 bits of entropy is generally considered strong for modern systems.
