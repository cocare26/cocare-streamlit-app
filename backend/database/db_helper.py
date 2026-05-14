from database import get_connection


def fetch_all(query, params=()):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def execute(query, params=()):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()


# =========================
# Save Chat Log
# =========================
def save_chat_log(row):

    query = """
    INSERT INTO chat_logs (
        timestamp,
        user_id,
        region,
        message,
        language,
        intent,
        intent_confidence,
        sentiment,
        sentiment_score,
        prediction,
        issue_type,
        network_problem,
        notification_type,
        display_channel,
        escalation,
        reason,
        repeat_count,
        area_issue_count
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    params = (
        row.get("timestamp"),
        row.get("user_id"),
        row.get("region"),
        row.get("message"),
        row.get("language"),
        row.get("intent"),
        row.get("intent_confidence"),
        row.get("sentiment"),
        row.get("sentiment_score"),
        row.get("prediction"),
        row.get("issue_type"),
        int(bool(row.get("network_problem"))),
        row.get("notification_type"),
        row.get("display_channel"),
        int(bool(row.get("escalation"))),
        row.get("reason"),
        row.get("repeat_count"),
        row.get("area_issue_count")
    )

    execute(query, params)
