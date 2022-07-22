public class Programme {

    public static void main(String[] args) {
    
    	int tam = 972, n;
		float[] an = new float[tam];
		an[0] = 1;
		an[1] = 1;
		an[2] = 1;

		for (n=4; n < tam; n++) {	        
			an[n] = (9 * an[n / 3]) + n;        
		}
		for (n=0; n < tam; n++)	{
			System.out.println("a["+n+"] = " + an[n]);
		}
    }

}