# Remote Server Demo Repo

This repo is intentionally simple for a remote server tutorial.

## Files
- `requirements.txt` — minimal packages for notebook demos
- `hello_remote.py` — a tiny Python script to run from the command line
- `long_job.py` — a 3-minute script for `tmux` / background-job demos
- `sample_local_upload.txt` — a small file for upload/download demos

## Quick start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python hello_remote.py
```
