# get lyrics
lyrics = open('brokenbricks/lyrics.txt').read()

# preprocess lyrics
def preprocess_lyrics(lyrics: str) -> list:
    '''
    lowercases and tokenizes lyrics

    lyrics: a string of lyrics to be processed
    '''
    lyrics = lyrics.lower().split()
    return lyrics

lyrics = preprocess_lyrics(lyrics)
