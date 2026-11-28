from .database import Database

class Auth_Page(Database):
    def verify_login(self, username, password):
            self.cursor.execute("""
                SELECT user_id, user_fname, role FROM users
                WHERE username = ? AND password = ?
            """, (username, password))
            
            user = self.cursor.fetchone()
            
            if user:
                return user[0]
            else:
                return 0