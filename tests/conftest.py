import pytest

from app import create_app


@pytest.fixture
def app(request):
    app = create_app()
    with app.app_context():
        yield app
