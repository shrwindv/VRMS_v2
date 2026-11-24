import sys
from pathlib import Path

system_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(system_dir))
from pages.database import Database

class Query(Database):
    def __init__(self):
        super().__init__()

    def count_users(self):
        self.cursor.execute("""
            SELECT COUNT(*) FROM users WHERE role != "admin"
        """)
        num = self.cursor.fetchone()
        return num[0]

    def count_vehicles(self):
        self.cursor.execute("""
            SELECT COUNT(*) FROM vehicle
        """)
        num = self.cursor.fetchone()
        return num[0]
    
    def count_unreturned(self):
        self.cursor.execute("""
                SELECT COUNT(*) FROM rental WHERE status = "rented"
        """)
        num = self.cursor.fetchone()
        return num[0]

    def dashboard_tb(self):
        self.cursor.execute("""
            SELECT u.user_id,
                   u.user_fname,
                   u.user_mname,
                   u.user_lname,
                   v.vehicle_id,
                   v.vehicle_name,
                   r.vehicle_id,
                   r.user_id,
                   r.created_at,
                   r.updated_at,
                   r.status
                FROM rental r
            INNER JOIN vehicle v ON v.vehicle_id = r.vehicle_id
            INNER JOIN users u ON u.user_id = r.user_id
            WHERE r.status = 'rented'
            
            LIMIT 11
        """)
        num = self.cursor.fetchall()
        return num