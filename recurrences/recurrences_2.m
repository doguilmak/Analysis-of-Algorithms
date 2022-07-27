format long
tam = 100;
n = 2;
an = zeros(tam, 1);
an(1) = 0;


while n <= tam
  an(n) = an(n - 1) - ((2 * an(n - 1)) / n) + (2 * (1 - (2 * an(n - 1))/ n))
  n=n+1;
end
