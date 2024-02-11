class Globals:
    admin = None

    def set_current_admin(self, admin):
        self.admin = admin

    def get_current_admin(self):
        return self.admin
