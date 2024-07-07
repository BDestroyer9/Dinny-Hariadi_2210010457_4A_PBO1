package Canibal;

    // Inheritance: Mobil adalah subclass dari Kendaraan
public class Mobil extends kendaraan {
    // Encapsulation: mendeklarasikan atribut sebagai private
    private int tahunProduksi;
    private String warna;

    // Constructor
    public Mobil(String merek, int tahunProduksi, String warna) {
        // Memanggil constructor superclass
        super(merek);
        this.tahunProduksi = tahunProduksi;
        this.warna = warna;
    }

    // Getter dan setter untuk atribut tahunProduksi dan warna

    // Polymorphism: overriding toString method
    @Override
    public String toString() {
        return "Mobil " + getMerek() + " tahun " + tahunProduksi + ", warna " + warna;
    }
}
