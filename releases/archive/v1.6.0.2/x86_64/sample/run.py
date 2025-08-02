#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-

"""
Barkoder SDK Python Demo Application

This script demonstrates how to use the Barkoder SDK to decode barcodes from an image.
It reads configuration from a JSON file, initializes the SDK, and processes an image.
"""

from Barkoder import BarkoderSDK
import json
import numpy as np
import cv2 as cv
import os
import sys

from setproctitle import setproctitle

def load_config():
    """Load configuration from config.json file"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    
    if not os.path.exists(config_path):
        print(f"Error: Configuration file not found at {config_path}")
        print("Please create config.json with your app_name and license_key")
        sys.exit(1)
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Validate required fields
        if 'license_key' not in config:
            print("Error: 'license_key' not found in config.json")
            sys.exit(1)
        
        if config['license_key'] == 'YOUR_LICENSE_KEY_HERE':
            print("Warning: Using placeholder license key from config.json")
            print("Please set a valid license_key for full functionality - app will still decode barcodes, results will be limited")
        
        return config
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in config file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

# Load configuration
config = load_config()

# Set process title from config
app_name = config.get('app_name', 'barkoder-demo')
setproctitle(app_name)

version = BarkoderSDK.getLibVersion();
print("SDK version: ", version)

# Initialize with license key from config
status = BarkoderSDK.initialize(config['license_key'])
print("SDK status: ", status)

#---------------configure the SDK--------------
QR = BarkoderSDK.constants["Decoders"]["QR"];
PDF417 = BarkoderSDK.constants["Decoders"]["PDF417"];

#set desired decoders
decoders = [QR, PDF417];
BarkoderSDK.setEnabledDecoders(decoders);

#set desired decodingSpeed
decodingSpeed = BarkoderSDK.constants["DecodingSpeed"]["Normal"];
BarkoderSDK.setDecodingSpeed(decodingSpeed);

#set desired ROI
BarkoderSDK.setRegionOfInterest(0, 0, 100, 100);

#set desired DPM mode
BarkoderSDK.setDatamatrixDpmModeEnabled(False);
#---------------configure the SDK--------------

with open('/proc/self/comm', 'r') as f:
    print(f"Current app name: {f.read().strip()}")

#---------------read and scan an image---------
img = cv.imread('qr.bmp', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

height, width = img.shape[:2]

result_json = BarkoderSDK.decodeImage(img, width, height)
#---------------read and scan an image---------



#---------------handle the result--------------
result = json.loads(result_json)

print("resultsCount: ", result["resultsCount"])

# the result is a Python dictionary:
if result["resultsCount"] == 1:
    print(result["barcodeTypeName"])
    print(result["textualData"])
    
elif result["resultsCount"] > 1:
    for res in result["results"]:
        print(res["barcodeTypeName"])
        print(res["textualData"])
        print("---------------------------")
        
else:
    print("No barcode found.")
#---------------handle the result--------------