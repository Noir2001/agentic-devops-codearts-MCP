from app.main import add, calculate_total, health


def test_add():
    assert add(2, 3) == 5


def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60


def test_health():
    result = health()
    assert result["status"] == "ok"
    assert result["service"] == "Agentic DevOps Demo"
