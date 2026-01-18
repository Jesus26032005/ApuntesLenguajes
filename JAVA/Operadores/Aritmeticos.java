public class Aritmeticos {
    public static void main(String[] args) {
        //OPERADORES ARITMETICOS
        float numero1=3,numero2=2;
        float suma=numero1+numero2;
        float resta=numero1-numero2;
        float multiplicacion=numero1*numero2;
        float division=(numero1/numero2);
        float modulo=numero1%numero2;

        System.out.println("El resultado de la suma es:" + suma);
        System.out.println("El resultado de la resta es:" + resta);
        System.out.println("El resultado de la multiplicacion es: "+ multiplicacion);
        System.out.printf("El resultado de la divisio es %.2f%n ",division);
        System.out.println("El modulo de la division es: " + modulo);

        //OPERADORES UNARIOS
        int numero3=+10,numero4=-10;
        System.out.println("El valor de la variable numero3 es: " + numero3+ "El del otro es" + numero4);
        int preincremento=++numero3, postincremento=numero3++;
        System.out.println("El valor con preincremento es " + preincremento + " y el postincremento es " + postincremento);
        int predecremento=--numero4, postdecremento=numero4--;
        System.out.println("El valor con predecremento es " + predecremento + " y el decremento es" + postdecremento);
        boolean x = true;
        System.out.println("Negación lógica: " + (!x)); 

        //OPERADORES DE ASIGNACION
        float a=10,b=20;
        a+=b;
        System.out.println("El valor de a es : " + a);
        a-=b;
        System.out.println("El valor de a es : " + a);
        a*=b;
        System.out.println("El valor de a es : " + a);
        a/=b;
        System.out.println("El valor de a es : " + a);
        a%=b;
        System.out.println("El valor de a es : " + a);

        //OPERADORES DE COMPARACION
        System.out.println("El valor de num1 es igual que num2: " + (a==b));
        System.out.println("El valor de num1 es distinto que num2: " + (a!=b));
        System.out.println("El valor de num1 es mayor que num2: " + (a>b));
        System.out.println("El valor de num1 es menor que num2: " + (a<b));
        System.out.println("El valor de num1 es mayor o igual que num2: " + (a>=b));
        System.out.println("El valor de num1 es menor o igual que num2: " + (a<=b));

        //OPERADORES LOGICOS
        boolean isReal=true ,isFalso=false;
        System.out.println("El valor usando el operador and es"+ (isReal && isFalso));
        System.out.println("El valor usando el operador or es"+ (isReal && isFalso));
        System.out.println("El valor usando el operador not es"+ (!isFalso));
    }
}
