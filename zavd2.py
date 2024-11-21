import os
import shutil

def manage_files():
    source_dir = "Python_docs"
    target_dir = "RESULTS"
    
    os.makedirs(target_dir, exist_ok=True)
    
    if os.path.exists(source_dir):
        files = os.listdir(source_dir)
        print("Вміст каталогу Python_docs:")
        print("\n".join(files))

        for file in files[:2]:
            full_source_path = os.path.join(source_dir, file)
            full_target_path = os.path.join(target_dir, file)
            shutil.copy(full_source_path, full_target_path)
            print(f"Скопійовано файл: {file}")
    else:
        print(f"Каталог {source_dir} не існує.")

manage_files()
