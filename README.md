# Ethiopian-Text-Data-Cleaner

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview
A Python-based tool for cleaning and preprocessing Ethiopian language text data (Amharic, Geez, etc.) for NLP and data analytics projects.

## Features
- Removes unwanted symbols, special characters, and extra spaces
- Normalizes text for consistent formatting
- Supports multiple Ethiopian scripts
- Prepares text for NLP pipelines or analytics workflows

## Tech Stack
- Python  
- Pandas  
- Regex

## Screenshot / Demo
![Cleaner Preview](screenshots/cleaner_preview.png)  

## Usage
```bash
# Clone the repository
git clone https://github.com/Tsion-W/Ethiopian-Text-Data-Cleaner.git
# Install dependencies
pip install -r requirements.txt
# Run the cleaner
python cleaner.py --input input_file.txt --output output_file.txt
