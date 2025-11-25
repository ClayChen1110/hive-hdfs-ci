# hive-hdfs

A project combining Python and shell script functionality.

## Project Structure

```
hive-hdfs/
├── .claude/              # Claude-specific project information
├── src/
│   ├── python/          # Python source code
│   └── scripts/         # Shell scripts
├── tests/               # Unit tests
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run setup script
bash src/scripts/setup.sh
```

## Usage

```bash
# Run the main Python application
python src/python/main.py
```

## Testing

```bash
# Run tests
python -m unittest discover tests
```
