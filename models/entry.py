class Entry():
    
    def __init__(self, id, concept, entry, date, mood_id):
       self.id = id
       self.concept = concept
       self.entry = entry
       self.date = date
       self.mood_id = mood_id
       self.mood = None
       self.tags = []

new_entry = Entry(2, "SQL", "SQL is really hard so far.", "	2022-04-11", 3)