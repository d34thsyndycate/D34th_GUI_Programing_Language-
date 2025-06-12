import tkinter as tk
from tkinter import filedialog, scrolledtext

v, f = {}, {}

def parse_line(l):
    l = l.lower().strip()
    if not l: return True
    if l.startswith("set karo") and ":" in l: return True
    if l.startswith("pucho "): return True
    if l.startswith("agar") and "toh" in l: return True
    if l.startswith("nahi toh"): return True
    if l.startswith("jab tak") and "tab tak" in l: return True
    if l.startswith("banao function"): return True
    if l.startswith("chalao function"): return True
    if any(op in l for op in "+-*/"): return True
    if l in ["mac address badlo", "scan chalu kar", "fake ip lagao"]: return True
    return False

def run(l, c, L=None, i=0):
    t = parse_line(l)
    if not t:
        c.insert(tk.END, f"[❌] Error: '{l}'\n")
        return
    else:
        c.insert(tk.END, f"[✅] Line OK: '{l}'\n")

def run_script(s, c):
    c.delete("1.0", tk.END)
    L = s.strip().split('\n')
    for line in L:
        run(line.strip(), c)

def check_live(editor, console):
    console.delete("1.0", tk.END)
    L = editor.get("1.0", tk.END).strip().split('\n')
    for line in L:
        run(line.strip(), console)
    editor.after(1000, lambda: check_live(editor, console))  # check every 1 sec

def start_gui():
    w = tk.Tk(); w.title("💀 D34TH Lang v6.0"); w.geometry("800x600")
    editor = scrolledtext.ScrolledText(w, font=("Consolas", 12)); editor.pack(fill=tk.BOTH, expand=1)
    console = scrolledtext.ScrolledText(w, height=10, bg="black", fg="lime", font=("Courier",11)); console.pack(fill=tk.X)

    tk.Button(w, text="🗂 Load", command=lambda: editor.insert("1.0", open(filedialog.askopenfilename(), encoding="utf-8").read())).pack(side=tk.LEFT, padx=5)
    tk.Button(w, text="💾 Save", command=lambda: open(filedialog.asksaveasfilename(defaultextension=".d34th"),"w",encoding="utf-8").write(editor.get("1.0", tk.END))).pack(side=tk.LEFT)
    tk.Button(w, text="▶️ Run", command=lambda: run_script(editor.get("1.0", tk.END), console)).pack(side=tk.RIGHT, padx=10)

    check_live(editor, console)
    w.mainloop()

if __name__ == "__main__": start_gui()
