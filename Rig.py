"""
File: Rig.py

Description: This module defines the Rig class, representing a hacker’s cyber rig (computer system) that can store assets, take damage, repair itself, and be upgraded.
Rigs play a central role in attacks and resource management during the simulation.

Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
import random

class Rig:

    def __init__(self, name):
        # Rig properties
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        # Each rig starts with some default assets
        self.storage = [
            Asset("Data Spike", "Used for attacks"),
            Asset("Data Spike", "Used for attacks"),
            Asset("Removable Drive", "Used for asset extraction")
        ]

    def take_hit(self):
        # Apply damage to the rig from a data spike attack
        if self.broken:
            print(f"{self.name} is already broken.")
            return

        # Increase damage count
        self.damage += 1
        # Damage threshold depends on rig’s upgrade level
        threshold = 2 + self.upgrade_level

        if self.damage >= threshold:
            self.broken = True
            print(f"{self.name} is broken!")
        else:
            print(f"{self.name} took damage. Current damage: {self.damage}")

    def repair(self, hacker_inventory):
        # Repair the rig using one CryptoToken from the hacker’s inventory
        token = next((a for a in hacker_inventory if a.name == "CryptoToken"), None)
        if not token:
            print("No CryptoToken to repair rig.")
            return False

        if self.damage == 0:
            print("Rig does not need repair.")
            return False

        hacker_inventory.remove(token)
        self.damage = 0
        self.broken = False
        print(f"{self.name} repaired successfully.")
        return True

    def upgrade(self, hacker_inventory):
        # Upgrade the rig using a Hardware Patch
        patch = next((a for a in hacker_inventory if a.name == "Hardware Patch"), None)
        if not patch:
            print("No Hardware Patch available.")
            return False

        hacker_inventory.remove(patch)
        self.upgrade_level += 1
        print(f"{self.name} upgraded to Level {self.upgrade_level}.")
        return True

    def generate_asset(self):
        # Generate a random new asset
        possible_assets = [
            Asset("Security Chip", "Used to encrypt or decrypt assets"),
            Asset("Hardware Patch", "Used to upgrade rigs"),
            Asset("CryptoToken", "Currency of the grid")
        ]
        new_asset = random.choice(possible_assets)
        self.storage.append(new_asset)
        print(f"{self.name} generated new asset: {new_asset}")
        return new_asset

    def condition(self):
        # Return a string describing the rig’s current condition
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        elif self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        else:
            return f"Damaged {self.damage}/2 (Level {self.upgrade_level})"

    def __str__(self):
        # Readable display of rig information and stored assets
        storage_items = ", ".join(a.name for a in self.storage)
        return f"Rig: {self.name} | Condition: {self.condition()} | Stored: [{storage_items}]"