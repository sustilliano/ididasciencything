# Example Outputs

This directory contains sample outputs from the Multi-Source Cosmic Correlation Analysis System.

## Files

### sample_data.json
Complete JSON output from analyzing the GW170817 gravitational wave event (neutron star merger). Contains:
- Raw correlation data
- Data source metadata
- Significance scores
- Timestamp information

### sample_report.txt
Human-readable analysis report for the GW170817 event. Includes:
- Executive summary
- Data sources analyzed
- Correlations detected
- Scientific interpretation
- Recommended next steps

## Event Details: GW170817

GW170817 was a historic gravitational wave event detected on August 17, 2017. It marked the first observation of a binary neutron star merger with both gravitational wave and electromagnetic counterparts, ushering in the era of multi-messenger astronomy.

**Event Characteristics:**
- **Date**: August 17, 2017
- **Type**: Binary neutron star merger
- **Detectors**: LIGO Hanford, LIGO Livingston, Virgo
- **Distance**: ~130 million light-years
- **Significance**: First multi-messenger observation (gravitational waves + gamma-rays + optical)

## Using These Examples

These files demonstrate the expected format and content of the analysis outputs. You can:

1. **Examine the JSON structure** to understand the data format for programmatic access
2. **Read the text report** to see how results are presented to users
3. **Use as test data** for validating changes to the analysis pipeline
4. **Reference for documentation** when explaining features

## Generating New Examples

To generate fresh analysis outputs:

```bash
python rdcs2.py
```

The system will create new timestamped files in the root directory, which can be compared against these examples.
