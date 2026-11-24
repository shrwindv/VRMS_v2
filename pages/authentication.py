from .database import Database

class Auth_Page(Database):
    def verify_login(self, username, password):
            self.cursor.execute("""
                SELECT user_id, user_fname, role FROM users
                WHERE username = ? AND password = ?
            """, (username, password))
            
            user = self.cursor.fetchone()
            
            if user:
                # user[0] = user_id, user[1] = user_fname, user[2] = role
                return True, user[1], user[2], f"Welcome back, {user[2]}!"
            else:
                return False, None, "Invalid username or password."