#!/usr/bin/env python3
"""
Barkoder SDK Python Wrapper

This module extends the native BarkoderSDK with Python-friendly constants and helper methods.
It provides a high-level interface for barcode scanning functionality.

Author: barKoder
Version: 1.6.2
"""

import BarkoderSDK

# ============================================================================
# CONSTANTS DEFINITIONS
# ============================================================================
# Initialize the constants dictionary that will hold all configuration options
# These constants provide a more readable way to configure the SDK
BarkoderSDK.constants = {
    "DecodingSpeed": None,           # Speed vs accuracy trade-off settings
    "Decoders": None,                # Available barcode format decoders
    "Code11ChecksumType": None,      # Code11 checksum validation options
    "Code39ChecksumType": None,      # Code39 checksum validation options
    "MsiChecksumType": None,         # MSI checksum validation options
    "UpcEanDeblur": None,           # UPC/EAN deblur enhancement settings
    "MulticodeCachingEnabled": None, # Multiple barcode caching options
    "EnableMisshaped1D": None,       # Detection of misshaped 1D barcodes
    "EnableVINRestrictions": None,   # VIN (Vehicle Identification Number) restrictions
    "Formatting": None               # Data formatting options
};

# Decoding Speed Configuration
# Controls the trade-off between scanning speed and accuracy
BarkoderSDK.constants["DecodingSpeed"] = {
    "Fast": 0,       # Fastest scanning, may miss some difficult barcodes
    "Normal": 1,     # Balanced speed and accuracy (recommended)
    "Slow": 2,       # Slower but more thorough scanning
    "Rigorous": 3    # Most thorough scanning, slowest performance
};

# Supported Barcode Decoders
# Each decoder corresponds to a specific barcode format/symbology
BarkoderSDK.constants["Decoders"] = {
    # 2D Matrix Codes
    "Aztec": 0,                  # Aztec 2D barcode
    "AztecCompact": 1,           # Compact Aztec variant
    "QR": 2,                     # QR Code (most common 2D format)
    "QRMicro": 3,                # Micro QR Code (smaller variant)
    "PDF417": 15,                # PDF417 2D barcode
    "PDF417Micro": 16,           # Micro PDF417 variant
    "Datamatrix": 17,            # Data Matrix 2D barcode
    "Dotcode": 27,               # DotCode 2D format
    "MaxiCode": 39,              # MaxiCode 2D format
    
    # Linear 1D Codes
    "Code128": 4,                # Code 128 (versatile 1D format)
    "Code93": 5,                 # Code 93 1D barcode
    "Code39": 6,                 # Code 39 1D barcode
    "Codabar": 7,                # Codabar 1D format
    "Code11": 8,                 # Code 11 1D barcode
    "Msi": 9,                    # MSI Plessey 1D format
    "Code32": 25,                # Code 32 (Italian Pharmacode)
    "Telepen": 26,               # Telepen 1D format
    
    # UPC/EAN Family
    "UpcA": 10,                  # UPC-A (Universal Product Code)
    "UpcE": 11,                  # UPC-E (compressed UPC)
    "UpcE1": 12,                 # UPC-E1 variant
    "Ean13": 13,                 # EAN-13 (European Article Number)
    "Ean8": 14,                  # EAN-8 (short EAN format)
    
    # Code 25 Family
    "Code25": 18,                # Standard Code 25
    "Interleaved25": 19,         # Interleaved 2 of 5
    "ITF14": 20,                 # ITF-14 (shipping container code)
    "IATA25": 21,                # IATA 2 of 5
    "Matrix25": 22,              # Matrix 2 of 5
    "Datalogic25": 23,           # Datalogic 2 of 5
    "COOP25": 24,                # COOP 2 of 5
    
    # GS1 DataBar Family
    "Databar14": 29,             # GS1 DataBar-14
    "DatabarLimited": 30,        # GS1 DataBar Limited
    "DatabarExpanded": 31,       # GS1 DataBar Expanded
    
    # Postal Codes
    "PostalIMB": 32,             # USPS Intelligent Mail Barcode
    "Postnet": 33,               # USPS POSTNET
    "Planet": 34,                # USPS PLANET
    "AustralianPost": 35,        # Australia Post barcode
    "RoyalMail": 36,             # Royal Mail 4-state barcode
    "KIX": 37,                   # Dutch KIX postal code
    "JapanesePost": 38,          # Japan Post barcode
};

# Setting Types for Specific Decoder Configuration
# Used internally by setSpecificConfig method
BarkoderSDK.constants["SettingType"] = {
    "checksumType": 0,      # Configure checksum validation
    "expandToUPCA": 1,      # Expand UPC-E to UPC-A format
    "dpmMode": 2,           # Direct Part Marking mode for 2D codes
    "multiPartMerge": 3     # Merge multiple barcode parts
};

# Code 11 Checksum Validation Options
BarkoderSDK.constants["Code11ChecksumType"] = {
    "disabled": 0,    # No checksum validation
    "single": 1,      # Single checksum digit
    "double": 2       # Double checksum digits (more secure)
};

# Code 39 Checksum Validation Options
BarkoderSDK.constants["Code39ChecksumType"] = {
    "disabled": 0,    # No checksum validation
    "enabled": 1      # Enable checksum validation
};

# MSI Plessey Checksum Validation Options
# Various algorithms for validating MSI barcodes
BarkoderSDK.constants["MsiChecksumType"] = {
    "disabled": 0,      # No checksum validation
    "mod10": 1,         # Modulo 10 checksum
    "mod11": 2,         # Modulo 11 checksum
    "mod1010": 3,       # Double modulo 10 checksum
    "mod1110": 4,       # Modulo 11 + modulo 10 checksum
    "mod11IBM": 5,      # IBM variant of modulo 11
    "mod1110IBM": 6     # IBM variant of mod11+mod10
};

# UPC/EAN Deblur Enhancement
# Improves reading of blurred or out-of-focus UPC/EAN codes
BarkoderSDK.constants["UpcEanDeblur"] = {
    "Disable": 0,    # Standard processing
    "Enable": 1      # Enhanced deblur processing
};

# Multicode Caching
# Caches results when scanning multiple barcodes in sequence
BarkoderSDK.constants["MulticodeCachingEnabled"] = {
    "Disable": 0,    # No caching (scan each frame independently)
    "Enable": 1      # Cache results for better multicode performance
};

# Misshaped 1D Barcode Detection
# Detects 1D barcodes that are curved, skewed, or distorted
BarkoderSDK.constants["EnableMisshaped1D"] = {
    "Disable": 0,    # Only detect straight barcodes
    "Enable": 1      # Detect curved/distorted barcodes (slower)
};

# VIN (Vehicle Identification Number) Restrictions
# Applies VIN format validation rules
BarkoderSDK.constants["EnableVINRestrictions"] = {
    "Disable": 0,    # No VIN validation
    "Enable": 1      # Apply VIN format restrictions
};

# Data Formatting Options
# Applies specific formatting rules to decoded data
BarkoderSDK.constants["Formatting"] = {
    "Disabled": 0,     # Raw data, no formatting
    "Automatic": 1,    # Auto-detect and apply appropriate formatting
    "GS1": 2,          # GS1 standard formatting (retail/supply chain)
    "AAMVA": 3,        # AAMVA standard (driver's licenses/IDs)
    "SADL": 4          # SADL standard formatting
};

# Note: EncodingCharacterSet is currently not implemented
# BarkoderSDK.constants.EncodingCharacterSet = {
#     "None": 0
# }

# ============================================================================
# HELPER METHODS
# ============================================================================
# These methods provide convenient wrappers around the native SDK functions
def setCode11ChecksumType(code11ChecksumType):
    """
    Configure checksum validation for Code 11 barcodes.
    
    Args:
        code11ChecksumType: Checksum type from BarkoderSDK.constants["Code11ChecksumType"]
                           (disabled, single, or double)
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["Code11"], 
        BarkoderSDK.constants["SettingType"]["checksumType"], 
        code11ChecksumType
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setCode11ChecksumType = setCode11ChecksumType

def setCode39ChecksumType(code39ChecksumType):
    """
    Configure checksum validation for Code 39 barcodes.
    
    Args:
        code39ChecksumType: Checksum type from BarkoderSDK.constants["Code39ChecksumType"]
                           (disabled or enabled)
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["Code39"], 
        BarkoderSDK.constants["SettingType"]["checksumType"], 
        code39ChecksumType
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setCode39ChecksumType = setCode39ChecksumType

def setMsiChecksumType(msiChecksumType):
    """
    Configure checksum validation for MSI Plessey barcodes.
    
    Args:
        msiChecksumType: Checksum type from BarkoderSDK.constants["MsiChecksumType"]
                        (disabled, mod10, mod11, mod1010, mod1110, mod11IBM, mod1110IBM)
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["Msi"], 
        BarkoderSDK.constants["SettingType"]["checksumType"], 
        msiChecksumType
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setMsiChecksumType = setMsiChecksumType

def setDatamatrixDpmModeEnabled(dpmModeEnabled):
    """
    Enable/disable DPM (Direct Part Marking) mode for Data Matrix barcodes.
    DPM mode is optimized for reading barcodes etched/marked directly on parts.
    
    Args:
        dpmModeEnabled: Boolean - True to enable DPM mode, False to disable
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["Datamatrix"], 
        BarkoderSDK.constants["SettingType"]["dpmMode"], 
        dpmModeEnabled
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setDatamatrixDpmModeEnabled = setDatamatrixDpmModeEnabled

def setQRDpmModeEnabled(dpmModeEnabled):
    """
    Enable/disable DPM (Direct Part Marking) mode for QR Code barcodes.
    DPM mode is optimized for reading barcodes etched/marked directly on parts.
    
    Args:
        dpmModeEnabled: Boolean - True to enable DPM mode, False to disable
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["QR"], 
        BarkoderSDK.constants["SettingType"]["dpmMode"], 
        dpmModeEnabled
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setQRDpmModeEnabled = setQRDpmModeEnabled

def setQRMicroDpmModeEnabled(dpmModeEnabled):
    """
    Enable/disable DPM (Direct Part Marking) mode for Micro QR Code barcodes.
    DPM mode is optimized for reading barcodes etched/marked directly on parts.
    
    Args:
        dpmModeEnabled: Boolean - True to enable DPM mode, False to disable
    """
    BarkoderSDK.setSpecificConfig(
        BarkoderSDK.constants["Decoders"]["QRMicro"], 
        BarkoderSDK.constants["SettingType"]["dpmMode"], 
        dpmModeEnabled
    )

# Attach the method to the BarkoderSDK module
BarkoderSDK.setQRMicroDpmModeEnabled = setQRMicroDpmModeEnabled

def setEnabledDecoders(decoders):
    """
    Enable specific barcode decoders for scanning.
    Only the specified decoders will be active during scanning.
    
    Args:
        decoders: List of decoder constants from BarkoderSDK.constants["Decoders"]
                 Example: [BarkoderSDK.constants["Decoders"]["QR"], BarkoderSDK.constants["Decoders"]["Code128"]]
    
    Example:
        # Enable only QR and PDF417 decoders
        decoders = [BarkoderSDK.constants["Decoders"]["QR"], BarkoderSDK.constants["Decoders"]["PDF417"]]
        BarkoderSDK.setEnabledDecoders(decoders)
    """
    total_decoders = len(decoders)
    BarkoderSDK.setEnabledDecoders_c(decoders, total_decoders)

# Attach the method to the BarkoderSDK module
BarkoderSDK.setEnabledDecoders = setEnabledDecoders

# ============================================================================
# END OF WRAPPER METHODS
# ============================================================================