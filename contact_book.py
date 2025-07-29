import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone number are required!")
        return

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    messagebox.showinfo("Success", f"Contact '{name}' added!")
    clear_entries()
    update_contact_list()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def update_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name, info in contacts.items():
        listbox_contacts.insert(tk.END, f"{name} - {info['Phone']}")

def search_contact():
    query = entry_search.get().strip().lower()
    listbox_contacts.delete(0, tk.END)
    for name, info in contacts.items():
        if query in name.lower() or query in info['Phone']:
            listbox_contacts.insert(tk.END, f"{name} - {info['Phone']}")

def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected.")
        return

    contact_line = listbox_contacts.get(selected[0])
    name = contact_line.split(" - ")[0]
    
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
        update_contact_list()

def update_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected.")
        return

    contact_line = listbox_contacts.get(selected[0])
    name = contact_line.split(" - ")[0]

    if name in contacts:
        new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contacts[name]["Phone"])
        new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contacts[name]["Email"])
        new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contacts[name]["Address"])

        contacts[name] = {"Phone": new_phone, "Email": new_email, "Address": new_address}
        messagebox.showinfo("Updated", f"Contact '{name}' updated.")
        update_contact_list()

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

tk.Button(root, text="Add Contact", command=add_contact, bg="lightblue").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="orange").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="red").pack(pady=5)

tk.Label(root, text="Search by Name or Phone").pack(pady=5)
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact, bg="lightgreen").pack(pady=5)

tk.Label(root, text="Contact List").pack(pady=5)
listbox_contacts = tk.Listbox(root, width=50)
listbox_contacts.pack(pady=10)

root.mainloop()
