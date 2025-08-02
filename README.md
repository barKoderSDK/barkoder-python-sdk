# Barkoder Python SDK

High-performance barcode scanning SDK for Python with support for 40+ barcode formats.

## Quick Start

### Download

Choose your system architecture:
- **[x86_64](releases/latest/x86_64/)** - Intel/AMD 64-bit systems
- **[ARM64](releases/latest/arm64/)** - ARM 64-bit systems (Apple Silicon, AWS Graviton)

### Installation

1. **Download and extract** the appropriate package
2. **Install dependencies:**
   ```bash
   pip install opencv-python numpy setproctitle
   ```
3. **Configure license key** in `config.json`
4. **Run the sample:**
   ```bash
   python3 run.py
   ```

## What's Included

Each package contains:
- `Barkoder/` - Python package with compiled SDK
- `config.json` - Configuration template
- `run.py` - Sample application
- `qr.bmp` - Test barcode image
- `README.md` - Detailed documentation

## 🔧 System Requirements

- **OS**: Linux (Ubuntu, RHEL, Amazon Linux, CentOS, etc.)
- **Python**: 3.9 or higher
- **Architecture**: x86_64 or ARM64
- **Dependencies**: libcurl (system library)

## Usage Example

```python
from Barkoder import BarkoderSDK
import cv2
import json

# Initialize SDK
status = BarkoderSDK.initialize("YOUR_LICENSE_KEY")
print(f"SDK Status: {status}")

# Configure for QR codes
QR = BarkoderSDK.constants["Decoders"]["QR"]
BarkoderSDK.setEnabledDecoders([QR])

# Load and decode image
img = cv2.imread('qr.bmp', cv2.IMREAD_GRAYSCALE)
height, width = img.shape[:2]
result_json = BarkoderSDK.decodeImage(img, width, height)

# Process results
result = json.loads(result_json)
if result["resultsCount"] > 0:
    print(f"Decoded: {result['textualData']}")
```

## 🏷️ Supported Barcode Types

### 2D Codes
QR Code, QR Micro, PDF417, PDF417 Micro, DataMatrix, Aztec, Aztec Compact, MaxiCode, DotCode

### 1D Codes  
Code128, Code93, Code39, Code32, Codabar, Code11, MSI, UPC-A, UPC-E, EAN-13, EAN-8

### Industrial Codes
Code25, Interleaved 2/5, ITF-14, IATA 2/5, Matrix 2/5, Datalogic 2/5, COOP 2/5, Telepen

### Postal Codes
DataBar (RSS), Australian Post, Royal Mail, KIX, Japanese Post, PostNet, Planet, IMB

## API Reference

### Core Functions
- `BarkoderSDK.initialize(license_key)` - Initialize SDK
- `BarkoderSDK.decodeImage(image, width, height)` - Decode barcode
- `BarkoderSDK.setEnabledDecoders(decoders)` - Set active barcode types
- `BarkoderSDK.setDecodingSpeed(speed)` - Set performance vs accuracy
- `BarkoderSDK.setRegionOfInterest(x, y, width, height)` - Set scan area

### Configuration Options
- `BarkoderSDK.setDatamatrixDpmModeEnabled(True)` - Enable DPM mode
- `BarkoderSDK.setCode39ChecksumType(type)` - Set checksum validation
- `BarkoderSDK.setMsiChecksumType(type)` - Set MSI checksum

## 📁 Project Structure

```
releases/
├── latest/                    # Current release
│   ├── x86_64/               # Intel/AMD builds
│   ├── arm64/                # ARM builds
│   └── RELEASE.md            # Release notes
└── archive/                  # Previous versions
    ├── v1.6.0.2/
    └── v1.6.0.1/
```

## 🔐 License

This SDK contains proprietary components. A valid license key is required for operation.

## 📞 Support

- **Documentation**: [barkoder.com/docs](https://barkoder.com/docs)
- **Contact**: [barkoder.com/contact](https://barkoder.com/contact)
- **Issues**: [Report issues](https://barkoder.com/issues)

## 📜 Version History

See [Releases](../../releases) for detailed version history and download links.
