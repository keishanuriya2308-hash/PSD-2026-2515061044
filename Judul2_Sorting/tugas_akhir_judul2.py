def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)

def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    usia = []
    print("Masukkan usia mahasiswa:")
    for i in range(n):
        while True:
            try:
                data = int(input(f"Usia mahasiswa ke-{i+1}: "))
                usia.append(data)
                break
            except ValueError:
                print("Input harus berupa angka!")

    print("\nData sebelum diurutkan:", usia)

    selection_sort(usia, n)

    print("Data setelah diurutkan (Ascending):", end=" ")
    for i in range(n):
        print(usia[i], end=" ")
    print()

if __name__ == "__main__":
    main()