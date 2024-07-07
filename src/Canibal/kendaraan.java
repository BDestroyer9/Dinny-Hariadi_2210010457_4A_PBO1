package Canibal;

class kendaraan {
    // Encapsulation: mendeklarasikan atribut sebagai private
    private String merek;

    // Constructor
    public kendaraan(String merek) {
        this.merek = merek;
    }

    // Getter
    public String getMerek() {
        return merek;
    }

    // Polymorphism: overriding toString method
    @Override
    public String toString() {
        return "kendaraan dengan merek: " + merek;
    }
}
