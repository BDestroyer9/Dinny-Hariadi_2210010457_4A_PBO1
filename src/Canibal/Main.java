package Canibal;

public class Main {
    public static void main(String[] args) {
        Mobil mobil1 = new Mobil("Toyota", 2019, "Merah");
        Mahasiswa mahasiswa1 = new Mahasiswa("Dinny H", 22, "Teknik Informatika");
        Buku buku1 = new Buku("Bandit Bandit Berkelas", "Tere Liye", 2024);

        // Polymorphism: menggunakan metode toString untuk menampilkan informasi objek
        System.out.println(mobil1);
        System.out.println(mahasiswa1);
        System.out.println(buku1);
    }
}
