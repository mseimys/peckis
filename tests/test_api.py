from api import allowed_file


def test_file_extensions(app):
    app.config["ALLOWED_EXTENSIONS"] = {"png",}
    assert allowed_file("something.png") == True
    assert allowed_file("something.txt") == False
