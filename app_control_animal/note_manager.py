import json
from note import Note
import datetime


class NoteManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_name, "r") as file:
                notes_data = json.load(file)  #считывает полный файл, а не построчко, как loads
                notes = [Note(**note_data) for note_data in notes_data]  #получаем список обьектов
                return notes
        except FileNotFoundError:
            return []

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.file_name, "w") as file:
            json.dump(notes_data, file, indent=4)

    def create_note(self, pet_name, commands, pet_type, pet_class):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(self.notes) + 1, pet_name, commands, pet_type, pet_class, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        return new_note

    def read_notes(self, date_filter=None):
        if date_filter:
            filtered_notes = [
                note for note in self.notes if date_filter in note.timestamp]
        else:
            filtered_notes = self.notes

        for note in filtered_notes:
            print(f"ID: {note.id}")
            print(f"Тип животного: {note.pet_type}")
            print(f"Кличка животного: {note.pet_name}")
            print(f"Команды: {note.commands}")
            print(f"Дата/время создания/изменения: {note.timestamp}\n")

    def view_note_for_edit(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                x1 = {note.id}
                x2 = {note.pet_type}
                x3 = {note.pet_name}
                x4 = {note.pet_class}
                x5 = {note.commands}
                x6 = {note.timestamp}
                return [
                    x1, x2, x3, x4, x5, x6
                ]
    def edit_note(self, note_id, new_commands):
        commands = self.view_note_for_edit(note_id)
        print(f"Добавлено к имеющимся командам: {commands[4]}")
        for note in self.notes:
            if note.id == note_id:
                note.commands = list(commands[4])[0] + ', ' + new_commands
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                return
        print("Животное с указанным ID не найдена.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return
        print("Животное с указанным ID не найдена.")

    def view_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(f"ID: {note.id}")
                print(f"Тип животного: {note.pet_type}")
                print(f"Кличка животного: {note.pet_name}")
                print(f"Класс животного: {note.pet_class}")
                print(f"Команды: {note.commands}")
                print(f"Дата/время создания/изменения: {note.timestamp}")
                return

    def view_note_commands(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                print(f"Команды: {note.commands}")
                return
        print("Заметка с указанным ID не найдена.")

    def view_all_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Тип животного: {note.pet_type}")
            print(f"Кличка животного: {note.pet_name}")
            print(f"Класс животного: {note.pet_class}")
            print(f"Команды: {note.commands}")
            print(f"Дата/время создания/изменения: {note.timestamp}")
            print("-------------------------------")
