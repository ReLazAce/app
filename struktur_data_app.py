# ==========================================
# NOTE-TAKING APP DATA STRUCTURE
# ==========================================

from collections import deque
from datetime import datetime

# ==========================================
# CLASS NOTE
# ==========================================

class Note:
    def __init__(self, note_id, title, content):
        self.id = note_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()

        # Doubly linked list (chronological)
        self.prev_chrono = None
        self.next_chrono = None

        # Doubly linked list (alphabetical)
        self.prev_alpha = None
        self.next_alpha = None

        # Multiple tags
        self.tags = []

    def __str__(self):
        return f"[{self.id}] {self.title}"


# ==========================================
# CLASS TAG
# ==========================================

class Tag:
    def __init__(self, name):
        self.name = name
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def __str__(self):
        return self.name


# ==========================================
# NOTE MANAGER
# ==========================================

class NoteManager:
    def __init__(self):

        # Storage note
        self.notes = []

        # Storage tag
        self.tags = {}

        # Circular buffer untuk sync log
        self.sync_log = deque(maxlen=5)

    # ======================================
    # TAMBAH NOTE
    # ======================================

    def add_note(self, note_id, title, content):

        note = Note(note_id, title, content)

        self.notes.append(note)

        self.sync_log.append(
            f"ADD NOTE: {title}"
        )

        return note

    # ======================================
    # TAMBAH TAG KE NOTE
    # ======================================

    def add_tag_to_note(self, note, tag_name):

        # Jika tag belum ada
        if tag_name not in self.tags:
            self.tags[tag_name] = Tag(tag_name)

        tag = self.tags[tag_name]

        # Hubungkan tag ke note
        note.tags.append(tag)

        # Hubungkan note ke tag
        tag.add_note(note)

        self.sync_log.append(
            f"ADD TAG '{tag_name}' TO '{note.title}'"
        )

    # ======================================
    # TAMPILKAN CHRONOLOGICAL
    # ======================================

    def show_chronological(self):

        print("\n=== CHRONOLOGICAL VIEW ===")

        sorted_notes = sorted(
            self.notes,
            key=lambda x: x.created_at
        )

        for note in sorted_notes:
            print(note)

    # ======================================
    # TAMPILKAN ALPHABETICAL
    # ======================================

    def show_alphabetical(self):

        print("\n=== ALPHABETICAL VIEW ===")

        sorted_notes = sorted(
            self.notes,
            key=lambda x: x.title
        )

        for note in sorted_notes:
            print(note)

    # ======================================
    # TAMPILKAN TAG
    # ======================================

    def show_tags(self):

        print("\n=== TAG LIST ===")

        for tag_name, tag in self.tags.items():

            print(f"\nTag: {tag_name}")

            for note in tag.notes:
                print(f" - {note.title}")

    # ======================================
    # TAMPILKAN SYNC LOG
    # ======================================

    def show_sync_log(self):

        print("\n=== RECENT SYNC LOG ===")

        for log in self.sync_log:
            print(log)


# ==========================================
# MAIN PROGRAM
# ==========================================

manager = NoteManager()

# Tambah note
n1 = manager.add_note(1, "Belajar Python", "Materi linked list")
n2 = manager.add_note(2, "Tugas Basis Data", "Normalisasi 3NF")
n3 = manager.add_note(3, "Algoritma", "Stack dan Queue")

# Tambah tag
manager.add_tag_to_note(n1, "Programming")
manager.add_tag_to_note(n1, "Kuliah")

manager.add_tag_to_note(n2, "Database")
manager.add_tag_to_note(n2, "Tugas")

manager.add_tag_to_note(n3, "Programming")

# Tampilkan data
manager.show_chronological()
manager.show_alphabetical()
manager.show_tags()
manager.show_sync_log()