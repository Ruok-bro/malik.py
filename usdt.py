#!/usr/bin/env python3
# USDT Flash Sender (Termux-compatible)
# ====================================
# This script simulates the core functionality of the "USDT Flash Sender" tool01.
# It allows a user to "send" fake USDT (Tether) tokens on the TRC20 (Tron) network in a simulated manner.
# No real blockchain transactions or funds are used; this is purely for demonstration and testing23.
#
# Summary of functionality:
# - Prompts for a recipient address and an amount of USDT.
# - Confirms the transfer with the user.
# - Simulates a network delay.
# - Prints a fake transaction ID and confirms completion.
#
# Dependencies:
# - Python 3.x (Termux: install via `pkg install python`)
# - No external libraries required (uses only the Python standard library).
#
# Installation (Termux):
# 1. Install Python: `pkg install python`
# 2. (Optional) Install pip if not present: `pkg install python-pip`
# 3. Place this script in a writable directory on Termux.
#
# Usage:
# 1. Run the script: `python3 usdt_flash_sender.py`
# 2. When prompted, enter the recipient's TRC20 address (e.g., starting with 'T' for Tron addresses).
# 3. Enter the amount of USDT to send.
# 4. Confirm the transaction when prompted.
# 5. The script will simulate sending and display a fake transaction ID.
#
# Limitations & Notes:
# - This tool DOES NOT interact with any real blockchain or wallet. It only simulates an instant transfer
#   for UI/testing purposes, as described by the original project45.
# - Ensure you do not use real private keys or sensitive data, as this is just a dummy interface.
# - The recipient address is not validated beyond basic checks.
# - The transaction ID is randomly generated and holds no real meaning.
#
# Below is the implementation of this simulation.
import time
import random
import sys

def main():
    print("\n=== USDT Flash Sender (Simulation) ===")
    # Prompt for recipient address
    recipient = input("Enter recipient address: ").strip()
    if not recipient:
        print("Error: No address entered.")
        sys.exit(1)

    # Prompt for amount
    amount_input = input("Enter amount of USDT to send: ").strip()
    try:
        # Convert to float to allow decimal amounts
        amount = float(amount_input)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Error: Amount must be a positive number.")
        sys.exit(1)

    # Confirm transaction details with user
    print(f"\nYou are about to send {amount} fake USDT to {recipient}")
    confirm = input("Confirm transaction? (y/n): ").strip().lower()
    if confirm not in ('y', 'yes'):
        print("Transaction cancelled by user.")
        sys.exit(0)

    # Simulate sending transaction
    print("\nSimulating transaction...", end='', flush=True)
    # Simulate a short delay (instant simulation)
    for i in range(3):
        print(".", end='', flush=True)
        time.sleep(0.5)
    print(" Done!")

    # Generate a fake transaction ID (64 hex chars, similar to a Tron txID)
    fake_txid = "0x" + ''.join(random.choices('0123456789abcdef', k=64))
    # Print transaction details
    print("\nTransaction successful!")
    print(f"Transaction ID: {fake_txid}")
    print(f"Recipient: {recipient}")
    print(f"Amount: {amount} USDT (simulated)")
    # Add a timestamp for realism
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} UTC")
    print("\n*** NOTE: This was a simulated transaction (no real USDT was sent) ***")

if __name__ == "__main__":
    main()
