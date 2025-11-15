from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"📧 Email отправлен: {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"📱 SMS отправлен: {message}")


class PushSender(NotificationSender):
    def send(self, message: str):
        print(f"🔔 Push уведомление отправлено: {message}")


class TelegramSender(NotificationSender):
    def send(self, message: str):
        print(f"✈️ Telegram сообщение отправлено: {message}")


class Application(ABC):
    @abstractmethod
    def create_notification_sender(self) -> NotificationSender:
        pass

    def notify(self, message: str):
        sender = self.create_notification_sender()
        sender.send(message)


class UserApp(Application):
    def create_notification_sender(self) -> NotificationSender:
        return EmailSender()


class AdminApp(Application):
    def create_notification_sender(self) -> NotificationSender:
        return SMSSender()


if __name__ == '__main__':
    user_app = UserApp()
    user_app.notify("Добро пожаловать!")
    admin_app = AdminApp()
    admin_app.notify("Система требует внимания!")
