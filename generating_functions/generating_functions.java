public class Programme {

	public static void main(String[] args) {

		int tam = 100, n;
		float[] an = new float[tam];
		float aux;
		an[0] = 0;
		an[1] = 1;

		for (n = 2; n < tam; n++)   {	        
			an[n] = (9 * an[n - 1]) - (20 * an[n - 2]);

			if (n>=2 && n <= 100)	{
				System.out.println("a["+n+"] = " + an[n]);
			}	        
		}

		for (n = 2; n < tam; n++)   {	        
			aux=(float)an[n]/an[n-1];

			if (n>=2 && n <= 100)	{
			System.out.println("aux["+n+"] = " + aux);
			}	        
	    	}
	
	}
}
