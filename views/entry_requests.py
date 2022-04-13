import sqlite3
import json
from models import Entry, entry
from models.mood import Mood

def get_all_entries():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.id mood_id,
            m.lable mood_lable
        FROM entries e
        JOIN mood m 
            ON e.mood_id = m.id
        """)
    
        Entries = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entries = Entry(row['id'], row['concept'], row['entry'], row['date'], row ['mood_id'])
            
            mood = Mood(row['id'], row['mood_lable'])
            
            entries.mood = mood.__dict__
            
            Entries.append(entries.__dict__)
    
    return json.dumps(Entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entries e
        WHERE e.id = ?
        """,( id, ))
        
        data = db_cursor.fetchone()
        
        entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data ['mood_id'])
    
    return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
        
def get_entry_by_search(entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM entries e
        WHERE e.entry LIKE ?
        """, (f"%{entry}%", ))
        #have to use question marks in query, in the tuple part input the thing you want
 
        entries = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row ['mood_id'])
            entries.append(entry.__dict__)
            
    return json.dumps(entries)

def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Entries
            (concept, entry, date, mood_id)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId']))
        
        id = db_cursor.lastrowid
        new_entry['id'] = id
    
    return json.dumps(new_entry)