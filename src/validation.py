from datetime import datetime


def validate_required_text(value: str, field_name: str) -> str:
    """
    Validate a required text field.
    Returns the stripped value if valid.
    Raises ValueError if invalid.
    """
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")
    return cleaned


def validate_optional_text(value: str) -> str:
    """
    Validate an optional text field.
    Returns stripped value.
    """
    return value.strip()


def validate_date(date_str: str) -> str:
    """
    Validate strict YYYY-MM-DD date format and impossible dates.
    Returns the cleaned date string if valid.
    Raises ValueError if invalid.
    """
    cleaned = date_str.strip()

    try:
        parsed = datetime.strptime(cleaned, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(
            "Date must be in strict YYYY-MM-DD format and be a real date."
        ) from exc

    return parsed.strftime("%Y-%m-%d")


def validate_event_input(
    name: str,
    date: str,
    location: str,
    description: str = "",
) -> dict[str, str]:
    """
    Validate all event input fields and return normalized values.
    """
    return {
        "name": validate_required_text(name, "Name"),
        "date": validate_date(date),
        "location": validate_required_text(location, "Location"),
        "description": validate_optional_text(description),
    }
