package Canibal;

public class Mahasiswa {
    private String nama;
    private int umur;
    private String jurusan;

    public Mahasiswa(String nama, int umur, String jurusan) {
        this.nama = nama;
        this.umur = umur;
        this.jurusan = jurusan;
    }

    // Getter dan setter untuk atribut nama, umur, dan jurusan

    // Polymorphism: overriding toString method
    @Override
    public String toString() {
        return "Mahasiswa bernama " + nama + ", berumur " + umur + " tahun, jurusan " + jurusan;
    }
}
