public class Programme {

    public static void main(String[] args) {
    
	int tam = 100, n;
	float[] an = new float[tam];
	an[0] = 0;

	for (n = 1; n < tam; n++) {
		an[n] = an[n - 1] - ((2 * an[n - 1]) / n) + (2 * (1 - (2 * an[n - 1])/ n));
	   System.out.println(an[n]);
	}
	
	System.out.println("a[99] = " + an[99]);
    
    }
}