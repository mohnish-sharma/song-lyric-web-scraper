FROM python:3.9-slim

ADD songLyricScraper.py .

RUN pip install requests beautifulsoup4

CMD ["python3", "./songLyricScraper.py"]