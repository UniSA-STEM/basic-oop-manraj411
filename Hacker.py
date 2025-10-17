"""
File: Hacker.py

Description: This module defines the Hacker class that represents a player or character in the cyberpunk simulation.
Hackers manage assets, operate rigs, attack opponents, encrypt data, and upgrade their systems while managing their trace level.

Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
from rig import Rig

class Hacker:

    def __init__(self, name):
        # Hacker starts with a name, no rig, and one CryptoToken
        self.name = name
        self.trace_level = 0
        self.inventory = [Asset("CryptoToken", "Currency of the grid")]
        self.rig = None

    def acquire_rig(self):
        # Acquire a new rig using one CryptoToken
        token = next((a for a in self.inventory if a.name == "CryptoToken"), None)
        if not token:
            print("You need a CryptoToken to acquire a rig.")
            return
        self.inventory.remove(token)
        self.rig = Rig(f"{self.name}_Rig")
        print(f"{self.name} acquired new rig: {self.rig.name}")

    def launch_attack(self, target):
        # Launch a data spike at another hacker’s rig
        if not self.rig or self.rig.broken:
            print("You have no functional rig to attack with.")
            return
        if self.trace_level > 5:
            print("Trace level too high! You are exposed and cannot attack.")
            return

        spike = next((a for a in self.rig.storage if a.name == "Data Spike"), None)
        if not spike:
            print("No Data Spikes available!")
            return

        # Remove spike and inflict damage
        self.rig.storage.remove(spike)
        target.rig.take_hit()
        self.trace_level += 1
        print(f"{self.name} launched a data spike at {target.name}. Trace level: {self.trace_level}")

    def extract_assets(self, target):

        if not self.rig or not target.rig.broken:
            print("Target rig not broken or no rig available.")
            return
        drive = next((a for a in self.rig.storage if a.name == "Removable Drive"), None)
        if not drive:
            print("No Removable Drive available.")
            return

        unencrypted_assets = [a for a in target.rig.storage if not a.encrypted]
        for asset in unencrypted_assets:
            self.inventory.append(asset)
        target.rig.storage = [a for a in target.rig.storage if a.encrypted]
        print(f"{self.name} extracted {len(unencrypted_assets)} assets from {target.name}'s rig.")

    def encrypt_asset(self, asset_name):
        # Encrypt an asset in the hacker’s inventory using a Security Chip
        chip = next((a for a in self.inventory if a.name == "Security Chip"), None)
        if not chip:
            print("No Security Chip found.")
            return
        asset = next((a for a in self.inventory if a.name == asset_name), None)
        if asset:
            asset.encrypt()
            self.inventory.remove(chip)
            print(f"{asset_name} encrypted.")
        else:
            print(f"Asset {asset_name} not found in inventory.")

    def decrypt_asset(self, asset_name):
        # Decrypt an encrypted asset in the hacker’s inventory using a Security Chip
        chip = next((a for a in self.inventory if a.name == "Security Chip"), None)
        if not chip:
            print("No Security Chip available.")
            return
        asset = next((a for a in self.inventory if a.name == asset_name and a.encrypted), None)
        if asset:
            asset.decrypt()
            self.inventory.remove(chip)
            print(f"{asset_name} decrypted.")
        else:
            print(f"No encrypted asset {asset_name} found.")

    def upgrade_rig(self):
        # Upgrade the hacker’s rig using a Hardware Patch
        if not self.rig:
            print("No rig to upgrade.")
            return
        self.rig.upgrade(self.inventory)

    def __str__(self):
        # Readable display of hacker’s current state
        inv_list = ", ".join([a.name for a in self.inventory]) or "Empty"
        rig_name = self.rig.name if self.rig else "No rig"
        return f"Hacker: {self.name} | Rig: {rig_name} | Trace: {self.trace_level} | Inventory: [{inv_list}]"