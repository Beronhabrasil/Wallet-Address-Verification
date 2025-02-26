📌 Documentation - Wallet Address Verification
Description
This code aims to prevent errors in cryptocurrency deposits to exchanges or incorrect addresses. It verifies whether the wallet address entered by the user matches the provided address, ensuring that funds are sent correctly.

📜 Functionality
The user enters a provided wallet address.
The user enters a typed wallet address.
The system compares both addresses:
If they match, it confirms that the address is correct.
If they do not match, it alerts the user about a possible error.
The process can be repeated until the user decides to stop.

📌 User Guide - Wallet Address Comparison
This guide explains how to use the code to verify if two wallet addresses are the same, helping to prevent errors in transactions.

1️⃣ Requirements Before Using
✅ Have Python installed on your computer.
✅ Install the easygui library (if not already installed) by running:

bash
Kopieren
Bearbeiten
pip install easygui
✅ Download and save the code in a file, e.g., compare_address.py.

2️⃣ How to Run the Code
Open a terminal or command prompt in the folder where the file is saved and execute:

bash
Kopieren
Bearbeiten
python compare_address.py
3️⃣ How to Use the Program
1️⃣ A window will appear asking you to enter the first wallet address (previous address).

Type the address and click "OK".
To cancel, click "Cancel", and the program will exit.
2️⃣ Next, another window will prompt you to enter the second wallet address (new address).

Type the address and click "OK".
If you click "Cancel", the program will exit.
3️⃣ The program will compare the addresses and display a result:

If they match, a message will confirm that the addresses are the same.
If they do not match, the program will alert you that the addresses are different.
4️⃣ After seeing the result, the program will ask:
"Do you want to compare another address?"

Click "Yes" to repeat the process with new addresses.
Click "No" to close the program.
4️⃣ Example of Use
📌 Input:

Previous address: 1A2b3C4D5e6F7G8H9i0J
New address: 1A2b3C4D5e6F7G8H9i0J
✅ Output:
✔ The addresses are the same.

📌 Input:

Previous address: 1A2b3C4D5e6F7G8H9i0J
New address: 9Z8Y7X6W5V4U3T2S1R0Q
⚠ Output:
❌ The addresses do not match!
