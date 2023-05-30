def alphanumeric(password):
    if len(password) >= 1:
        if " " in password:
            return False
        return True if password.isalnum() else False
    return False
