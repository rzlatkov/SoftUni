class PhotoAlbum:
    page_size = 4

    def __init__(self, pages):
        self.pages = int(pages)
        self.photos = [[] for _ in range(self.pages)]

    def add_photo(self, label: str):
        for p in range(self.pages):
            if len(self.photos[p]) < 4:
                self.photos[p].append(label)
                return f"{label} photo added successfully on page {p+1} slot {len(self.photos[p])}"
        return "No more free spots"

    def display(self):
        output = ''
        for p in range(self.pages):
            output += '-----------\n'
            if len(self.photos[p]) == 0:
                output += '\n'
            else:
                for i in range(len(self.photos[p])):
                    output += '[] '
                output = output.rstrip()
                output += '\n'
        output += "-----------\n"
        return output

    @staticmethod
    def from_photos_count(photos_count: int):
        inpt = 0

        if photos_count % PhotoAlbum.page_size == 0:
            inpt = photos_count / PhotoAlbum.page_size
            return PhotoAlbum.create(inpt)
        if photos_count <= PhotoAlbum.page_size:
            inpt = 1
            return PhotoAlbum.create(inpt)
        if photos_count % PhotoAlbum.page_size != 0:
            inpt = (photos_count / PhotoAlbum.page_size) + 1
            return PhotoAlbum.create(inpt)

    @classmethod
    def create(cls, inpt):
        return cls(inpt)