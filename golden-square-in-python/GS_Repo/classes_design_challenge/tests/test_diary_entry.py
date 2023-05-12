from lib.DiaryEntry import DiaryEntry


"""DiaryEntry contains title and contents"""

def test_diary_entry_contents():
    entry = DiaryEntry("Title 1", "My Contents")
    assert entry.title == "Title 1"
    assert entry.contents == "My Contents"