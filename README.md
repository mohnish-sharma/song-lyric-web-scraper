# song-lyric-web-scraper

A simple web scraper that retrieves song lyrics based on the song requested by the user.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Docker](#docker)

## Features

- Retrieves song lyrics from [www.songlyrics.com](https://www.songlyrics.com).
- Supports user-specified song requests.
- Outputs lyrics in plain text format.

## Requirements

- Python 3.x
- BeautifulSoup4 (install via `pip install beautifulsoup4`)
- Requests (install via `pip install requests`)

## Docker

To run this project using Docker:

1. Build the Docker image:
```console
docker build -t lyrics-scraper .
```

2. Run the Docker container:
```console
docker run -it lyrics-scraper
```
