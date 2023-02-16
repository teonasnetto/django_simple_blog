from rolepermissions.roles import AbstractUserRole

class Administrator(AbstractUserRole):
    available_permissions = {
        'can_moderate': True,
        'can_publish': True,
        'can_edit': True,
    }

class Author(AbstractUserRole):
    available_permissions = {
        'can_publish': True,
        'can_edit': True,
    }

class Editor(AbstractUserRole):
    available_permissions = {
        'can_edit': True,
    }

class Guest(AbstractUserRole):
    available_permissions = {}