public class Programme {

    public static void main(String[] args) {
    
	int tam = 1000, n;
	float[] an = new float[tam];
	an[0] = 0;
	an[1] = 0;
	an[2] = 0;

	for (n = 3; n < tam; n++) {
	   an[n] = (((n - 3) * an[n - 1]) / n) + 1;
	   System.out.println(an[n]);
	}
		
    }

}
