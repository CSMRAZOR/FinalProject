import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd

class TransactionLookupApp:
    def __init__(self, root):
        self.root=root
        root.title("Transaction Lookup")

        # Widget for entering a wallet address
        self.address_label = tk.Label(root, text="Enter Wallet Address: ")
        self.address_label.pack()

        self.address_entry = tk.Entry(root)
        self.address_entry.pack()

        # Button to look up transactions
        self.lookup_button = tk.Button(root, text="Lookup Transactions")
        self.lookup_button.pack()

    def lookup_transactions(self):
        try:
            # Read the CSV file 
            file_path = simpledialog.askstring("Input", "Enter the path to your CSV file: ")
            df = pd.read_csv(file_path)

            # Get the wallet address from the user
            entered_adress = self.address_entry.get()

            # Check if the wallet address is valid and in the CSV file
            if entered_adress in df['Wallet Address'].values:
                # Get transactions from the entered wallet address
                transactions = df[df['Wallet Address'] == entered_adress]

                # Display the transactions
                info_message = f"Transactions for Wallet Address: {entered_adress}\n\n"
                for _, transaction in transactions.iterrows():
                    info_message += f"Date: {transaction['Date']}, Amout: {transaction['Amount']}, Description: {transaction['Description']}\n"
                messagebox.showinfo("Transactions", info_message)
            else:
                # Display an error message if no wallet address was found
                messagebox.showerror("error", "Walletaddres was not found in the CSV file.")
        except Exception as e:
            # Display an error if there was a proplem with reading the CSV file
            messagebox.showerror("Error", f"An error occurred:{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransactionLookupApp(root)
    root.mainloop()







