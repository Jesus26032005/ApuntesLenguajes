public class FuncionRecurs {
    
    public static void recursion(int n) {
        if (n==1) {
            System.out.println(n);
        } else {
            recursion(n-1);
            System.err.println(n+ " ");
        }
    }


    public static void main(String[] args) {
        recursion(10);
    }
}
