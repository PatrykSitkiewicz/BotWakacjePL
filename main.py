# --------------------------------
# Name:        BotWakacjePL 3.0
# Author:   Patryk Sitkiewicz
# Created     04 December 2024
# Last update: 11 August 2025
# Python Version:   3.12
# --------------------------------
### Przed użyciem przeczytaj instrukcję w README.md
# Bot przegląda wskazaną stronę wyszukiwania hoteli na portalu Wakacje.pl
# Zapisuje nazwy hoteli wraz z ich aktualnie najniższymi cenami do pliku excel
# następnie w Google sprawdza oceny hoteli i zapisuje je w kolejnej kolumnie
# po zakończeniu pobierania danch tworzy ranking hoteli na podstawie przyznanym im punktów za cenę i ocenę
# ------------------------------------------------------------

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from scraper import scrape_hotels_and_ratings
from ranking import calculate_score
import pandas as pd
import os, sys

def resource_path(relative_path: str) -> str:
    # działa w .exe (PyInstaller) i w trybie developerskim
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

# Konfiguracja stylu
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Główne okno
root = ctk.CTk()
root.title("Wakacje.pl Analyzer")
root.geometry("700x400")
root.resizable(False, False)

# Wczytanie i ustawienie tła
bg_image = Image.open(resource_path("tlo.png")).resize((700, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=700, height=400, highlightthickness=0)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Zmienne globalne
driver_path = tk.StringVar()
save_folder = tk.StringVar()

# --- Funkcje ---

def choose_driver_file():
    selected_file = filedialog.askopenfilename(filetypes=[("ChromeDriver", "chromedriver.exe")])
    if selected_file:
        driver_path.set(selected_file)

def choose_save_folder():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        save_folder.set(selected_dir)

def start_scraping():
    link_template = entry_link.get()
    pages = entry_pages.get()
    chromedriver = driver_path.get()
    folder = save_folder.get()

    if not all([link_template, pages, chromedriver, folder]):
        messagebox.showerror("Błąd", "Uzupełnij wszystkie pola przed rozpoczęciem.")
        return
    if "/?str-2," not in link_template:
        messagebox.showerror(
            "Niepoprawny link",
            "Link musi zawierać fragment '/?str-2,'.\n\nWróć do wyszukiwarki wakacje.pl,\nprzejdź na drugą stronę wyników,\ni wklej tu link z paska adresu."
        )
        return

    try:
        excel_path = os.path.join(folder, "hotele_wakacje.xlsx")
        scrape_hotels_and_ratings(
            wakacje_link_template=link_template,
            num_pages=int(pages),
            chromedriver_path=chromedriver,
            excel_output_path=excel_path
        )
        # Wczytaj dane i oblicz ranking
        df = pd.read_excel(excel_path)
        df_ranked = calculate_score(df)

        # Zapisz zaktualizowany ranking do pliku
        df_ranked.to_excel(excel_path, index=False)
        print("✅ Ranking zapisany do pliku Excel.")
        messagebox.showinfo("Gotowe", f"Wyniki zostały zapisane do:\n{excel_path}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd:\n{e}")


# --- Tooltip class ---
class Tooltip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # bez ramki
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify='left',
                         background="#ffffe0", relief='solid', borderwidth=1,
                         font=("tahoma", 9))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

# --- Tekst instrukcji na Canvasie (100% przezroczystość tła) ---
instrukcja = (
    "Wejdź na stronę wakacje.pl.\n"
    "Wybierz skąd, dokąd i kiedy chcesz pojechać.\n"
    "Wyszukaj dostępne oferty.\n"
    "Możesz skorzystać z filtrów, np. all-inclusive, blisko plaży, itp.\n"
    "Gdy skończysz ustawiać filtry, przejdź na drugą stronę wyników,\n"
    "Następnie skopiuj cały link z przeglądarki i wklej go poniżej:"
)
canvas.create_text(20, 20, anchor="nw", text=instrukcja, fill="black", font=("Arial", 11, "bold"), width=660)

# --- Widżety ---
entry_link = ctk.CTkEntry(root, width=600, fg_color="transparent", border_color="gray", text_color="gray25",
                          placeholder_text="https://www.wakacje.pl/wczasy/kreta/?str-2,samolotem,...")
entry_link.place(x=20, y=140)

canvas.create_text(20, 180, anchor="nw", text="Ile stron wyników mam analizować?", fill="black", font=("Arial", 11, "bold"), width=660)

entry_pages = ctk.CTkComboBox(root, values=[str(i) for i in range(1, 26)], width=60, fg_color="white",
                               border_color="gray", button_color="gray")
entry_pages.set("5")
entry_pages.place(x=290, y=175)

canvas.create_text(20, 222, anchor="nw", text="Wskaż lokalizację pliku chromedriver.exe:", fill="black", font=("Arial", 11, "bold"), width=660)

info_label = tk.Label(root, text="?", fg="red", bg="yellow", font=("Arial", 10))
info_label.place(x=315, y=220)

Tooltip(info_label, "Masz przeglądarkę Google Chrome? Sprawdź w jakiej wersji, np. 318.\nŚciągnij program Chrome Driver tej samej wersji.\nNastępnie wskaż pobrany i wypakowany plik chromedriver.exe")

btn_driver = ctk.CTkButton(root, text="Wybierz plik", command=choose_driver_file, width=120, corner_radius=0)
btn_driver.place(x=360, y=217)

canvas.create_text(20, 260, anchor="nw", text="Wskaż folder, w którym zapisać plik Excel z wynikami analiz:", fill="black", font=("Arial", 11, "bold"), width=660)

btn_save = ctk.CTkButton(root, text="Wybierz folder", command=choose_save_folder, width=120, corner_radius=0)
btn_save.place(x=480, y=255)

btn_start = ctk.CTkButton(root, text="Start", command=start_scraping, width=120, corner_radius=0)
btn_start.place(x=290, y=340)

canvas.create_text(180, 370, anchor="nw", text="Obserwuj okno Chrome i rozwiąż ewentualne Capcha (masz 30 sekund) ", fill="black", font=("Arial", 11), width=660)

root.mainloop()
