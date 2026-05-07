def binary_search(arr, n, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        print(f"Cek indeks ke-{mid}, nilai = {arr[mid]}")

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def main():
    n = int(input("Masukkan jumlah elemen array: "))
    arr = []

    print("Masukkan elemen secara urut menaik:")
    for i in range(n):
        nilai = int(input(f"Data ke-{i+1}: "))
        arr.append(nilai)

    target = int(input("Masukkan angka yang dicari: "))

    hasil = binary_search(arr, n, target)

    if hasil != -1:
        print(f"Data ditemukan pada indeks ke-{hasil}")
    else:
        print("Data tidak ditemukan")


if __name__ == "__main__":
    main()