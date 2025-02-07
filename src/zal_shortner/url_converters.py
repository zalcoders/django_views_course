from utils import get_num_from_shortened_url

class ShortenedUrlSlugConverter:
    regex = "[0-9a-zA-Z]+"

    def to_python(self, value):
        return get_num_from_shortened_url(value)

    def to_url(self, value):
        return  str(value)