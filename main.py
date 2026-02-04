import json
import os
import time

DATA_FILE = "catatan.json"

catatan = []

def load_data():
    global catatan
    if not os.path.exists(DATA_FILE):
        catatan = []
        return
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                catatan = data
            else:
                catatan = []
    except (json.JSONDecodeError, OSError):
        catatan = []

def save_data():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(catatan, f, ensure_ascii=False, indent=2)
    except OSError:
        print("❌ Gagal menyimpan data ke file.")

def tambah_catatan():
    print("\nTambah catatan belajar 📝")
    mapel = input("Mapel: 📘 ").strip()
    topik = input("Topik: ✍️ ").strip()

    while True:
        durasi_input = input("Durasi belajar (menit): ⏱️ ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("⚠️ Masukkan durasi positif (lebih dari 0).")
                continue
            break
        except ValueError:
            print("⚠️ Durasi harus berupa angka (menit). Silakan coba lagi.")

    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi,
    })
    save_data()
    print("✅ Catatan berhasil ditambahkan.")

def lihat_catatan():
    print("\nDaftar catatan belajar 📖")
    if not catatan:
        print("Belum ada catatan belajar. 😊")
        return

    for i, c in enumerate(catatan, start=1):
        mapel = c.get("mapel", "-")
        topik = c.get("topik", "-")
        durasi = c.get("durasi", 0)
        print(f"{i}. Mapel: {mapel} | Topik: {topik} | Durasi: {durasi} menit")

def total_waktu():
    total = sum(c.get("durasi", 0) for c in catatan)
    print("\nTotal waktu belajar ⏱️")
    if total == 0:
        print("Belum ada durasi tercatat. 😊")
    else:
        print(f"Total: {total} menit ✅")

def ringkasan():
    print("\nRingkasan aktivitas belajar 📊")
    if not catatan:
        print("Belum ada catatan belajar untuk dirangkum. 😊")
        return

    total_sessions = len(catatan)
    total_minutes = sum(c.get("durasi", 0) for c in catatan)
    avg_minutes = total_minutes / total_sessions if total_sessions else 0

    per_mapel = {}
    for c in catatan:
        m = c.get("mapel", "-")
        d = c.get("durasi", 0)
        if m not in per_mapel:
            per_mapel[m] = {"sessions": 0, "minutes": 0}
        per_mapel[m]["sessions"] += 1
        per_mapel[m]["minutes"] += d

    longest = max(catatan, key=lambda x: x.get("durasi", 0))
    shortest = min(catatan, key=lambda x: x.get("durasi", 0))

    print(f"Total sesi: {total_sessions} 📌")
    print(f"Total waktu: {total_minutes} menit ⏱️")
    print(f"Rata-rata durasi per sesi: {avg_minutes:.1f} menit")
    print("\nStatistik per mapel:")
    for m, info in per_mapel.items():
        print(f"- {m}: {info['sessions']} sesi, {info['minutes']} menit total")

    print("\nSesi terpanjang 🔝:")
    print(f"- Mapel: {longest.get('mapel','-')} | Topik: {longest.get('topik','-')} | {longest.get('durasi',0)} menit")
    print("Sesi terpendek 🔽:")
    print(f"- Mapel: {shortest.get('mapel','-')} | Topik: {shortest.get('topik','-')} | {shortest.get('durasi',0)} menit")

def menu():
    print("\n=== Study Log App 📚 ===")
    print("1. Tambah catatan belajar 📝")
    print("2. Lihat catatan belajar 📖")
    print("3. Total waktu belajar ⏱️")
    print("4. Keluar 🚪")
    print("5. Ringkasan & Statistik 📊")

while True:
    # load data on first loop iteration
    try:
        # if catatan already loaded, skip; otherwise load from file
        if not catatan:
            load_data()
    except NameError:
        # load_data not defined yet
        pass
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "5":
        ringkasan()
    elif pilihan == "4":
        save_data()
        print("🙏 Terima kasih, terus semangat belajar! 🎉")
        break
    else:
        print("Pilihan tidak valid ❗")
    # jeda sebelum kembali ke menu
    time.sleep(2)