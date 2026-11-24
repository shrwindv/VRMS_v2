import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("rental_system.db")
        self.cursor = self.conn.cursor()
        
        # 1. Users Table (Fixed 'role' check constraint & changed EMAIL to TEXT)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_fname TEXT NOT NULL,
                user_mname TEXT,
                user_lname TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                contact_num TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT CHECK(role IN ('customer', 'admin')) DEFAULT 'customer'
            )
        """)
        
        # 2. Vehicle Table (Changed vehicle_price to REAL for calculations)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehicle (
                vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                code_name TEXT NOT NULL,
                vehicle_name TEXT NOT NULL,
                vehicle_price REAL NOT NULL,
                description TEXT,
                file_name TEXT NOT NULL
            )
        """)
        
        # 3. Rental Table (Fixed AUTOINCREMENT spelling)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rental (
                rent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                vehicle_id INTEGER NOT NULL,
                status TEXT CHECK(status IN('rented', 'returned')) DEFAULT 'rented',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (vehicle_id) REFERENCES vehicle(vehicle_id)
            )
        """)

        
        # 4. Payment Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS payment (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                rental_id INTEGER NOT NULL,
                payment_date TEXT NOT NULL,
                status TEXT CHECK(status IN ('paid', 'pending', 'refunded')) DEFAULT 'pending',
                FOREIGN KEY (rental_id) REFERENCES rental(rent_id)
            )
        """)





        

        # Hardcoded Admin
        self.cursor.execute("""
            INSERT OR IGNORE INTO users (
                user_fname, user_mname, user_lname, username, contact_num, email, address, password, role
            ) VALUES (
                'Sherwin Dave', 'Belleza', 'Parado', 'shrwndave', '09317445560', 'sherwinparado05@gmail.com', 'Headquarters', 'admin123', 'admin'
            )
        """)

        self.cursor.execute("""
            INSERT OR IGNORE INTO users (
                user_fname, user_mname, user_lname, username, contact_num, email, address, password, role
            ) VALUES (
                'Jean Ann', 'M.', 'Abayan', 'jeanann', '0985889', 'jeanannn@gmail.com', 'Headquarters', '123', 'customer'
            )
        """)

        # self.cursor.execute("""
        #     INSERT INTO vehicle (
        #         code_name, vehicle_name, vehicle_price, description, file_name
        #     ) VALUES (
        #         'V001', 'Toyota', 9000.9, 'world hello', 'car1.png'
        #     )
        # """)
        
        # 1. Enable foreign keys
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.cursor.execute("""
            INSERT INTO rental (
                user_id, vehicle_id, status, created_at, updated_at
            ) VALUES (
                2, 2, 'returned', datetime('now'), datetime('now')
            )
        """)
        self.conn.commit()
