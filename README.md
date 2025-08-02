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
3. **Configure your license key:**
   ```bash
   # Edit the config.json file
   nano config.json
   
   # Replace YOUR_LICENSE_KEY_HERE with your actual license key
   {
     "app_name": "your-app-name",
     "license_key": "YOUR_ACTUAL_LICENSE_KEY_HERE",
     "description": "Your application description",
     "version": "1.6.0.2"
   }
   ```
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

## 📝 Configuration Setup

### License Configuration

The SDK requires a valid license key. Configure it in the `config.json` file:

```json
{
  "app_name": "my-barcode-app",
  "license_key": "your-actual-license-key-from-barkoder",
  "description": "My barcode scanning application",
  "version": "1.6.0.2"
}
```

⚠️ **Important**: Replace `YOUR_LICENSE_KEY_HERE` with your actual license key from Barkoder.

### Loading Configuration in Code

```python
import json

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize SDK with license from config
from Barkoder import BarkoderSDK
status = BarkoderSDK.initialize(config['license_key'])
print(f"SDK Status: {status}")
```

## 💻 Usage Example

### Complete Example with Configuration

```python
from Barkoder import BarkoderSDK
import cv2
import json

# Load configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

# Initialize SDK with license key from config
status = BarkoderSDK.initialize(config['license_key'])
if status != 0:
    print(f"❌ SDK initialization failed with status: {status}")
    print("Please check your license key in config.json")
    exit(1)

print(f"✅ SDK initialized successfully")
print(f"📱 App: {config['app_name']}")
print(f"🔢 Version: {config['version']}")

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
    print(f"🎯 Decoded: {result['textualData']}")
    print(f"📊 Type: {result['barcodeTypeName']}")
else:
    print("❌ No barcode found")
```

### Error Handling

```python
# Check SDK initialization status
status_codes = {
    0: "Success",
    -1: "Invalid license key",
    -2: "License expired", 
    -3: "Network error",
    -4: "Invalid configuration"
}

status = BarkoderSDK.initialize(license_key)
if status != 0:
    error_msg = status_codes.get(status, f"Unknown error ({status})")
    print(f"SDK Error: {error_msg}")
    # Handle error appropriately
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

## 🔐 License & Getting Started

### Obtaining a License Key

This SDK contains proprietary components and requires a valid license key for operation.

1. **Contact Barkoder** to obtain your license key:
   - Website: [barkoder.com/request-quote](https://barkoder.com/request-quote)
   - Specify your use case and required barcode types

2. **License Types Available**:
   - **Evaluation**: Free trial license for testing
   - **Development**: License for development and testing
   - **Production**: Full commercial license
   - **Enterprise**: Volume licensing with support

3. **What to Specify When Requesting**:
   - Target platform (Linux x86_64/ARM64)
   - Required barcode types (QR, PDF417, Code128, etc.)
   - Expected usage volume
   - Commercial vs non-commercial use

### License Key Setup

Once you receive your license key:

```bash
# Edit the configuration file
nano config.json

# Replace the placeholder with your actual key
{
  "license_key": "your-actual-key-here"
}
```

### Troubleshooting License Issues

**Common license errors:**
- **Status -1**: Invalid license key format
- **Status -2**: License expired or not yet valid
- **Status -3**: Network connectivity issues
- **Status -4**: License doesn't support requested features

**Solutions:**
1. Verify license key is copied correctly (no extra spaces/characters)
2. Check license expiration date with Barkoder
3. Ensure internet connectivity for license validation
4. Contact Barkoder support if issues persist

## 📞 Support

- **Documentation**: [barkoder.com/docs](https://barkoder.com/docs)
- **Contact**: [barkoder.com/contact](https://barkoder.com/contact)
- **Issues**: [Report issues](https://barkoder.com/issues)

## 📜 Version History

See [Releases](../../releases) for detailed version history and download links.
