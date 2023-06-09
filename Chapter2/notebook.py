from Chapter2.note import Note


class Notebook:

    def __init__(self):
        self.notes = []

    def search(self, search_filter: str):
        """Find all notes that match the given filter
         string."""
        return [note for note in self.notes if note.match(search_filter)]

    def new_note(self, memo, tags="") -> None:
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id: int, memo: str) -> None:
        """"Find the note with the given id and change its memo to the given value."""
        self._find_note_by_id(note_id).memo = memo

    def modify_tags(self, note_id: int, tags: str) -> None:
        """Find the note with the given id and change its tags to the given value."""
        self._find_note_by_id(note_id).tags = tags

    def _find_note_by_id(self, note_id) -> Note | None:
        """Locate the note with the given id."""
        for note in self.notes:
            return note if note.id == note_id else None
