# Barkoder Python SDK - Distribution Package

This directory contains the built and packaged Barkoder Python SDK ready for distribution and consumption by end users.

## Package Contents

### Architecture Support
- `x86_64/` - Intel/AMD 64-bit builds
- `arm64/` - ARM 64-bit builds (e.g., Apple Silicon, AWS Graviton)

### Each Architecture Package Contains
```
sample/
├── Barkoder/                 # Python package
│   ├── __init__.py          # Package initializer
│   ├── Barkoder.py          # Main SDK wrapper
│   └── BarkoderSDK.so       # Compiled C++ extension
├── config.json              # Configuration template
├── run.py                   # Sample application
└── qr.bmp                   # Test barcode image
```

## Quick Start

1. **Choose your architecture:**
   ```bash
   # For x86_64 systems
   cd x86_64/sample
   
   # For ARM64 systems  
   cd arm64/sample
   ```

2. **Install Python dependencies:**
   ```bash
   pip install opencv-python numpy setproctitle
   ```

3. **Configure your license:**
   ```bash
   # Edit config.json with your actual license key
   nano config.json
   ```

4. **Run the sample:**
   ```bash
   python3 run.py
   ```

## Integration into Your Project

### Method 1: Copy the Barkoder Package
```bash
# Copy the entire Barkoder directory to your project
cp -r x86_64/sample/Barkoder /path/to/your/project/
```

### Method 2: Use as Reference
Use the sample files as a template for integrating the SDK into your existing Python application.

## Configuration

Edit `config.json` to customize your application:

```json
{
  "app_name": "your-app-name",
  "license_key": "YOUR_ACTUAL_LICENSE_KEY_HERE",
  "description": "Your application description",
  "version": "1.6.0.2"
}
```

## System Requirements

- **Operating System**: Linux (Ubuntu, RHEL, Amazon Linux, etc.)
- **Python**: 3.9 or higher
- **Architecture**: x86_64 or ARM64
- **Dependencies**: 
  - libcurl (system library)
  - OpenCV Python (`pip install opencv-python`)
  - NumPy (`pip install numpy`)
  - setproctitle (`pip install setproctitle`)

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
else:
    print("No barcode found")
```

## Supported Barcode Types

- **2D**: QR Code, PDF417, DataMatrix, Aztec, MaxiCode, DotCode
- **1D**: Code128, Code39, Code93, UPC/EAN, Codabar, Code11, MSI
- **Industrial**: ITF-14, Code25, Interleaved 2/5, Telepen
- **Postal**: DataBar, Australian Post, Royal Mail, PostNet

## License

This package contains proprietary Barkoder SDK components. A valid license key is required for operation.

## Support

- **Documentation**: [docs.barkoder.com](https://docs.barkoder.com)
- **Contact**: [barkoder.com/contact](https://barkoder.com/contact)
- **License**: Contact Barkoder for licensing information