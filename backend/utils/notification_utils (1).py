def send_notification(notification_type: str, payload: dict):
    if notification_type == "none":
        return False

    print(f"[NOTIFICATION] type={notification_type}")
    print(f"[PAYLOAD] {payload}")

    return True
