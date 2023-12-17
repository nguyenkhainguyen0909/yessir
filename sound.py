from pydub import AudioSegment
from pydub.playback import play
song = AudioSegment.from_wav('pacman-original-theme.mp3')
play(song)
