#!/usr/bin/env python3
"""
USDT TRC20 Flash Sender Script (Simulation)

Description:
    This script simulates the "flash send" functionality of USDT (Tether) on the TRON (TRC20) network,
    based on the quaffiinn/usdt-flash-sender project. It performs a fake (simulated) transfer of USDT
    between two given wallet addresses, without requiring real private keys or actual transactions.
    The intention is for testing or demonstration purposes only. No real USDT is moved.

Usage:
    - Ensure you have Python 3 installed on Termux (Android) or Linux.
    - Install required dependencies (see instructions below).
    - Edit the BINANCE_ADDRESS and TRUST_ADDRESS variables below to your wallet addresses.
    - Optionally adjust the AMOUNT_USDT to send (in USDT).
    - Run the script: python3 flash_usdt_trc20.py

Compatibility:
    - Designed for Termux (Android) or any Linux environment (no GUI needed).
    - Requires an internet connection to fetch token data (optional; simulation does not strictly need it).
    - The script uses the TronPy library to query TRON network data for USDT.

Dependencies:
    - tronpy: Python library for interacting with TRON. Install with:
        pip install tronpy
    - (Termux may require: pkg install python, pip, etc.)

Security and Limitations:
    - This script is a simulation. **No private keys are used or needed.**
    - Do NOT paste or share any private keys or sensitive data in this script.
    - Always keep your wallet keys secure. This script only uses public addresses.
    - If Tron network access fails or is unavailable, the script will continue in offline simulation mode.
    - Do not use this for actual transfers. It's for demonstration/testing only.
"""
import sys
import secrets

# === Configuration ===
# Provide your TRC20 USDT wallet addresses here (Base58 format, typically starts with 'T').
# The script will simulate sending from TRUST_ADDRESS to BINANCE_ADDRESS.
BINANCE_ADDRESS = "TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your actual Binance (TRC20 USDT) address
TRUST_ADDRESS   = "TYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"  # Replace with your actual Trust Wallet (TRC20 USDT) address

# Amount of USDT to "flash send" (in USDT units). This is a simulated amount.
AMOUNT_USDT = 10.0

# TRC20 USDT Token Contract (official TRON USDT contract address)
USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"

# === End Configuration ===

def is_valid_tron_address(addr: str) -> bool:
    """Basic check for Tron address format."""
    return isinstance(addr, str) and len(addr) >= 30 and addr[0] == 'T'

# Validate addresses
if not (is_valid_tron_address(BINANCE_ADDRESS) and is_valid_tron_address(TRUST_ADDRESS)):
    print("[!] ERROR: Please set valid Tron (TRC20) addresses for BINANCE_ADDRESS and TRUST_ADDRESS in the script.")
    sys.exit(1)

print("\n--- USDT TRC20 Flash Sender (Simulation) ---")
print("Simulating transfer of USDT on TRON network (TRC20).")
print(f"From (Trust Wallet) : {TRUST_ADDRESS}")
print(f"To   (Binance Addr) : {BINANCE_ADDRESS}")
print(f"Amount            : {AMOUNT_USDT} USDT\n")

# Attempt to fetch token data using TronPy (optional)
try:
    from tronpy import Tron
    client = Tron()
    usdt_contract = client.get_contract(USDT_CONTRACT)
    symbol = usdt_contract.functions.symbol()
    decimals = usdt_contract.functions.decimals()
    print(f"[+] Connected to TRON network. Token symbol: {symbol}, Decimals: {decimals}")

    # Fetch balances
    try:
        bal_trust = usdt_contract.functions.balanceOf(TRUST_ADDRESS) or 0
        bal_bin = usdt_contract.functions.balanceOf(BINANCE_ADDRESS) or 0
        bal_trust_hr = bal_trust / (10 ** decimals)
        bal_bin_hr = bal_bin / (10 ** decimals)
        print(f"[+] Balance of Trust Wallet address ({TRUST_ADDRESS}): {bal_trust_hr} {symbol}")
        print(f"[+] Balance of Binance address ({BINANCE_ADDRESS}): {bal_bin_hr} {symbol}")
    except Exception as e:
        print(f"[!] Unable to fetch balances: {e}")
        bal_trust_hr = None
        bal_bin_hr = None

except ImportError:
    print("[!] TronPy not installed or failed to import. Install with 'pip install tronpy'. Proceeding with simulation only.")
    symbol = "USDT"
    decimals = 6
    bal_trust_hr = None
    bal_bin_hr = None

except Exception as e:
    print(f"[!] Error accessing Tron network or USDT contract: {e}")
    print("Continuing in offline simulation mode...")
    symbol = "USDT"
    decimals = 6
    bal_trust_hr = None
    bal_bin_hr = None

print("\n--- Simulating USDT Transfer ---")
amount_tokens = AMOUNT_USDT

# Check if we have a balance to compare
if bal_trust_hr is not None:
    if AMOUNT_USDT > bal_trust_hr:
        print(f"[!] Warning: Trust wallet has {bal_trust_hr} {symbol}, which is less than the send amount {AMOUNT_USDT}. Proceeding with simulation anyway.")
else:
    print("[*] Trust wallet balance unavailable; cannot verify sufficient balance (simulation only).")

print(f"Sending {amount_tokens} {symbol} from Trust Wallet to Binance address...")

# Generate a fake transaction ID for demonstration
txid = secrets.token_hex(32)  # 64 hex chars
print(f"[+] Transaction simulated. (Fake TXID: {txid})\n")

# Compute and display new balances (simulation)
if bal_trust_hr is not None and bal_bin_hr is not None:
    new_bal_trust = bal_trust_hr - AMOUNT_USDT
    new_bal_bin = bal_bin_hr + AMOUNT_USDT
    # Avoid negative balance display
    if new_bal_trust < 0:
        new_bal_trust = 0.0
    print("[+] NEW (simulated) balances after transfer:")
    print(f"    Trust Wallet:   {new_bal_trust} {symbol}")
    print(f"    Binance Addr:   {new_bal_bin} {symbol}")
else:
    print("[*] Balances after transfer not computed (offline simulation mode).")
    print("    (Run with tronpy installed and a network connection to compute balances.)")

print("\n--- Simulation Complete ---")
print("Note: This was a SIMULATED transfer. No actual USDT was moved.")
print("Ensure you handle real private keys and wallet data securely when performing real transactions.")
