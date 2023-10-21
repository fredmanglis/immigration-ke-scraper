# Immigration KE Scraper

## Motivation

I am annoyed at the fact that I have to manually scan through the pages provided
on Kenya's immigration site https://immigration.go.ke/ to find out whether or
not my passport has been processed.

It is 2023 for Cthulhu's sake!!! It is ridiculous that anyone has to, in 2023,
manually scan through tabular data, when computers can do this way easier.

This is my attempt to make this easy for myself. If it works for you too, Nice!

## Requirements

Install `tesseract-ocr` with something like:

```sh
sudo apt install tesseract-ocr tesseract-ocr-eng
```

then set up your virtual-env with

```sh
python3 -m venv .venv
```

activate and install the python libraries we need

```sh
source .venv/bin/activate
pip install -r requirements.txt
```

## TODO

- [x] Parse image files into text
- [ ] Attach collection station details to parsed text
- [ ] Save data into SQLite-3 database for easier search
- [ ] Provide script for searching SQLite-3 database
- [ ] Scrape site for images

## Usage

```sh
python3 -m scripts.parse_and_output /path/to/downloaded/image.png
```
