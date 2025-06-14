# Music Analyzer

This Python project scans a folder of `.mp3` files, extracts metadata, analyzes audio features like tempo and dominant pitch, and visualizes the data in a dashboard.

## Features

- MP3 metadata extraction (title, artist, duration, etc.)
- Tempo (BPM) analysis using `librosa`
- Pitch/key estimation via chroma features
- Dashboard visualization (tempo, genre, pitch distribution)

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt

# How to Use

    Place .mp3 files in a folder.

    Run main.py to generate music_data.json.

    Run dashboard.py to visualize the data.

An example of the visualization:

![Dashboard Example](screenshots/music-analyzer-screenshot.png)