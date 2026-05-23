# Edge Filer Monitoring & Management Tool

Python-based monitoring and management framework for CTERA Edge Filers.

## Features

- Edge Filer Monitoring
- Cloud Sync Monitoring
- Dynamic Table Display
- Suspend / Unsuspend Cloud Sync
- Enterprise Project Structure

## Project Structure

```text
EF TOOL/
│
├── collectors/
│   ├── filer_collector.py
│   └── cloud_sync_collector.py
│
├── core/
│   └── connection.py
│
├── display/
│   └── terminal.py
│
├── parsers/
│   ├── filer_parser.py
│   └── sync_parser.py
│
├── services/
│   ├── monitoring_service.py
│   └── cloud_sync_service.py
│
└── main.py
```

## Installation

Clone repository:

```bash
git clone <repo-url>
cd edge-filer-tool
```

Install dependencies:

```bash
pip install cterasdk
```

## Run

```bash
python main.py
```

## Current Capabilities

### Monitoring

- Filer status
- Firmware version
- Connectivity
- Capacity usage
- Cloud sync status

### Cloud Sync

- View sync status
- Suspend sync
- Unsuspend sync