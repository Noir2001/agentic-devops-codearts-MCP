"""Small demo application for the CodeArts Agent PoC."""

APP_NAME = "Agentic DevOps Demo"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def calculate_total(items: list[float]) -> float:
    """Return the total of all items."""
    return sum(items)


def health() -> dict[str, str]:
    """Return a simple health response."""
    return {"status": "ok", "service": APP_NAME}


if __name__ == "__main__":
    print(health())
    print("2 + 3 =", add(2, 3))
