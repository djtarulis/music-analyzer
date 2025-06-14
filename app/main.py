import eyed3
import os
import json
import librosa
import numpy as np

folder = input("Enter path to your music folder: ")

music_data = {} # dictionary to hold music metadata

def get_tempo(file_path):
    # Add tempo to the music data
    try:
        y, sr = librosa.load(file_path, sr=None)
        tempo_array, _ = librosa.beat.beat_track(y=y, sr=sr)

        # tempo_array is a numpy.ndarray or float depending on librosa version
        tempo = float(tempo_array)
        return round(tempo, 2)
    except Exception as e:
        print(f"Could not compute tempo for {os.path.basename(file_path)}: {e}")

def get_dominant_pitch(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)
        pitch_index = np.argmax(chroma_mean)
        pitch_classes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return pitch_classes[pitch_index]
    except Exception as e:
        print(f"Could not compute dominant pitch for {os.path.basename(file_path)}: {e}")
        return None

for filename in os.listdir(folder):
    if filename.endswith(".mp3"):
        file_path = os.path.join(folder, filename)
        audiofile = eyed3.load(file_path)

        # Error handling in case metadata is missing
        if audiofile is None or audiofile.tag is None:
            print(f"Could not read metadata for {filename}")
            continue

        title = audiofile.tag.title
        artist = audiofile.tag.artist
        album = audiofile.tag.album
        genre = str(audiofile.tag.genre) if audiofile.tag.genre else "Unknown"
        duration = round(audiofile.info.time_secs, 2)
        tempo = get_tempo(file_path)
        # This gives us a chroma feature matrix showing energy in each of the 12 pitch classes (C, C#, D, ..., B) across time.
        # We’ll then take the mean chroma vector and guess the most dominant pitch class.
        pitch = get_dominant_pitch(file_path)

        # Display metadata
        print("Title:", title)
        print("Artist:", artist)
        print("Album:", album)
        print("Genre:", genre)
        print("Duration:", duration, "seconds")
        print("Tempo:", f"{tempo} BPM" if tempo else "Unknown")
        print("Pitch:", f"{pitch}")
        print("-" * 40)

        # Keep inside loop to accumulate data for all files instead of just the last one
        music_data[filename] = {
            "filename": filename,
            "title": title,
            "artist": artist,
            "album": album,
            "genre": genre,
            "duration": duration,
            "tempo": tempo,
            "pitch": pitch
        }

# Save metadata to a JSON file
with open("music_data.json", "w") as f:
    json.dump(music_data, f, indent = 4)
    print("Saved", len(music_data), "songs to music_data.json")
