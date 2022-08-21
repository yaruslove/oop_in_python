class MailBox:
    def __init__ (self):
        self.inbox_list=list()

    def receive(self):
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        # lst_in=  """sc_lib@list.ru; От Балакирева; Успехов в IT!
        #             mail@list.ru; Выгодное предложение; Вам одобрен кредит.
        #             mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."""
        lst_in=  ["sc_lib@list.ru; От Балакирева; Успехов в IT!", \
            "mail@list.ru; Выгодное предложение; Вам одобрен кредит.", \
            "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить."]
        self.inbox_list=[MailItem(*map(str, t.split("; ")))  for t in lst_in]


class MailItem:
    def __init__ (self,mail_from, title, content):
        self.mail_from=mail_from.strip()
        self.title=title.strip()
        self.content=content.strip()
        self.is_read=False

    def set_read(self, fl_read):
        self.is_read=fl_read
    def __bool__   (self):
        return bool(self.is_read)

    def __repr__ (self):
        return f"cls.MailItem {self.mail_from}"

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)

inbox_list_filtered=list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)