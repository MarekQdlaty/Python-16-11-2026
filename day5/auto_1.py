# pyautogui, pywinauto
from pywinauto import Desktop

desktop = Desktop(backend="uia")

for okno in desktop.windows():
    tytul = okno.window_text()

    if tytul:
        print(f"Tytuł: {tytul!r}")
        print(f"Handle: {okno.handle}")
        print("-" * 50)
