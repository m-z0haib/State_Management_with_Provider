import tkinter as tk
from tkinter import simpledialog, messagebox

# CREATED A DATA MODEL CLASS
class ListItem:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# CREATED A PROVIDER CLASS
class ListProvider:
    def __init__(self):
        self.items = []
        self.id_counter = 1
# ADD FUNCTION
    def add_item(self, name):
        new_item = ListItem(self.id_counter, name)
        self.items.append(new_item)
        self.id_counter += 1
# REMOVE FUNCTION
    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
# UPDATE FUNCTION
    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
# UPDATE FUNCITON
    def update_item(self, item_id, name):
        for item in self.items:
            if item.id == item_id:
                item.name = new_name
                break

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("List Manager")

        self.list_provider = ListProvider()

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        self.listbox.pack(pady=10)

        self.refresh_list()

        add_button = tk.Button(root, text="Add Item", command=self.add_item)
        add_button.pack()

        remove_button = tk.Button(root, text="Remove Selected", command=self.remove_item)
        remove_button.pack()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item in self.list_provider.items:
            self.listbox.insert(tk.END, item.name)

    def add_item(self):
        name = simpledialog.askstring("Add Item", "Enter item name:")
        if name:
            self.list_provider.add_item(name)
            self.refresh_list()

    def remove_item(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            item_name = self.listbox.get(selected_index)
            confirmed = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{item_name}'?")
            if confirmed:
                item_id = self.list_provider.items[selected_index[0]].id
                self.list_provider.remove_item(item_id)
                self.refresh_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
