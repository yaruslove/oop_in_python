# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
class Graph:
    def __init__(self,data):
        self.data=data[:]
        self.is_show=bool(True)
    def set_data(self, data):
        self.data=data
    def show_table(self):
        if self.is_show==False:
            print("Отображение данных закрыто")
        else:
            print(" ".join([str(i) for i in self.data]))
    def show_graph(self): # - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
        if self.is_show==False:
            print("Отображение данных закрыто")
        else:
            ned_str="Графическое отображение данных: "
            data_str=" ".join([str(i) for i in self.data])
            print("{}{}".format(ned_str,data_str))
    def show_bar(self): # - для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>");
        if self.is_show==False:
            print("Отображение данных закрыто")
        else:
            ned_str="Столбчатая диаграмма: "
            data_str=" ".join([str(i) for i in self.data])
            print("{}{}".format(ned_str,data_str))
    def set_show(self, fl_show):
        self.is_show=fl_show
  

gr=Graph(data_graph)
              
gr.show_bar()
gr.set_show( fl_show = False)
gr.show_table()