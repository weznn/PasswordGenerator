import json
import secrets
import string
import os


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def save_password(service, username, password, filename="passwords.json"):
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[service] = {"username": username, "password": password}

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Şifre {service} için kaydedildi.")


def get_password(service, filename="passwords.json"):
    if not os.path.exists(filename):
        print("Şifre dosyası bulunamadı!")
        return None

    with open(filename, "r") as file:
        try:
            data = json.load(file)
            return data.get(service, None)
        except json.JSONDecodeError:
            print("Dosya bozuk!")
            return None


def main():
    while True:
        print("\n1. Şifre oluştur")
        print("2. Şifre kaydet")
        print("3. Şifre al")
        print("4. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            length = int(input("Şifre uzunluğunu girin: "))
            print("Oluşturulan Şifre:", generate_password(length))
        elif choice == "2":
            service = input("Hizmet adını girin: ")
            username = input("Kullanıcı adını girin: ")
            password = input("Şifreyi girin (boş bırakılırsa otomatik oluşturulur): ")
            if not password:
                password = generate_password()
            save_password(service, username, password)
        elif choice == "3":
            service = input("Hizmet adını girin: ")
            credentials = get_password(service)
            if credentials:
                print(f"Kullanıcı Adı: {credentials['username']}")
                print(f"Şifre: {credentials['password']}")
            else:
                print("Hizmet bulunamadı!")
        elif choice == "4":
            break
        else:
            print("Geçersiz seçim, tekrar deneyin!")


if __name__ == "__main__":
    main()