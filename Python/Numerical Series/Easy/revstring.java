import java.util.Scanner;

public class revstring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str=sc.nextLine();
        String rev="";
        int start=0;
        int end=str.length()-1;
        for(int i=str.length()-1;i>-1;i--){
            rev += str.charAt(i);
        }
        if(rev.equals(str)){
            System.out.println("its palindrome");
        }
        else{

            System.out.println("not a palindrome");
        }
    }
    
}
