import json
import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class JsonEditor:
    def __init__(self, master):
        self.master = master
        master.title("JSON Editor")

        # Load JSON data
        with open('config.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        # Create labels and entries
        self.label_date_str = tk.Label(master, text="出款日")
        self.label_date_str.pack()
        self.entry_date_str = tk.Entry(master)
        self.entry_date_str.insert(0, self.data['date_str'])
        self.entry_date_str.pack()

        self.label_days_to_add = tk.Label(master, text="账期")
        self.label_days_to_add.pack()
        self.entry_days_to_add = tk.Entry(master)
        self.entry_days_to_add.insert(0, self.data['days_to_add'])
        self.entry_days_to_add.pack()

        self.label_contract1 = tk.Label(master, text="订单编号")
        self.label_contract1.pack()
        self.entry_contract1 = tk.Entry(master)
        self.entry_contract1.insert(0, self.data['contract1'])
        self.entry_contract1.pack()

        self.label_contract_amount = tk.Label(master, text="订单金额")
        self.label_contract_amount.pack()
        self.entry_contract_amount = tk.Entry(master)
        self.entry_contract_amount.insert(0, self.data['contract_amount'])
        self.entry_contract_amount.pack()

        self.label_factoring_amount = tk.Label(master, text="融资金额")
        self.label_factoring_amount.pack()
        self.entry_factoring_amount = tk.Entry(master)
        self.entry_factoring_amount.insert(0, self.data['factoring_amount'])
        self.entry_factoring_amount.pack()

        self.save_button = tk.Button(master, text="Save", command=self.save)
        self.save_button.pack()

        self.run_button = tk.Button(master, text="生成合同", command=self.run_exe)
        self.run_button.pack()

    def save(self):
        # Update JSON data
        self.data['date_str'] = self.entry_date_str.get()
        self.data['days_to_add'] = int(self.entry_days_to_add.get())
        self.data['contract1'] = self.entry_contract1.get()
        self.data['contract_amount'] = self.entry_contract_amount.get()
        self.data['factoring_amount'] = self.entry_factoring_amount.get()

        # Save JSON data
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)

        messagebox.showinfo("Information","Data saved successfully")

    def run_exe(self):
        subprocess.call(os.path.join(os.getcwd(), "auto_contract.exe"))
        self.master.destroy()

root = tk.Tk()
json_editor = JsonEditor(root)
root.mainloop()
