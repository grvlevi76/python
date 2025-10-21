class mammal{
    mammal() {
        System.out.println("mammal class constructor");
    }
    public void walk() {
        System.out.println("mammals going for walk");
    }
}

class Dog extends mammal{
    Dog() {
        System.out.println("dog class constructor");
    }
    public void bark() {
        System.out.println("dog barks");
    }
}

public class check{
    public static void main(String[] args) {
        Dog d = new Dog();

    }
}