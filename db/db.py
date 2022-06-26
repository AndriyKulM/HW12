class UserDB:
    users = [{"name": "test", "email": "test@test.com", "password": "passhash"}]

    def get_all(self):
        return self.users

    def retrieve_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def add(self, name, email, password_hash):        
        for user in self.users:
            if user["email"] != email or user["name"] != name:    # check if user already exists
                user = {
                    "name": name,
                    "email": email,
                    "password": password_hash
                }
                self.users.append(user)
                return user
            return None

    def update_by_email(self, email, name, password):
        # TODO: refactor
        for user in self.users:
            if user["email"] == email:
                user["name"] = name
                user["password"] = password
                user.update()
                return user
            return None

    def delete_by_email(self, email):
        self.users = [user for user in self.users if user["email"] != email]


class BookDB:
    books = [{"name": "Different Seasons", "author": "Stephen King", "ISBN": "9781444723601"}]

    def get_all(self):
        return self.books
