package Canibal;

public class Buku {
    // Inheritance: Buku adalah subclass dari Object (secara implisit)
    private String judul;
    private String pengarang;
    private int tahunTerbit;

    public Buku(String judul, String pengarang, int tahunTerbit) {
        this.judul = judul;
        this.pengarang = pengarang;
        this.tahunTerbit = tahunTerbit;
    }

    // Getter dan setter untuk atribut judul, pengarang, dan tahunTerbit

    // Polymorphism: overriding toString method
    @Override
    public String toString() {
        return "Buku dengan judul " + judul + ", pengarang " + pengarang + ", tahun terbit " + tahunTerbit;
    }
}
