# Installation

This guide covers how to install and set up PolicyEngine Ireland for different use cases.

## Prerequisites

- **Python**: Version 3.10 or higher (3.13 recommended)
- **Package Manager**: `uv` (recommended) or `pip`

## Option 1: Install from PyPI (Recommended)

For most users, installing from PyPI is the simplest option:

```bash
pip install policyengine-ie
```

Or using `uv` (faster):

```bash
uv pip install policyengine-ie
```

## Option 2: Development Installation

If you want to contribute to the project or need the latest development version:

### 1. Clone the Repository

```bash
git clone https://github.com/PolicyEngine/policyengine-ie.git
cd policyengine-ie
```

### 2. Install with Development Dependencies

Using the Makefile (recommended):

```bash
make install
```

Or manually:

```bash
uv pip install --system -e .[dev]
```

### 3. Verify Installation

Run the test suite:

```bash
make test
```

## Installation Options

### Core Dependencies

The core installation includes:
- `policyengine-core` - Core microsimulation framework
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `pyyaml` - Parameter file parsing

### Development Dependencies

When installing with `[dev]`, you also get:
- `pytest` - Testing framework
- `black` - Code formatting
- `jupyter-book` - Documentation generation
- `plotly` - Interactive visualizations

## Virtual Environment (Recommended)

We recommend using a virtual environment to avoid conflicts:

### Using venv

```bash
python -m venv policyengine-ie-env
source policyengine-ie-env/bin/activate  # On Windows: policyengine-ie-env\Scripts\activate
pip install policyengine-ie
```

### Using conda

```bash
conda create -n policyengine-ie python=3.13
conda activate policyengine-ie
pip install policyengine-ie
```

## Verify Installation

Test that PolicyEngine Ireland is working correctly:

```python
from policyengine_ie import IrishTaxBenefitSystem

# Create a system
system = IrishTaxBenefitSystem()
print("PolicyEngine Ireland installed successfully!")
print(f"System has {len(system.entities)} entity types")
```

Expected output:
```
PolicyEngine Ireland installed successfully!
System has 5 entity types
```

## Troubleshooting

### Common Issues

**ImportError: No module named 'policyengine_ie'**
- Ensure you've activated the correct virtual environment
- Try reinstalling: `pip uninstall policyengine-ie && pip install policyengine-ie`

**ModuleNotFoundError: No module named 'policyengine_core'**
- The core dependency wasn't installed correctly
- Try: `pip install policyengine-core>=3.19.0`

**Permission denied errors**
- Use `--user` flag: `pip install --user policyengine-ie`
- Or create a virtual environment (recommended)

### Platform-Specific Notes

**Windows**
- Use Windows Subsystem for Linux (WSL) for best compatibility
- Ensure you have Microsoft Visual C++ Build Tools installed

**macOS**
- May need to install Xcode command line tools: `xcode-select --install`

**Linux**
- Most distributions work out of the box
- May need to install `python3-dev` package

## Next Steps

Once installed, check out the [quickstart guide](quickstart.md) to begin using PolicyEngine Ireland.

## System Requirements

- **Memory**: 2GB RAM minimum (4GB recommended)
- **Storage**: 500MB free space
- **Network**: Required for downloading government data updates