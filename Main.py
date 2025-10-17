"""
File: main.py

Description: This module contains the test simulation for the Into the Grid assignment.
It creates hacker objects, rigs, and assets to simulate attacks, encryption, decryption, extraction, and rig upgrades according to the task specifications.

Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker


def run_simulation():
    """Run a sample scenario to test hacker interactions and game mechanics."""

    # Create two hackers
    alice = Hacker("ZeroGhost")
    bob = Hacker("ByteFang")

    print("=== INITIAL STATE ===")
    print(alice)
    print(bob)

    # Both hackers acquire rigs
    alice.acquire_rig()
    bob.acquire_rig()

    # Alice launches several attacks on Bob
    print("\n=== ATTACK PHASE ===")
    alice.launch_attack(bob)
    alice.launch_attack(bob)
    alice.launch_attack(bob)  # May break Bob's rig

    # If Bob’s rig is broken, Alice extracts unsecured assets
    print("\n=== EXTRACTION PHASE ===")
    alice.extract_assets(bob)

    # Generate new assets on Bob’s rig for demonstration
    print("\n=== ASSET GENERATION ===")
    bob.rig.generate_asset()
    bob.rig.generate_asset()

    # Encrypt and decrypt demonstration
    print("\n=== ENCRYPTION / DECRYPTION ===")
    alice.inventory.append(bob.rig.generate_asset())  # Add a new asset for Alice
    alice.encrypt_asset("CryptoToken")
    alice.decrypt_asset("CryptoToken")

    # Upgrade and repair phase
    print("\n=== UPGRADE & REPAIR PHASE ===")
    alice.upgrade_rig()
    bob.rig.repair(bob.inventory)

    print("\n=== FINAL STATE ===")
    print(alice)
    print(bob)


if __name__ == "__main__":
    run_simulation()