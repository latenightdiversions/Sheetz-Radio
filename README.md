# Sheetz-Radio
Pulls the name of the song currently playing at Sheetz stores and then plays the song.

This project very well may be the most pointless and poorly written code in decades, so if you stumble upon this and have the slightest clue on improvements, don't be afraid to tell us how to improve, or simply submit a pull request.

This project is purely an excuse to learn a little Python and for fun. I do not expect anybody to honestly use this.

Prerequisites:
- Python in a functional Linux/Windows environment (however we cannot be positive it will work in every situation.)
- [python-vlc](https://github.com/oaubert/python-vlc)
- [spotipy](https://github.com/plamere/spotipy)

How to Install:
- Ask yourself, "Do I really want this?", and if the answer is yes, I am truly sorry. Continue reading.
- Install python.
- Install [python-vlc](https://github.com/oaubert/python-vlc) and [spotipy](https://github.com/plamere/spotipy) from a package manager of your choice.
```bash
pip install python-vlc spotipy
```
- Clone the repository.
```bash
git clone https://github.com/roostaa/Sheetz-Radio
```
- Navigate into the newly formed directory.
```bash
cd Sheetz-Radio
```
- Set your environment variables.
```bash
export SPOTIPY_CLIENT_ID='123456...'
export SPOTIPY_CLIENT_SECRET='123456...'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
```
You can get your own API keys on the [Spotify Developer website](https://beta.developer.spotify.com/). Create an account and an non-commercial licensed application. Sheetz-Radio will not work unless there are API keys to communicate with their servers. We are looking into alternative services but Spotify has a web API that is easy enough to use and allows 30 second playback. We know that this is a pain in the ass.

- Run the program.
```bash
python main.py
```

- Pray that nothing explodes.

Completed Tasks:
- Fetch metadata of current song.
- Create a CSV file that tracks songs that have been recently played.
TODO:
- CLI, GUI, and desktop widget versions (Conky maybe?).
- Cross platform support (Linux/Windows/Android...?)
- Ability to stream the song, so that one can experience the feeling of Sheetz in the comfort of their home.

TBD:
- Find a more productive use of our time.
