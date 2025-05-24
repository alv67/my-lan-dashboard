import sqlite3
from contextlib import closing

DB_PATH = 'network.db'

def init_db():
    """Create the database and the devices table if they don't exist."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS devices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    mac TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    assignment TEXT,
                    type TEXT,
                    manufacturer TEXT,
                    device_model TEXT,
                    os TEXT,
                    hostname TEXT,
                    services TEXT,
                    ports TEXT,
                    external_access TEXT,
                    notes TEXT
                )
            ''')

def get_all_devices():
    """Return a list of all devices."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute('SELECT * FROM devices').fetchall()

def get_device(device_id):
    """Return a single device by ID."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute('SELECT * FROM devices WHERE id = ?', (device_id,)).fetchone()

def add_device(data):
    """Insert a new device."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''
                INSERT INTO devices (
                    name, mac, ip, assignment, type,
                    manufacturer, device_model, os, hostname, services,
                    ports, external_access, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['name'], data['mac'], data['ip'], data.get('assignment'),
                data.get('type'), data.get('manufacturer'), data.get('device_model'), data.get('os'),
                data.get('hostname'), data.get('services'), data.get('ports'),
                data.get('external_access'), data.get('notes')
            ))

def update_device(device_id, data):
    """Update an existing device by ID."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('''
                UPDATE devices SET
                    name = ?, mac = ?, ip = ?, assignment = ?, type = ?,
                    manufacturer = ?, device_model = ?, os = ?, hostname = ?, services = ?,
                    ports = ?, external_access = ?, notes = ?
                WHERE id = ?
            ''', (
                data['name'], data['mac'], data['ip'], data.get('assignment'),
                data.get('type'), data.get('manufacturer'), data.get('device_model'), data.get('os'),
                data.get('hostname'), data.get('services'), data.get('ports'),
                data.get('external_access'), data.get('notes'), device_id
            ))

def delete_device(device_id):
    """Delete a device by ID."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        with conn:
            conn.execute('DELETE FROM devices WHERE id = ?', (device_id,))