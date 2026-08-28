import sqlite3

DB_PATH = "data/stats.db"

def init_db():
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS command_stats (
                guild_id TEXT NOT NULL,
                author_id TEXT NOT NULL,
                command TEXT NOT NULL,
                count INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (guild_id, author_id, command)
            )
        """)

        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                username TEXT
            )
        """)

        db.execute("""
            CREATE TABLE IF NOT EXISTS guilds (
                guild_id TEXT PRIMARY KEY,
                name TEXT
            )
        """)
        db.execute("""
            INSERT INTO guilds (guild_id, name)
            VALUES ('None', 'DM')
            ON CONFLICT(guild_id) DO NOTHING
        """)


def increment_command(guild_id: str, author_id: str, command: str):
    if not guild_id:
        guild_id = "None"
    
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            INSERT INTO command_stats (guild_id, author_id, command, count)
            VALUES (?, ?, ?, 1)
            ON CONFLICT(guild_id, author_id, command)
            DO UPDATE SET count = count + 1
        """, (guild_id, author_id, command))