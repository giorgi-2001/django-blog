import pytest


@pytest.mark.parametrize(
    "username, email, password1, password2, validity",
    [
        ("TestUser", "user@user.com", "user1234", "user1234", True),
        ("", "user@user.com", "user1234", "user1234", False),
        ("TestUser", "", "user1234", "user1234", False),
        ("TestUser", "user@user.com", "", "user1234", False),
        ("TestUser", "user@user.com", "user1234", "", False), 
        ("TestUser", "user", "user1234", "user1234", False), # invalid email
        ("TestUser", "user@user", "user1234", "", False), # invalid email
        ("TestUser", "user@user.com", "user1234", "user12345", False), # passwords
        ("TestUser", "user@user.com", "user", "user", False), # password
    ]
)
def test_user_registration_form(
    db, register_form_factory, username, email, password1, password2, validity
):
    form = register_form_factory(
        username, email, password1, password2
    )
    assert form.is_valid() is validity
    if form.is_valid():
        user = form.save()
        assert user.username == username
        assert user.email == email
        assert user.check_password(password1)


def test_save_dublicate_users(db, user, register_form_factory):
    form = register_form_factory(
        "TestUser", "user@user.com", "user1234", "user1234"
    )
    with pytest.raises(ValueError):
        form.save()


@pytest.mark.parametrize(
    "username, email, validity", [
        ("TestUser2", "user@gmail.com", True),
        ("", "user@gmail.com", False),
        ("TestUser2", "", False),
        ("TestUser2", "user", False),
        ("TestUser2", "user@gmail", False),
        ("dublicate", "user@gmail.com", False), # dublicate username
        ("TestUser2", "dublicate@user.com", False), # dublicate password
    ]
)
def test_update_user_form(
    db, user, update_form_factory, username, email, validity
):
    form = update_form_factory(username, email)
    assert form.is_valid() is validity

    if form.is_valid():
        updated_user = form.save()
        assert updated_user == user
        assert updated_user.username == username
        assert updated_user.email == email

