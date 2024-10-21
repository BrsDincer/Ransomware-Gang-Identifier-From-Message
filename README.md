
# Ransomware Gang Identifier From Message

## Overview
This project, **Ransomware Gang Identifier From Message**, is designed to compare a given ransomware message with all messages stored in a database. It utilizes multiple similarity algorithms to determine which ransomware actor or group is most likely responsible for the message.

## Features
- **Sequence-oriented similarity calculation**: Calculates similarity based on sequence matching.
- **Distance-oriented similarity calculation**: Measures similarity using distance-based metrics.
- **Jaccard-oriented similarity calculation**: Compares similarity using the Jaccard index.
- **Comprehensive analysis**: Option to run all similarity calculations at once.

## Usage

### Arguments

- `path` (optional): Provide the path to the ransomware message file to be analyzed. If not specified, the system may prompt for input.
  
- `-s`, `--sequence`: Use sequence-oriented similarity calculation. This flag is optional.
  
- `-d`, `--distance`: Use distance-oriented similarity calculation. This flag is optional.
  
- `-j`, `--jaccard`: Use Jaccard-oriented similarity calculation. This flag is optional.
  
- `-a`, `--all`: Run all available similarity calculation modules in one go. This flag is optional.

### Example Usage
```bash
python .\RGIFM.py /path/to/message.txt --sequence
```
This example runs the tool to identify the ransomware gang using sequence-oriented similarity.

```bash
python .\RGIFM.py --all
```
This example runs all similarity calculation algorithms on the given message.

## Dependencies
- Python 3.x
- Any other relevant libraries

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/BrsDincer/Ransomware-Gang-Identifier-From-Message.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Note
You can add entries to the `ransomware_messages.json` file depending on your goal without breaking the specific format.

## Contributing
Feel free to submit issues or pull requests for new features, bug fixes, or improvements.
