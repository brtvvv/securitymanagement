import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox

def run_powershell_command(command):
    """Uruchom polecenie PowerShell."""
    result = os.popen(f"powershell -Command \"{command}\"").read()
    return result.strip()

# Funkcje dla "Ochrona przed wirusami i zagrożeniami"
def toggle_realtime_protection(enable):
    command = f"Set-MpPreference -DisableRealtimeMonitoring {1 - enable}"
    run_powershell_command(command)
    messagebox.showinfo("Sukces", f"Ochrona w czasie rzeczywistym {'włączona' if enable else 'wyłączona'}.")

def toggle_cloud_protection(enable):
    command = f"Set-MpPreference -MAPSReporting {2 if enable else 0}"
    run_powershell_command(command)
    messagebox.showinfo("Sukces", f"Ochrona dostarczania z chmury {'włączona' if enable else 'wyłączona'}.")

# Funkcje dla "Zapora i ochrona sieci"
def toggle_firewall(profile, enable):
    command = f"Set-NetFirewallProfile -Profile {profile} -Enabled {'True' if enable else 'False'}"
    run_powershell_command(command)
    messagebox.showinfo("Sukces", f"Zapora dla {profile} {'włączona' if enable else 'wyłączona'}.")

# Funkcje nawigacji
def show_section(section_frame):
    """Pokaż wybraną sekcję, ukrywając pozostałe."""
    for frame in frames:
        frame.pack_forget()
    section_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Tworzenie aplikacji z ciemnym motywem
app = ttk.Window(themename="darkly")
app.title("Zarządzanie Zabezpieczeniami Windows")
app.geometry("800x600")

# Side menu
menu_frame = ttk.Frame(app, padding=10, bootstyle="secondary")
menu_frame.pack(side="left", fill="y")

ttk.Label(menu_frame, text="Menu", font=("Helvetica", 16), bootstyle="primary").pack(pady=10)

ttk.Button(menu_frame, text="Ochrona przed wirusami", bootstyle="secondary-outline", command=lambda: show_section(virus_frame)).pack(fill="x", pady=5)
ttk.Button(menu_frame, text="Zapora i ochrona sieci", bootstyle="secondary-outline", command=lambda: show_section(firewall_frame)).pack(fill="x", pady=5)

# Sekcja: Ochrona przed wirusami i zagrożeniami
virus_frame = ttk.Frame(app, padding=10)

ttk.Label(virus_frame, text="Ochrona przed wirusami i zagrożeniami", font=("Helvetica", 16)).pack(pady=10)

ttk.Button(virus_frame, text="Włącz ochronę w czasie rzeczywistym", bootstyle="success-outline", command=lambda: toggle_realtime_protection(True)).pack(fill="x", pady=5)
ttk.Button(virus_frame, text="Wyłącz ochronę w czasie rzeczywistym", bootstyle="danger-outline", command=lambda: toggle_realtime_protection(False)).pack(fill="x", pady=5)

ttk.Button(virus_frame, text="Włącz ochronę chmurową", bootstyle="success-outline", command=lambda: toggle_cloud_protection(True)).pack(fill="x", pady=5)
ttk.Button(virus_frame, text="Wyłącz ochronę chmurową", bootstyle="danger-outline", command=lambda: toggle_cloud_protection(False)).pack(fill="x", pady=5)

# Sekcja: Zapora i ochrona sieci
firewall_frame = ttk.Frame(app, padding=10)

ttk.Label(firewall_frame, text="Zapora i ochrona sieci", font=("Helvetica", 16)).pack(pady=10)

ttk.Button(firewall_frame, text="Włącz zaporę dla sieci domeny", bootstyle="success-outline", command=lambda: toggle_firewall("Domain", True)).pack(fill="x", pady=5)
ttk.Button(firewall_frame, text="Wyłącz zaporę dla sieci domeny", bootstyle="danger-outline", command=lambda: toggle_firewall("Domain", False)).pack(fill="x", pady=5)

ttk.Button(firewall_frame, text="Włącz zaporę dla sieci prywatnej", bootstyle="success-outline", command=lambda: toggle_firewall("Private", True)).pack(fill="x", pady=5)
ttk.Button(firewall_frame, text="Wyłącz zaporę dla sieci prywatnej", bootstyle="danger-outline", command=lambda: toggle_firewall("Private", False)).pack(fill="x", pady=5)

ttk.Button(firewall_frame, text="Włącz zaporę dla sieci publicznej", bootstyle="success-outline", command=lambda: toggle_firewall("Public", True)).pack(fill="x", pady=5)
ttk.Button(firewall_frame, text="Wyłącz zaporę dla sieci publicznej", bootstyle="danger-outline", command=lambda: toggle_firewall("Public", False)).pack(fill="x", pady=5)

# Zarządzanie widocznością sekcji
frames = [virus_frame, firewall_frame]
show_section(virus_frame)  # Domyślnie pokazujemy sekcję "Ochrona przed wirusami"

# Start aplikacji
app.mainloop()
