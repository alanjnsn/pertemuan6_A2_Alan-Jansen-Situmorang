nilai= set({3,6,9,2,5,7})
nilai.update([1,4,8,10])
print(f"nilai setelah proses penambahan = {nilai}")
nilai_yang_dihapus= {1,3,4,5,7,8,10}
nilai.difference_update(nilai_yang_dihapus)
print(f"nilai setelah proses penghapusan = {nilai}")

