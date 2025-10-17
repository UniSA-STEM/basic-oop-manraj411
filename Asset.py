"""
File: Asset.py

Description: This module defines the Asset class used to represent digital assets in the cyberpunk simulation.
Assets can be encrypted or decrypted and are used by hackers and rigs for trading, upgrading and security operations.

Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:

    def __init__(self, name, description):
        # Basic information about the asset
        self.name = name
        self.description = description
        # Assets are unencrypted by default
        self.encrypted = False

    def encrypt(self):
        # Encryption of the asset
        self.encrypted = True

    def decrypt(self):
        # Decryption of the asset
        self.encrypted = False

    def __str__(self):
        # Returns a readable string representation of the asset
        status = " [Encrypted]" if self.encrypted else ""
        return f"{self.name}: {self.description}{status}"

