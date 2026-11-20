from pywinauto import Desktop

desktop = Desktop(backend="uia")

okno = desktop.window(title="Bez tytułu — Notatnik")

przycisk = okno.child_window(
    title="Dodaj nową kartę",
    control_type="Button"
)

przycisk.click_input()

# okno.child_window(
#     title="Plik",
#     control_type="MenuItem"
# ).click_input()
