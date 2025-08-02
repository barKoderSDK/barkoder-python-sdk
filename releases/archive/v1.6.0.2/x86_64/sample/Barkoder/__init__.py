"""
Barkoder SDK Package

This package provides Python bindings for the Barkoder barcode scanning SDK.
"""

import sys
import os

# Add the package directory to Python path so BarkoderSDK.so can be found
package_dir = os.path.dirname(__file__)
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# Import the native BarkoderSDK library first
import BarkoderSDK

# Import the Barkoder wrapper module which extends BarkoderSDK
from . import Barkoder

# Make BarkoderSDK available at package level
# After importing Barkoder, BarkoderSDK will have additional methods and constants

# Package metadata
__version__ = "1.6.2"
__author__ = "barKoder"
__description__ = "Python SDK for barKoder barcode scanning"

# Expose main functionality at package level
__all__ = ['BarkoderSDK', 'Barkoder']