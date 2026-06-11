from abc import ABC , abstractmethod    

class NotificationsSender(ABC):

    @abstractmethod 
    def send_notification(self,message: str) -> None:
        pass

class EmailNotificationSender(NotificationsSender):

    def send_notification(self, message):
        print(f'Email message {message}')   

class SMSNotificationSender(NotificationsSender):

    def send_notification(self, message):
        print(f'SMS message {message}')   

class Notificator:
    def __init__(self, notification_sender: NotificationsSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        self.__notification_sender.send_notification(message)

obj = Notificator(EmailNotificationSender())
obj.send('menssagem enviada')


obj2 = Notificator(SMSNotificationSender())
obj2.send('menssagem enviada')