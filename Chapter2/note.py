from datetime import datetime

last_id = 0


class Note:
    """Represent a note in the notebook. Match against a
     string in searches and store tags for each note."""

    def __init__(self, memo, tags=""):
        """initialize a note with memo and optional
         space-separated tags. Automatically set the note's
         creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.now()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, search_filter):
        """Determine if this note matches the filter
         text. Return True if it matches, False otherwise.
         Search is case-sensitive and matches both text and
         tags."""
        return search_filter in self.memo or search_filter in self.tags
