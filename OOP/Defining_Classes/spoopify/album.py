from spoopify.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        found = [s for s in self.songs if s.name == song_name]
        if not found:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(found[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = f"Album {self.name}\n"
        for s in self.songs:
            output += '== ' + s.get_info() + '\n'
        return output
