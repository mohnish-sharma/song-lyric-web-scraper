import requests
from bs4 import BeautifulSoup

def get_lyrics(artist, song_title):
    artist = artist.lower().replace(" ", "-")
    song_title_with_dashes = song_title.lower().replace(" ", "-")
    url = f"https://www.songlyrics.com/{artist}/{song_title_with_dashes}-lyrics/"

    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        lyrics_div = soup.find('p', id='songLyricsDiv')
        
        if lyrics_div:
            return lyrics_div.text.strip()
        else:
            return "Lyrics not found for the given song..."
    else:
        return "Failed to retrieve lyrics. Please check the artist and song title..."


artist = input("Enter the artist name: ")
song_title = input("Enter the song title: ")
lyrics = get_lyrics(artist, song_title)
print("****************************** \n\n" + lyrics)
