from textblob import TextBlob
import lyricsgenius as genius

api = genius.Genius("CydEoGc8vKMeEbnj3ZzCcyFcf7dCEd5OMlUGcg1UVNJtviH4y_8h6sz3AWyEluaM")

artists = ["Tyler, The Creator", "Nicki Minaj", "Cardi B", "Drake", "Kendrick Lamar", "Kanye West", "Eminem", "XXXTentacion", "Childish Gambino", "50 Cent"]

WordCounter = 0
ICounter = 0
MeCounter = 0
MyCounter = 0
MineCounter = 0
ThirdPersonCounter = 0

for x in range(len(artists)):
    artist = api.search_artist(artists[x])
    for songs in artist.songs:
        lyrics_special = TextBlob(songs.lyrics)
        wordList = lyrics_special.words
        for word in wordList:
            WordCounter = WordCounter + 1
            if word not in unique_words:
                unique_words.append(word)
                Unique_Word_Counter += 1
            if word == "I" or word == "I'm":
                ICounter += 1
            elif word == "Me" or word == "me":
                MeCounter += 1
            elif word == "My" or word == "my":
                MyCounter += 1
            elif word == "Mine" or word == "mine":
                MineCounter += 1
            elif word in artist.name:
                ThirdPersonCounter += 1
    percentageEgo = ((ICounter + MeCounter + MyCounter + MineCounter + ThirdPersonCounter) / WordCounter) * 100
    print("Artist: {}".format(artist.name))
    print("Number of Words: {}".format(WordCounter))
    print("I/I'm: {}".format(ICounter))
    print("Me: {}".format(MeCounter))
    print("My: {}".format(MyCounter))
    print("Mine: {}".format(MineCounter))
    print("Third Person Reference: {}".format(ThirdPersonCounter))
    print("Percentage of egotistical words: {:.2f}%".format(percentageEgo))
    WordCounter = 0
    ICounter = 0
    MeCounter = 0
    MyCounter = 0
    MineCounter = 0
    ThirdPersonCounter = 0
 
    Unique_Word_Counter = 0
    unique_words = []










