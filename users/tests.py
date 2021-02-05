def test_user_can_authenticate(client, django_user_model):
    username = "foo1"
    password = "bar1"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.force_login(user)
    assert user.is_authenticated
