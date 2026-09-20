CREATE TABLE IF NOT EXISTS signals (id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT NOT NULL,url TEXT,source TEXT,published_at TEXT,topic TEXT,score REAL,confidence TEXT,collected_at TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS idx_signals_topic ON signals(topic);
CREATE INDEX IF NOT EXISTS idx_signals_collected_at ON signals(collected_at);
