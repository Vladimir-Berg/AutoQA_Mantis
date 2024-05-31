

def test_signup_new_account(app):
    username = 'username2'
    password = 'test'
    app.james.ensure_user_exist(username, password)

