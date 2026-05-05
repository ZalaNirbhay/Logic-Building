import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int temp = n;
        int rev = 0;
        while (temp != 0) {
            int lastdigit = temp % 10;
            rev = (rev * 10) + lastdigit;
            temp = temp / 10;
        }
        if (n == rev) {
            System.out.println("the number is palindrome number");
        } else {

            System.out.println("the number is not palindrome number");
        }

    }
}