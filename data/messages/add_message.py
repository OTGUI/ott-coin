#!/usr/bin/env python3
"""Add cheer messages to the OTT (오뚜기) database."""
import argparse, csv, sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cheer_messages.db")
VALID_GRADES = {"common", "rare", "epic", "legendary", "mythic"}
VALID_CATEGORIES = {"motivation", "proverb", "humor", "life", "comeback"}
VALID_LANGUAGES = {"ko", "en", "ja", "zh"}

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""CREATE TABLE IF NOT EXISTS cheer_messages (
        id INTEGER PRIMARY KEY,
        grade TEXT NOT NULL,
        category TEXT NOT NULL,
        language TEXT NOT NULL,
        message TEXT NOT NULL,
        source TEXT,
        used_count INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    return conn

def add_one(conn, grade, category, lang, message, source=None):
    assert grade in VALID_GRADES, f"Invalid grade: {grade}"
    assert category in VALID_CATEGORIES, f"Invalid category: {category}"
    assert lang in VALID_LANGUAGES, f"Invalid language: {lang}"
    conn.execute("INSERT INTO cheer_messages (grade, category, language, message, source) VALUES (?,?,?,?,?)",
                 (grade, category, lang, message, source or None))

def import_csv(conn, path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if len(row) < 4: continue
            grade, category, lang, message = row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()
            source = row[4].strip() if len(row) > 4 and row[4].strip() else None
            if grade not in VALID_GRADES or category not in VALID_CATEGORIES or lang not in VALID_LANGUAGES:
                continue
            add_one(conn, grade, category, lang, message, source)
            count += 1
    return count

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Add OTT cheer messages")
    p.add_argument("--grade", choices=sorted(VALID_GRADES))
    p.add_argument("--category", choices=sorted(VALID_CATEGORIES))
    p.add_argument("--lang", choices=sorted(VALID_LANGUAGES))
    p.add_argument("--message")
    p.add_argument("--source", default=None)
    p.add_argument("--import-csv", dest="import_file", help="Import from CSV file")
    args = p.parse_args()
    conn = get_db()
    if args.import_file:
        n = import_csv(conn, args.import_file)
        conn.commit()
        print(f"Imported {n} messages.")
    elif args.grade and args.category and args.lang and args.message:
        add_one(conn, args.grade, args.category, args.lang, args.message, args.source)
        conn.commit()
        print("Added 1 message.")
    else:
        p.print_help()
    conn.close()
