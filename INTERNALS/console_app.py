import os

DATA_DIR = "websites"
os.makedirs(DATA_DIR, exist_ok=True)

def search_websites(query):
    found = []
    for fname in os.listdir(DATA_DIR):
        with open(os.path.join(DATA_DIR, fname), "r", encoding="utf8") as f:
            if query.lower() in f.read().lower():
                found.append(fname)
    if not found:
        print("No results found.")
    else:
        print("Found in:")
        for fname in found:
            print(fname)

def create_website():
    title = input("Title: ")
    content = input("HTML Content: ")
    fname = f"{title.replace(' ', '_')}.html"
    with open(os.path.join(DATA_DIR, fname), "w", encoding="utf8") as f:
        f.write(f"<h1>{title}</h1>\n{content}")
    print(f"Website created: {fname}")

def main():
    while True:
        print("1. Search Websites\n2. Create Website\n3. Exit")
        choice = input("Choice: ")
        if choice == "1":
            q = input("Enter search query: ")
            search_websites(q)
        elif choice == "2":
            create_website()
        else:
            break

if __name__ == "__main__":
    main()