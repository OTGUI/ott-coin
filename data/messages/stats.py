#!/usr/bin/env python3
"""Show statistics for OTT cheer messages DB."""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cheer_messages.db")

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    total = cur.execute("SELECT COUNT(*) FROM cheer_messages").fetchone()[0]
    print(f"=== 🎯 OTT 오뚜기 응원 메시지 DB 통계 ===\n")
    print(f"📊 총 메시지 수: {total}\n")
    
    print("── 등급별 (Grade) ──")
    for row in cur.execute("SELECT grade, COUNT(*) FROM cheer_messages GROUP BY grade ORDER BY CASE grade WHEN 'common' THEN 1 WHEN 'rare' THEN 2 WHEN 'epic' THEN 3 WHEN 'legendary' THEN 4 WHEN 'mythic' THEN 5 END"):
        icons = {"common": "⚪", "rare": "🔵", "epic": "🟣", "legendary": "🟡", "mythic": "🔴"}
        print(f"  {icons.get(row[0],'?')} {row[0]:12s} : {row[1]:>4d}")
    
    print("\n── 언어별 (Language) ──")
    for row in cur.execute("SELECT language, COUNT(*) FROM cheer_messages GROUP BY language ORDER BY COUNT(*) DESC"):
        flags = {"ko": "🇰🇷", "en": "🇺🇸", "ja": "🇯🇵", "zh": "🇨🇳"}
        print(f"  {flags.get(row[0],'?')} {row[0]:4s} : {row[1]:>4d}")
    
    print("\n── 카테고리별 (Category) ──")
    for row in cur.execute("SELECT category, COUNT(*) FROM cheer_messages GROUP BY category ORDER BY COUNT(*) DESC"):
        print(f"  📌 {row[0]:12s} : {row[1]:>4d}")
    
    print("\n── 등급 × 언어 상세 ──")
    print(f"  {'':12s} {'ko':>6s} {'en':>6s} {'ja':>6s} {'zh':>6s} {'합계':>6s}")
    for grade in ['common', 'rare', 'epic', 'legendary', 'mythic']:
        counts = {}
        for row in cur.execute("SELECT language, COUNT(*) FROM cheer_messages WHERE grade=? GROUP BY language", (grade,)):
            counts[row[0]] = row[1]
        t = sum(counts.values())
        print(f"  {grade:12s} {counts.get('ko',0):>6d} {counts.get('en',0):>6d} {counts.get('ja',0):>6d} {counts.get('zh',0):>6d} {t:>6d}")
    
    conn.close()

if __name__ == "__main__":
    main()
