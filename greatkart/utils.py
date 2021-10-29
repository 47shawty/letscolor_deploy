def get_current_utc():
    from datetime import datetime, timezone
    return datetime.now(timezone.utc)


def get_filename(filename):
    return filename.upper()
