"""
Напиши паттерн Builder для Email-сообщения.
Требования:
Продукт: класс Email

Обязательные поля:

to (кому) — список email-адресов
subject (тема)
body (тело письма)

Опциональные поля:

cc (копия) — список email-адресов
bcc (скрытая копия) — список email-адресов
attachments (вложения) — список имён файлов
priority ("low", "normal", "high") — по умолчанию "normal"

Строитель: EmailBuilder

Методы:

add_recipient(email) — добавить получателя (можно вызвать несколько раз)
set_subject(subject) — установить тему
set_body(body) — установить тело письма
add_cc(email) — добавить в копию
add_bcc(email) — добавить в скрытую копию
attach_file(filename) — добавить вложение
set_priority(priority) — установить приоритет
build() — создать объект Email с валидацией

Валидация в build():

Должен быть хотя бы один получатель
Тема не должна быть пустой
Тело письма не должно быть пустым
Priority должен быть один из: "low", "normal", "high"

Метод __str__() в Email:
Должен выводить письмо в читаемом формате.

Добавь класс EmailDirector
Директор должен знать популярные шаблоны писем и создавать их одной командой.
Методы директора:

make_notification(recipient, title, message)
Простое уведомление:

Один получатель
Тема: "Уведомление: {title}"
Тело: сообщение
Приоритет: normal


make_marketing(recipients, campaign_name, content)
Маркетинговое письмо:

Несколько получателей (список)
Тема: "🎉 {campaign_name}"
Тело: контент
Приоритет: low
Примечание в конце тела: "\n\n---\nЧтобы отписаться, нажмите здесь"


make_urgent_alert(recipients, alert_title, alert_body, cc_list=None)
Срочное оповещение:

Несколько получателей
Копии руководителям (если указаны)
Тема: "⚠️ СРОЧНО: {alert_title}"
Тело: alert_body
Приоритет: high


make_report(recipient, report_name, summary, *attachments)
Отчёт с вложениями:

Один получатель
Тема: "Отчёт: {report_name}"
Тело: краткое описание (summary)
Вложения: файлы отчёта
Приоритет: normal

email = (EmailBuilder()
         .add_recipient("ivan@example.com")
         .add_recipient("maria@example.com")
         .set_subject("Важное письмо")
         .set_body("Привет! Это тестовое письмо.")
         .add_cc("boss@example.com")
         .attach_file("report.pdf")
         .set_priority("high")
         .build())

print(email)
```

**Ожидаемый вывод:**
```
To: ivan@example.com, maria@example.com
Cc: boss@example.com
Subject: Важное письмо
Priority: high
Attachments: report.pdf

Привет! Это тестовое письмо.

"""


class Email:
    def __init__(
            self,
            to: list,
            subject: str,
            body: str,
            cc: list | None = None,
            bcc: list | None = None,
            attachments: list | None = None,
            priority: str = "normal",
    ):
        self.to = to
        self.subject = subject
        self.body = body
        self.cc = cc or []
        self.bcc = bcc or []
        self.attachments = attachments or []
        self.priority = priority

    def __str__(self):
        result = f"To: {', '.join(self.to)}\n"

        if self.cc:
            result += f"Cc: {', '.join(self.cc)}\n"
        if self.bcc:
            result += f"Bcc: {', '.join(self.bcc)}\n"

        result += f"Subject: {self.subject}\n"
        result += f"Priority: {self.priority}\n"

        if self.attachments:
            result += f"Attachments: {', '.join(self.attachments)}\n"

        result += f"\n{self.body}\n"
        return result


class EmailBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._to = []
        self._subject = ""
        self._body = ""
        self._cc = []
        self._bcc = []
        self._attachments = []
        self._priority = "normal"
        return self

    def add_recipient(self, email):
        self._to.append(email)
        return self

    def set_body(self, body):
        self._body += body
        return self

    def set_subject(self, subject):
        self._subject = subject
        return self

    def add_cc(self, email):
        self._cc.append(email)
        return self

    def add_bcc(self, email):
        self._bcc.append(email)
        return self

    def attach_file(self, filename):
        self._attachments.append(filename)
        return self

    def set_priority(self, priority):
        self._priority = priority
        return self

    def build(self):
        if not self._to:
            raise ValueError("Field could not be empty")
        if not self._subject:
            raise ValueError("Field could not be empty")
        if not self._body:
            raise ValueError("Field could not be empty")
        if self._priority not in ("low", "normal", "high"):
            raise ValueError("Priority must be low, normal, high")

        email = Email(
            to=self._to,
            subject=self._subject,
            body=self._body,
            cc=self._cc,
            bcc=self._bcc,
            attachments=self._attachments,
            priority=self._priority,
        )

        self.reset()

        return email


class EmailDirector:
    def __init__(self, builder: EmailBuilder):
        self._builder = builder

    def make_notification(self, recipient, title, message):
        return (self._builder
                .add_recipient(recipient)
                .set_subject(f"Уведомление: {title}")
                .set_body(message)
                .build()
                )

    def make_marketing(self, recipients, campaign_name, content):
        for recipient in recipients:
            self._builder.add_recipient(recipient)
        return (self._builder
                .set_subject(f"🎉 {campaign_name}")
                .set_body(content)
                .set_priority("low")
                .set_body("\n\n---\nЧтобы отписаться, нажмите здесь")
                .build()
                )

    def make_urgent_alert(self, recipients, alert_title, alert_body, cc_list=None):
        for recipient in recipients:
            self._builder.add_recipient(recipient)
        if cc_list:
            for recipient in cc_list:
                self._builder.add_cc(recipient)

        return (
            self._builder
            .set_subject(f"⚠️ СРОЧНО: {alert_title}")
            .set_body(alert_body)
            .set_priority("high")
            .build()
        )

    def make_report(self, recipient, report_name, summary, attachments=None):
        if attachments:
            for attachment in attachments:
                self._builder.attach_file(attachment)

        return (
            self._builder
            .add_recipient(recipient)
            .set_subject(report_name)
            .set_body(f"краткое описание ({summary})")
            .build()
        )


if __name__ == '__main__':
    builder = EmailBuilder()
    director = EmailDirector(builder)

    # Тест 1: Уведомление
    print("="*60)
    print("ТЕСТ 1: Уведомление")
    print("="*60)
    email1 = director.make_notification(
        recipient="user@example.com",
        title="Новое сообщение",
        message="У вас новое сообщение в системе"
    )
    print(email1)

    # Тест 2: Маркетинг
    print("="*60)
    print("ТЕСТ 2: Маркетинговая рассылка")
    print("="*60)
    email2 = director.make_marketing(
        recipients=["client1@example.com", "client2@example.com"],
        campaign_name="Скидка 50%",
        content="Только сегодня скидка на все товары!"
    )
    print(email2)

    # Тест 3: Срочное оповещение
    print("="*60)
    print("ТЕСТ 3: Срочное оповещение")
    print("="*60)
    email3 = director.make_urgent_alert(
        recipients=["dev1@example.com", "dev2@example.com"],
        alert_title="Сервер недоступен",
        alert_body="Сервер production упал. Требуется немедленное вмешательство!",
        cc_list=["cto@example.com", "manager@example.com"]
    )
    print(email3)

    # Тест 4: Отчёт с вложениями
    print("="*60)
    print("ТЕСТ 4: Отчёт")
    print("="*60)
    email4 = director.make_report(
        recipient="boss@example.com",
        report_name="Продажи за Q3 2024",
        summary="Общий объём продаж вырос на 25% по сравнению с Q2.",
        attachments=["sales_q3.pdf", "charts.xlsx"]
    )
    print(email4)

    # Тест 5: Проверка, что builder переиспользуется
    print("="*60)
    print("ТЕСТ 5: Повторное использование builder")
    print("="*60)
    email5 = director.make_notification(
        recipient="another@example.com",
        title="Второе письмо",
        message="Builder был сброшен корректно!"
    )
    print(email5)
