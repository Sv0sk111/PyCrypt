from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class Calculator:
    def __init__(self):
        self.price = 0
        self.trimmings_price = 0
        self.cost = 0
        self.amount = 0
        self.gram_amount = 1.0
        self.full_amount = 0
        self.trimmings = 0
        self.profit = 0
        self.money_made = 0

    def calculate_full_amount(self):
        try:
            if self.gram_amount == 1.0:
                self.full_amount = self.amount
                self.trimmings = 0
            else:
                self.full_amount = self.amount / self.gram_amount
                self.trimmings = self.amount * (1.0 - self.gram_amount)
            return True
        except:
            return False

    def calculate_profit(self):
        try:
            part_profit = self.full_amount * self.price
            self.profit = (part_profit + (self.trimmings * self.trimmings_price)) - self.cost
            self.money_made = self.profit + self.cost
            return True
        except:
            return False


class ProfitCalculatorUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        self.calc = Calculator()

        # Title
        self.add_widget(Label(text="Profit Calculator", font_size=24, size_hint=(1, 0.1)))

        # Input fields
        self.entries = {}
        fields = [
            ("Full Price ($)", "price"),
            ("Trimmings Price ($)", "trimmings_price"),
            ("Amount of Product", "amount"),
            ("Cost ($)", "cost"),
            ("Gram Adjustment (0.8-1.0)", "gram_amount"),
        ]

        for label_text, field_name in fields:
            box = BoxLayout(orientation='horizontal', size_hint=(1, None), height=40)
            label = Label(text=label_text, size_hint=(0.5, 1))
            ti = TextInput(multiline=False, input_filter='float', size_hint=(0.5, 1))
            self.entries[field_name] = ti
            box.add_widget(label)
            box.add_widget(ti)
            self.add_widget(box)

        # Buttons
        btn_layout = BoxLayout(size_hint=(1, None), height=50, spacing=20)
        calculate_btn = Button(text="Calculate")
        clear_btn = Button(text="Clear")
        calculate_btn.bind(on_press=self.calculate)
        clear_btn.bind(on_press=self.clear)
        btn_layout.add_widget(calculate_btn)
        btn_layout.add_widget(clear_btn)
        self.add_widget(btn_layout)

        # Results
        self.results_label = Label(text="", font_size=16, size_hint=(1, 0.3))
        self.add_widget(self.results_label)

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(0.7, 0.4))
        popup.open()

    def calculate(self, instance):
        try:
            self.calc.price = float(self.entries["price"].text)
            self.calc.trimmings_price = float(self.entries["trimmings_price"].text)
            self.calc.amount = float(self.entries["amount"].text)
            self.calc.cost = float(self.entries["cost"].text)
            self.calc.gram_amount = float(self.entries["gram_amount"].text)

            if not (0.8 <= self.calc.gram_amount <= 1.0):
                self.show_popup("Error", "Gram adjustment must be between 0.8 and 1.0")
                return

            if self.calc.calculate_full_amount() and self.calc.calculate_profit():
                result_text = (
                    f"Profit: ${self.calc.profit:.2f}\n"
                    f"Money Made: ${self.calc.money_made:.2f}\n"
                    f"Amount: {self.calc.full_amount:.2f}\n"
                    f"Trimmings: {self.calc.trimmings:.2f}"
                )
                self.results_label.text = result_text
            else:
                self.show_popup("Error", "Calculation failed. Check inputs.")
        except ValueError:
            self.show_popup("Error", "Invalid input. Enter numbers only.")

    def clear(self, instance):
        for entry in self.entries.values():
            entry.text = ""
        self.results_label.text = ""


class ProfitCalculatorApp(App):
    def build(self):
        return ProfitCalculatorUI()


if __name__ == '__main__':
    ProfitCalculatorApp().run()
