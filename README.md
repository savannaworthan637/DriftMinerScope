# DriftMinerScope

DriftMinerScope scans historical log or metric archives to detect behavioral drifts and abnormal trend changes across time windows.

## Features
- Loads time-series logs or JSONL events.
- Applies statistical and threshold drift tests.
- Highlights change windows with scoring.
- Matplotlib visual output for analysis.

## Usage
```bash
git clone https://github.com/your-org/DriftMinerScope.git
cd DriftMinerScope
python driftminer/analyzer.py logs/events.jsonl
