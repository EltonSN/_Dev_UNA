class Main {

  public static int le (String dado) {
      Scanner entrada = new Scanner (System.in);
  		System.out.print("Informe " + dado + ": ");
      
      return entrada.nextInt();
  }
 
  public static boolean par (int numero) {
    if (numero % 2 == 0)
       return true;
    else
        return false;
  }  
    
  public static void main(String Args[ ]) {
    int numero = le ("numero");
    
    if ( par(numero) == true )
      System.out.println ("O numero " + numero + " é par" );
    else
      System.out.println ("O numero " + numero + " é impar" );

  }
}
