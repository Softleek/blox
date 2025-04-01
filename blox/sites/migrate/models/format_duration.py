from datetime import timedelta
import re

def format_duration_default(raw_default):
    """
    Convert various duration formats to Django-compatible timedelta or HH:MM:SS string.
    Returns either a timedelta object or None if format is invalid.
    """
    if raw_default is None:
        return None

    # If already a timedelta, return as-is
    if isinstance(raw_default, timedelta):
        return raw_default

    # Handle string inputs
    if isinstance(raw_default, str):
        raw_default = raw_default.strip().strip("'\"")

        # Check for empty string
        if not raw_default:
            return None

        # Check if format is already HH:MM:SS
        hh_mm_ss_pattern = re.compile(r'^(\d{1,2}):(\d{1,2}):(\d{1,2})$')
        if hh_mm_ss_pattern.match(raw_default):
            hours, minutes, seconds = map(int, hh_mm_ss_pattern.match(raw_default).groups())
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)

        # Handle "Xh Ym Zs" format (e.g., "1h 30m")
        time_parts = re.findall(r'(\d+)\s*([hms])', raw_default.lower())
        if time_parts:
            total_seconds = 0
            for value, unit in time_parts:
                if unit == 'h':
                    total_seconds += int(value) * 3600
                elif unit == 'm':
                    total_seconds += int(value) * 60
                elif unit == 's':
                    total_seconds += int(value)
            return timedelta(seconds=total_seconds)

        # Handle colon-separated formats
        parts = raw_default.split(':')
        if len(parts) == 3:  # HH:MM:SS
            hours, minutes, seconds = map(int, parts)
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)
        elif len(parts) == 2:  # MM:SS
            minutes, seconds = map(int, parts)
            return timedelta(minutes=minutes, seconds=seconds)

    # Handle numeric inputs (treated as seconds)
    try:
        if isinstance(raw_default, (int, float)) or (isinstance(raw_default, str) and raw_default.isdigit()):
            return timedelta(seconds=int(raw_default))
    except (ValueError, TypeError):
        pass

    return None  # Invalid format


