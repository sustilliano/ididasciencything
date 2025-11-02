# Multi-Source Cosmic Correlation Analysis System

A comprehensive Python-based analysis tool for detecting correlations between gravitational wave events and other cosmic/terrestrial phenomena using real data from multiple scientific sources.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

This system integrates and analyzes data from multiple real-world scientific sources to detect correlations around gravitational wave events. It fetches, processes, and correlates data from:

- **Gravitational Waves**: LIGO/Virgo data via GWOSC (Gravitational Wave Open Science Center)
- **Seismic Activity**: USGS earthquake data
- **Ocean Tides**: NOAA tide measurements
- **Space Weather**: NOAA solar wind, proton flux, x-ray flux, and Kp index
- **Cosmic Rays**: Neutron monitor data from global stations
- **Planetary Positions**: Calculated using Astropy ephemerides

## Features

- Real-time data fetching from multiple scientific APIs
- Automated correlation analysis between different data sources
- Support for major gravitational wave events (GW150914, GW170817, etc.)
- Comprehensive reporting with significance assessments
- JSON and text report generation
- Rate-limited API requests with caching
- Configurable analysis parameters via YAML

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sustilliano/ididasciencything.git
cd ididasciencything
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Configure API keys:
   - NOAA Token: Register at https://www.ncdc.noaa.gov/cdo-web/token
   - NASA API Key: Register at https://api.nasa.gov/

   Edit `real_data_config.yaml` after first run to add your API keys.

## Usage

### Basic Usage

Run analysis for a specific gravitational wave event:

```bash
python rdcs2.py
```

By default, this analyzes the GW170817 neutron star merger event.

### Configuration

The system automatically generates a `real_data_config.yaml` file on first run. You can modify:

- API keys for various data sources
- Detector locations (LIGO Hanford, LIGO Livingston, Virgo)
- Tide station IDs
- Cosmic ray monitoring stations
- Analysis parameters (time windows, correlation thresholds)

Example configuration:
```yaml
analysis_window_hours: 24
correlation_threshold: 0.3
cache_duration_hours: 6
```

### Supported Gravitational Wave Events

- **GW150914**: First detected gravitational wave (binary black hole merger)
- **GW151226**: Binary black hole merger
- **GW170814**: Three-detector observation
- **GW170817**: Neutron star merger with electromagnetic counterpart
- **GW190425**: Neutron star merger
- **GW190521**: Most massive binary black hole merger

### Output

The system generates two output files per analysis:

1. **JSON file** (`real_analysis_[EVENT]_[TIMESTAMP].json`): Detailed structured data including all raw correlations and measurements
2. **Text report** (`real_analysis_report_[EVENT]_[TIMESTAMP].txt`): Human-readable analysis summary with insights and interpretations

## Project Structure

```
ididasciencything/
├── rdcs2.py                    # Main analysis script
├── README.md                   # This file
├── LICENSE                     # GPL v3 license
├── requirements.txt            # Python dependencies
├── CONTRIBUTING.md             # Contribution guidelines
├── .gitignore                 # Git ignore rules
├── real_data_config.yaml      # Configuration file (auto-generated)
└── examples/                  # Sample outputs
    ├── sample_report.txt
    └── sample_data.json
```

## Data Sources & APIs

### Gravitational Wave Data
- **Source**: GWOSC (Gravitational Wave Open Science Center)
- **API**: gwpy library
- **Documentation**: https://www.gw-openscience.org/

### Seismic Data
- **Source**: USGS Earthquake Catalog
- **API**: https://earthquake.usgs.gov/fdsnws/event/1/
- **Rate Limit**: 1 request/second

### Tide Data
- **Source**: NOAA Tides and Currents
- **API**: https://api.tidesandcurrents.noaa.gov/
- **Rate Limit**: 2 requests/second

### Space Weather
- **Source**: NOAA Space Weather Prediction Center
- **API**: https://services.swpc.noaa.gov/json/
- **Rate Limit**: 0.5 requests/second

### Cosmic Ray Data
- **Source**: Neutron Monitor Database (NMDB)
- **Note**: Currently uses realistic synthetic data; full NMDB integration planned

### Planetary Positions
- **Source**: Calculated via Astropy
- **Method**: JPL ephemerides

## Scientific Methodology

The system performs correlation analysis using:

1. **Temporal Correlation**: Detecting time-aligned events across data sources
2. **Spatial Correlation**: Analyzing geographic proximity of phenomena
3. **Statistical Significance**: Calculating confidence scores for correlations
4. **Multi-Source Validation**: Cross-referencing correlations across multiple independent data sources

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this software in your research, please cite:

```
Multi-Source Cosmic Correlation Analysis System
https://github.com/sustilliano/ididasciencything
```

## Acknowledgments

- LIGO Scientific Collaboration and Virgo Collaboration for gravitational wave data
- USGS for seismic data
- NOAA for tide and space weather data
- Neutron Monitor Database for cosmic ray data
- NASA JPL for planetary ephemerides

## Disclaimer

This is a research tool for exploratory data analysis. Correlations detected by this system require rigorous statistical validation and should be interpreted with appropriate scientific caution. This software is provided "as is" without warranty of any kind.

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

## Roadmap

- [ ] Complete NMDB API integration for cosmic ray data
- [ ] Add machine learning for pattern detection
- [ ] Implement longer time-window analysis
- [ ] Add visualization dashboard
- [ ] Support for custom gravitational wave events
- [ ] Docker containerization
- [ ] Automated testing suite
- [ ] Performance optimization for large datasets
