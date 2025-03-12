# PRODIGY_CS_03
🔐 Password Strength Checker
📌 About
This is a simple password strength checker written in Python. It evaluates a user's password based on security best practices and provides feedback on its strength.

🚀 Features
✔️ Checks if the password has at least 8 characters
✔️ Ensures the password contains a digit (0-9)
✔️ Verifies the presence of an uppercase letter (A-Z)
✔️ Confirms the use of a lowercase letter (a-z)
✔️ Requires at least one special character (!@#$%^&*(){}<>.?)
✔️ Provides real-time feedback on password strength

📜 How It Works
1️⃣ The script continuously prompts the user to enter a password.
2️⃣ If the user types "exit", the program stops.
3️⃣ The script evaluates the password and returns one of the following messages:

Weak Password: If it lacks minimum length, digits, uppercase, or lowercase letters.
Medium Password: If it lacks special characters.
Strong Password: If all criteria are met.
