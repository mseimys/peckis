import io
from unittest.mock import patch, Mock

import pytest
import flask
from flask import url_for

import api


@pytest.mark.options(config={"ALLOWED_EXTENSIONS": {"png"}})
def test_file_extensions(app):
    assert api.allowed_file("something.png") == True
    assert api.allowed_file("something.txt") == False


def test_missing_image_returns_error(client):
    res = client.post(url_for("api.guess"))
    assert res.status_code == 400


def test_correct_image_performs_number_guess(client, monkeypatch):
    file_mock = Mock(filename="image.png")
    mock_request = Mock(files={"image": file_mock})
    mock_guess = Mock(delay=Mock(return_value="TASK-ID"))
    with patch("api.guess_number", mock_guess):
        with patch("api.request", mock_request):
            res = client.post(url_for("api.guess"))
            assert res.status_code == 200
            assert res.json == "TASK-ID"
            file_mock.save.assert_called_once()
