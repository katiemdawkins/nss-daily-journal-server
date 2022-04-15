import sqlite3
import json

from models.entrytag import EntryTag

def get_all_entrytags():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.entry_id,
            e.tag_id
        FROM entrytag e
        """)
        
        entrytags=[]
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entrytag=EntryTag(row['id'], row['entry_id'], row['tag_id'])
            entrytags.append(entrytag.__dict__)
            
    return json.dumps(entrytags)