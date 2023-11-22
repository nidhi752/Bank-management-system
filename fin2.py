import tkinter as tk
from tkinter import messagebox
from time import strftime
from PIL import Image, ImageTk

# Placeholder values for user information
user_info = {"username": "", "phone_number": ""}

# Class to manage the finance application
class FinanceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Finance Management")
        self.master.geometry("600x500")

        # Set digital-style background color
        self.master.configure(bg="#001a33")

        # Create and place widgets
        self.title_label = tk.Label(self.master, text=f"Welcome to Finance Management, {user_info['username']}!", font=("Helvetica", 16), pady=10, bg="#001a33", fg="white")
        self.title_label.pack()

        # Account Information
        self.account_info_label = tk.Label(self.master, text=f"Account Holder: {user_info['username']}\nPhone Number: {user_info['phone_number']}", font=("Helvetica", 12), pady=10, bg="#001a33", fg="white")
        self.account_info_label.pack()

        # Clock
        self.clock_label = tk.Label(self.master, font=("Helvetica", 12), pady=10, bg="#001a33", fg="white")
        self.clock_label.pack()
        self.update_clock()

        # Finance Bank Logo\




        # Balance Label
        self.balance_label = tk.Label(self.master, text="Current Balance: $0.00", font=("Helvetica", 12), bg="#001a33", fg="white")
        self.balance_label.pack()

        # Add Money Frame
        self.add_frame = tk.Frame(self.master, bg="#004080", pady=10)  # Darker blue background
        self.add_frame.pack(fill=tk.BOTH, expand=True)

        self.add_label = tk.Label(self.add_frame, text="Add Money:", font=("Helvetica", 12), pady=5, bg="#004080", fg="white")
        self.add_label.pack()

        self.add_entry = tk.Entry(self.add_frame, width=15)
        self.add_entry.pack()

        self.add_button = tk.Button(self.add_frame, text="Add", command=self.add_money, bg="#007acc", fg="white")  # Lighter blue button
        self.add_button.pack()

        # Transfer Money Frame
        self.transfer_frame = tk.Frame(self.master, bg="#0080ff", pady=10)  # Even lighter blue background
        self.transfer_frame.pack(fill=tk.BOTH, expand=True)

        self.transfer_label = tk.Label(self.transfer_frame, text="Transfer Money:", font=("Helvetica", 12), pady=5, bg="#0080ff", fg="white")
        self.transfer_label.pack()

        self.transfer_entry = tk.Entry(self.transfer_frame, width=15)
        self.transfer_entry.pack()

        self.transfer_button = tk.Button(self.transfer_frame, text="Transfer", command=self.transfer_money, bg="#33adff", fg="white")  # Lighter blue button
        self.transfer_button.pack()

        # Withdraw Money Frame
        self.withdraw_frame = tk.Frame(self.master, bg="#0099ff", pady=10)  # Even lighter blue background
        self.withdraw_frame.pack(fill=tk.BOTH, expand=True)

        self.withdraw_label = tk.Label(self.withdraw_frame, text="Withdraw Money:", font=("Helvetica", 12), pady=5, bg="#0099ff", fg="white")
        self.withdraw_label.pack()

        self.withdraw_entry = tk.Entry(self.withdraw_frame, width=15)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(self.withdraw_frame, text="Withdraw", command=self.withdraw_money, bg="#66ccff", fg="white")  # Lighter blue button
        self.withdraw_button.pack()

        # Deposit Frame
        self.deposit_frame = tk.Frame(self.master, bg="#00cc66", pady=10)  # Green background
        self.deposit_frame.pack(fill=tk.BOTH, expand=True)

        self.deposit_label = tk.Label(self.deposit_frame, text="Deposit Money:", font=("Helvetica", 12), pady=5, bg="#00cc66", fg="white")
        self.deposit_label.pack()

        self.deposit_entry = tk.Entry(self.deposit_frame, width=15)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(self.deposit_frame, text="Deposit", command=self.deposit_money, bg="#33ff99", fg="white")  # Lighter green button
        self.deposit_button.pack()

        # Transaction History Frame
        self.history_frame = tk.Frame(self.master, bg="#6600cc", pady=10)  # Purple background
        self.history_frame.pack(fill=tk.BOTH, expand=True)

        self.history_label = tk.Label(self.history_frame, text="Transaction History", font=("Helvetica", 12), pady=5, bg="#6600cc", fg="white")
        self.history_label.pack()

        self.history_text = tk.Text(self.history_frame, height=10, width=40, bg="#9933cc", fg="white")  # Darker purple background
        self.history_text.pack()

        self.history_button = tk.Button(self.master, text="Show History", command=self.show_history, bg="#9900cc", fg="white")  # Dark purple button
        self.history_button.pack()

        # History Tracking
        self.history = []

    def update_clock(self):
        current_time = strftime('%H:%M:%S %p')
        self.clock_label.config(text=current_time)
        self.master.after(1000, self.update_clock)

    def add_money(self):
        try:
            amount = float(self.add_entry.get())
            with open('balance.txt', 'r+') as file:
                try:
                    balance = float(file.read())
                except ValueError:
                    balance = 0.0

                new_balance = balance + amount
                file.seek(0)
                file.write(str(new_balance))
                file.truncate()
                self.balance_label.config(text=f"Current Balance: ${new_balance}")
                self.history.append(f"Added ${amount} to the balance")
        except FileNotFoundError:
            messagebox.showerror("Error", "balance.txt file not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")

    def transfer_money(self):
        try:
            amount = float(self.transfer_entry.get())
            with open('balance.txt', 'r+') as file:
                try:
                    balance = float(file.read())
                except ValueError:
                    balance = 0.0

                if amount > balance:
                    messagebox.showerror("Error", "Insufficient funds!")
                else:
                    new_balance = balance - amount
                    file.seek(0)
                    file.write(str(new_balance))
                    file.truncate()
                    self.balance_label.config(text=f"Current Balance: ${new_balance}")
                    self.history.append(f"Transferred ${amount} from the balance")
        except FileNotFoundError:
            messagebox.showerror("Error", "balance.txt file not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")

    def withdraw_money(self):
        try:
            amount = float(self.withdraw_entry.get())
            with open('balance.txt', 'r+') as file:
                try:
                    balance = float(file.read())
                except ValueError:
                    balance = 0.0

                if amount > balance:
                    messagebox.showerror("Error", "Insufficient funds!")
                else:
                    new_balance = balance - amount
                    file.seek(0)
                    file.write(str(new_balance))
                    file.truncate()
                    self.balance_label.config(text=f"Current Balance: ${new_balance}")
                    self.history.append(f"Withdrew ${amount} from the balance")
        except FileNotFoundError:
            messagebox.showerror("Error", "balance.txt file not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")

    def deposit_money(self):
        try:
            amount = float(self.deposit_entry.get())
            with open('balance.txt', 'r+') as file:
                try:
                    balance = float(file.read())
                except ValueError:
                    balance = 0.0

                new_balance = balance + amount
                file.seek(0)
                file.write(str(new_balance))
                file.truncate()
                self.balance_label.config(text=f"Current Balance: ${new_balance}")
                self.history.append(f"Deposited ${amount} to the balance")
        except FileNotFoundError:
            messagebox.showerror("Error", "balance.txt file not found!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount!")

    def show_history(self):
        self.history_text.delete(1.0, tk.END)  # Clear previous content
        for transaction in self.history:
            self.history_text.insert(tk.END, transaction + "\n")

# Tkinter GUI setup for login
def login():
    entered_username = username_entry.get()
    entered_phone = phone_entry.get()

    # Check if both username and phone number are provided
    if entered_username and entered_phone:
        user_info["username"] = entered_username
        user_info["phone_number"] = entered_phone
        root = tk.Tk()
        app = FinanceApp(root)
        root.mainloop()
    else:
        messagebox.showerror("Login Failed", "Please enter both username and phone number")

# Tkinter GUI setup for login
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x300")

# Title for the login window
title_label = tk.Label(login_window, text="Finance Management Login", font=("Helvetica", 24), pady=10, bg="#001a33", fg="white")
title_label.pack()

username_label = tk.Label(login_window, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_window, font=("Digital-7", 20), width=25)
username_entry.pack()

phone_label = tk.Label(login_window, text="Phone Number:")
phone_label.pack()

phone_entry = tk.Entry(login_window, font=("Digital-7", 20), width=25)
phone_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login, font=("Helvetica", 18), bg="#006bb3", fg="white")  # Darker blue button
login_button.pack(pady=20)

login_window.mainloop()
