import sqlite3
import json
from models import Entry, entry
from models.entrytag import EntryTag
from models.mood import Mood
from models.tag import Tag

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
            ON m.id = e.mood_id
        """)
    
        Entries = []
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row ['mood_id'])
            
            mood = Mood(row['id'], row['mood_lable'])
            
            entry.mood = mood.__dict__
            
        #before we get all entries we want too check for tags, 
        #and add them too the entries OR add an empty array to the entry
            db_cursor.execute("""
            SELECT
                t.id,
                t.name
            FROM entries e
            JOIN entrytag et
                ON e.id = et.entry_id
            JOIN tag t
                ON t.id = et.tag_id
            WHERE e.id = ?          
            """, (entry.id, ))
            #tuple has entry id...
            
            #fetch all tags
            tagList = db_cursor.fetchall()
            
            for row in tagList:
                tag = Tag(row['id'], row['name'])
                entry.tags.append(tag.__dict__)
             
             #add tags to the entries    
            Entries.append(entry.__dict__)
    
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
        
        #loop through the tags after adding new entry 
        #w/n loop execute SQL command to INSERT a row to entrytag table 
        for tag in new_entry['tags']:
            
            db_cursor.execute("""
            INSERT INTO EntryTag
                (entry_id, tag_id)
            VALUES
                (?,?);
            """, (id, tag))    
            
    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        UPDATE Entries
            SET
                concept = ?,
                entry = ?,
                date = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId'], id, ))
        
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True