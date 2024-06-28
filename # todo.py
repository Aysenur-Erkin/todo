def display_menu():
    print("To-Do List Uygulaması")
    print("======================")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Sil")
    print("4. Çıkış")

def add_task(tasks):
    task = input("Yeni Görev: ")
    tasks.append(task)
    print(f"'{task}' görevi eklendi.")

def list_tasks(tasks):
    print("Görevler:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(tasks):
    list_tasks(tasks)
    task_num = int(input("Silinecek Görev Numarası: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"'{removed_task}' görevi silindi.")
    else:
        print("Geçersiz görev numarası.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Seçiminiz: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
