#!/usr/bin/env python3
"""Prática de ergonomia cognitiva em Python/Tkinter, sem persistência."""

from __future__ import annotations

import sys
import tkinter as tk
from tkinter import ttk


EXPECTED = {
    "predio": ("74", "Prédio B"),
    "categoria": ("K", "Acessório"),
    "local": ("19", "Armário 3"),
    "descricao": ("guarda-chuva azul", "guarda-chuva azul"),
}


def validate_record(values: dict[str, str], mode: str) -> tuple[bool, str, str | None]:
    for field in ("predio", "categoria", "local", "descricao"):
        if not values.get(field, "").strip():
            return False, f"Campo incompleto: {field}. Corrija sem perder os demais dados.", field
    allowed_index = 0 if mode == "A" else 1
    for field, allowed in EXPECTED.items():
        if values[field].strip().casefold() != allowed[allowed_index].casefold():
            return False, f"Revise {field}: a seleção não corresponde ao caso fictício.", field
    return True, "Registro fictício concluído. Confira prédio e armário; nada foi salvo.", None


class ErgonomiaApp(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=18)
        self.master = master
        self.mode = tk.StringVar(value="A")
        self.status = tk.StringVar(value="Nenhuma tentativa registrada.")
        self.entries: dict[str, tk.Widget] = {}
        self.pack(fill="both", expand=True)
        self._build()

    def _build(self) -> None:
        self.master.title("Ergonomia da interação — Python/Tkinter")
        self.master.minsize(700, 500)
        toolbar = ttk.Frame(self)
        toolbar.pack(fill="x", pady=(0, 12))
        ttk.Label(toolbar, text="Condição:").pack(side="left")
        for mode, label in (("A", "A — códigos"), ("B", "B — reconhecimento")):
            ttk.Radiobutton(toolbar, text=label, value=mode, variable=self.mode,
                            command=self.rebuild_form).pack(side="left", padx=8)
        ttk.Button(toolbar, text="Simular interrupção", command=self.interrupt).pack(side="right")
        self.instructions = ttk.Label(self, wraplength=650, justify="left")
        self.instructions.pack(fill="x", pady=(0, 12))
        self.form = ttk.LabelFrame(self, text="Registro interno", padding=14)
        self.form.pack(fill="both", expand=True)
        self.rebuild_form()
        actions = ttk.Frame(self)
        actions.pack(fill="x", pady=12)
        ttk.Button(actions, text="Confirmar registro", command=self.confirm).pack(side="left")
        ttk.Button(actions, text="Limpar", command=self.clear).pack(side="left", padx=10)
        ttk.Label(self, textvariable=self.status, wraplength=650).pack(fill="x")

    def rebuild_form(self) -> None:
        for child in self.form.winfo_children():
            child.destroy()
        self.entries.clear()
        mode_a = self.mode.get() == "A"
        self.instructions.configure(text=(
            "Memorize: prédio B = 74; acessório = K; armário 3 = 19. "
            "Registre um guarda-chuva azul."
            if mode_a else
            "Registre um guarda-chuva azul no Prédio B, categoria Acessório, Armário 3. "
            "As opções permanecem visíveis após interrupção."
        ))
        fields = (
            ("predio", "Prédio/código", ("Prédio A", "Prédio B", "Prédio C")),
            ("categoria", "Categoria/código", ("Acessório", "Documento", "Eletrônico")),
            ("local", "Local/código", ("Armário 1", "Armário 2", "Armário 3")),
            ("descricao", "Descrição", ()),
        )
        for row, (key, label, options) in enumerate(fields):
            ttk.Label(self.form, text=f"{row + 1}. {label}").grid(row=row, column=0, sticky="w", padx=6, pady=8)
            widget: tk.Widget
            if options and not mode_a:
                widget = ttk.Combobox(self.form, values=options, state="readonly")
            else:
                widget = ttk.Entry(self.form)
            widget.grid(row=row, column=1, sticky="ew", padx=6, pady=8)
            self.entries[key] = widget
        self.form.columnconfigure(1, weight=1)
        self.entries["predio"].focus_set()
        self.status.set("Condição alterada. Comece uma nova observação.")

    def values(self) -> dict[str, str]:
        return {key: str(widget.get()) for key, widget in self.entries.items()}  # type: ignore[attr-defined]

    def interrupt(self) -> None:
        self.status.set("Interrupção: o telefone tocou. Conte até cinco e retome do ponto em que estava.")
        self.master.focus_force()

    def confirm(self) -> None:
        ok, message, field = validate_record(self.values(), self.mode.get())
        self.status.set(message)
        if not ok and field:
            self.entries[field].focus_set()

    def clear(self) -> None:
        for widget in self.entries.values():
            if isinstance(widget, ttk.Combobox):
                widget.set("")
            else:
                widget.delete(0, tk.END)  # type: ignore[attr-defined]
        self.entries["predio"].focus_set()
        self.status.set("Campos limpos; nenhuma informação foi persistida.")


def smoke_test() -> None:
    valid_a = {"predio": "74", "categoria": "K", "local": "19", "descricao": "guarda-chuva azul"}
    valid_b = {"predio": "Prédio B", "categoria": "Acessório", "local": "Armário 3", "descricao": "guarda-chuva azul"}
    assert validate_record(valid_a, "A")[0]
    assert validate_record(valid_b, "B")[0]
    assert not validate_record({**valid_b, "predio": "Prédio A"}, "B")[0]
    assert validate_record({**valid_b, "descricao": ""}, "B")[2] == "descricao"
    print("PYTHON_SMOKE_PASS")


if __name__ == "__main__":
    if "--smoke-test" in sys.argv:
        smoke_test()
    else:
        root = tk.Tk()
        ErgonomiaApp(root)
        root.mainloop()
