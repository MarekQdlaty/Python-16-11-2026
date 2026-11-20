import tkinter as tk
from tkinter import ttk


def calculate(left: float, operator: str, right: float) -> float:
    if operator == "+":
        return left + right
    if operator == "−":
        return left - right
    if operator == "×":
        return left * right
    if operator == "÷":
        if right == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero.")
        return left / right
    raise ValueError(f"Nieznane działanie: {operator}")


class Calculator:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Kalkulator")
        self.root.resizable(False, False)

        self.display = tk.StringVar(value="0")
        self.first_operand: float | None = None
        self.operator: str | None = None
        self.waiting_for_operand = True

        frame = ttk.Frame(root, padding=12)
        frame.grid()

        display = ttk.Entry(
            frame,
            textvariable=self.display,
            justify="right",
            state="readonly",
            font=("Segoe UI", 20),
            width=16,
        )
        display.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 10))

        buttons: tuple[tuple[str, int, int, int, int], ...] = (
            ("C", 1, 0, 1, 3),
            ("÷", 1, 3, 1, 1),
            ("7", 2, 0, 1, 1),
            ("8", 2, 1, 1, 1),
            ("9", 2, 2, 1, 1),
            ("×", 2, 3, 1, 1),
            ("4", 3, 0, 1, 1),
            ("5", 3, 1, 1, 1),
            ("6", 3, 2, 1, 1),
            ("−", 3, 3, 1, 1),
            ("1", 4, 0, 1, 1),
            ("2", 4, 1, 1, 1),
            ("3", 4, 2, 1, 1),
            ("+", 4, 3, 1, 1),
            ("0", 5, 0, 1, 2),
            (".", 5, 2, 1, 1),
            ("=", 5, 3, 1, 1),
        )

        for label, row, column, rowspan, columnspan in buttons:
            def on_button_press(button_label: str = label) -> None:
                self.press(button_label)

            button = ttk.Button(
                frame,
                text=label,
                command=on_button_press,
            )
            button.grid(
                row=row,
                column=column,
                rowspan=rowspan,
                columnspan=columnspan,
                sticky="nsew",
                padx=3,
                pady=3,
                ipadx=8,
                ipady=8,
            )

        for column in range(4):
            frame.columnconfigure(column, weight=1, uniform="calculator")

    def press(self, value: str) -> None:
        if value.isdigit():
            self._input_digit(value)
        elif value == ".":
            self._input_decimal()
        elif value == "C":
            self._clear()
        elif value in {"+", "−", "×", "÷"}:
            self._choose_operator(value)
        elif value == "=":
            self._calculate_result()

    def _input_digit(self, digit: str) -> None:
        if self.waiting_for_operand or self.display.get() == "0":
            self.display.set(digit)
        else:
            self.display.set(self.display.get() + digit)
        self.waiting_for_operand = False

    def _input_decimal(self) -> None:
        if self.waiting_for_operand:
            self.display.set("0.")
            self.waiting_for_operand = False
        elif "." not in self.display.get():
            self.display.set(self.display.get() + ".")

    def _choose_operator(self, operator: str) -> None:
        if (
            self.operator is not None
            and self.first_operand is not None
            and not self.waiting_for_operand
        ):
            try:
                result = calculate(
                    self.first_operand,
                    self.operator,
                    float(self.display.get()),
                )
            except ZeroDivisionError:
                self._show_division_error()
                return
            self.display.set(format(result, ".12g"))
            self.first_operand = result
        elif self.first_operand is None:
            self.first_operand = float(self.display.get())

        self.operator = operator
        self.waiting_for_operand = True

    def _calculate_result(self) -> None:
        if self.operator is None or self.first_operand is None or self.waiting_for_operand:
            return

        try:
            result = calculate(
                self.first_operand,
                self.operator,
                float(self.display.get()),
            )
        except ZeroDivisionError:
            self._show_division_error()
            return

        self.display.set(format(result, ".12g"))
        self.first_operand = None
        self.operator = None
        self.waiting_for_operand = True

    def _show_division_error(self) -> None:
        self.display.set("Nie można dzielić przez zero")
        self.first_operand = None
        self.operator = None
        self.waiting_for_operand = True

    def _clear(self) -> None:
        self.display.set("0")
        self.first_operand = None
        self.operator = None
        self.waiting_for_operand = True


if __name__ == "__main__":
    window = tk.Tk()
    Calculator(window)
    window.mainloop()
