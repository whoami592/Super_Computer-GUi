import tkinter as tk
from tkinter import ttk
import random
import time
import threading

class SuperComputerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Supercomputer Interface")
        self.root.geometry("800x600")
        self.root.configure(bg="#0a0a23")

        # Style configuration
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10, "bold"), padding=10)
        self.style.configure("TLabel", font=("Helvetica", 12), background="#0a0a23", foreground="#00ffcc")
        self.style.configure("TProgressbar", thickness=20)

        # Main frame
        self.main_frame = tk.Frame(root, bg="#0a0a23")
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Header
        self.header_label = ttk.Label(self.main_frame, text="Quantum Core Control System", font=("Helvetica", 20, "bold"))
        self.header_label.pack(pady=10)

        # System Status Frame
        self.status_frame = tk.Frame(self.main_frame, bg="#0a0a23", bd=2, relief="ridge")
        self.status_frame.pack(pady=10, fill="x")

        self.cpu_label = ttk.Label(self.status_frame, text="CPU Usage: 0%")
        self.cpu_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_bar = ttk.Progressbar(self.status_frame, length=300, mode="determinate")
        self.cpu_bar.pack(anchor="w", padx=10, pady=5)

        self.memory_label = ttk.Label(self.status_frame, text="Memory Usage: 0%")
        self.memory_label.pack(anchor="w", padx=10, pady=5)
        self.memory_bar = ttk.Progressbar(self.status_frame, length=300, mode="determinate")
        self.memory_bar.pack(anchor="w", padx=10, pady=5)

        self.temp_label = ttk.Label(self.status_frame, text="Core Temperature: 0°C")
        self.temp_label.pack(anchor="w", padx=10, pady=5)

        # Control Panel Frame
        self.control_frame = tk.Frame(self.main_frame, bg="#0a0a23", bd=2, relief="ridge")
        self.control_frame.pack(pady=10, fill="x")

        self.start_button = ttk.Button(self.control_frame, text="Start Core", command=self.start_core)
        self.start_button.pack(side="left", padx=10, pady=10)
        self.stop_button = ttk.Button(self.control_frame, text="Stop Core", command=self.stop_core)
        self.stop_button.pack(side="left", padx=10, pady=10)
        self.diagnostic_button = ttk.Button(self.control_frame, text="Run Diagnostics", command=self.run_diagnostics)
        self.diagnostic_button.pack(side="left", padx=10, pady=10)

        # Console Output
        self.console = tk.Text(self.main_frame, height=8, bg="#1c2526", fg="#00ffcc", font=("Courier", 10))
        self.console.pack(pady=10, fill="x")
        self.console.insert(tk.END, "System Initialized...\n")
        self.console.config(state="disabled")

        # System state
        self.running = False
        self.update_thread = None

    def log_message(self, message):
        self.console.config(state="normal")
        self.console.insert(tk.END, f"{time.strftime('%H:%M:%S')}: {message}\n")
        self.console.see(tk.END)
        self.console.config(state="disabled")

    def start_core(self):
        if not self.running:
            self.running = True
            self.log_message("Quantum Core Starting...")
            self.update_thread = threading.Thread(target=self.update_stats, daemon=True)
            self.update_thread.start()

    def stop_core(self):
        if self.running:
            self.running = False
            self.log_message("Quantum Core Stopping...")
            self.cpu_bar["value"] = 0
            self.memory_bar["value"] = 0
            self.cpu_label.config(text="CPU Usage: 0%")
            self.memory_label.config(text="Memory Usage: 0%")
            self.temp_label.config(text="Core Temperature: 0°C")

    def run_diagnostics(self):
        self.log_message("Running System Diagnostics...")
        self.root.after(2000, lambda: self.log_message("Diagnostics Complete: All Systems Nominal"))

    def update_stats(self):
        while self.running:
            cpu_usage = random.randint(20, 90)
            memory_usage = random.randint(30, 80)
            temperature = random.randint(40, 75)

            self.cpu_bar["value"] = cpu_usage
            self.memory_bar["value"] = memory_usage
            self.cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
            self.memory_label.config(text=f"Memory Usage: {memory_usage}%")
            self.temp_label.config(text=f"Core Temperature: {temperature}°C")

            self.log_message(f"System Update - CPU: {cpu_usage}%, Memory: {memory_usage}%, Temp: {temperature}°C")
            time.sleep(2)

def main():
    root = tk.Tk()
    app = SuperComputerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()