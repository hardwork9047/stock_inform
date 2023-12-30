import requests


def send_line_notify(notification_message, image_path):
    """
    LINEに通知する。
    :param notification_message: 送信するメッセージ
    :param image_path: 送信する画像のパス
    """
    line_notify_token = "vFNJYHWr5T3ARqLDbEL6N98Yx8OpQwqjEgxgUQ5lntP"
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"message: {notification_message}"}
    files = {"imageFile": open(image_path, "rb")}
    requests.post(line_notify_api, headers=headers, data=data, files=files)


def send_line_notify_group(notification_message, image_path):
    """
    LINEに通知する。
    :param notification_message: 送信するメッセージ
    :param image_path: 送信する画像のパス
    """
    line_notify_token = "mCMLKYNbN2Abs0bZxhO2hahELqtMJj2RMkVCKjBjjTI"
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_notify_token}"}
    data = {"message": f"message: {notification_message}"}
    files = {"imageFile": open(image_path, "rb")}
    requests.post(line_notify_api, headers=headers, data=data, files=files)


# 使用例
# send_line_notify("テスラの株価チャート", "tesla_stock_price.png")
