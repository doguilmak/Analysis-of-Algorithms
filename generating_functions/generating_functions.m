format long
tam = 100;
n = 3;
an = zeros(tam, 1);
an(1) = 0;
an(2) = 1;

while n <= tam
  an(n) = (9 * an(n-1)) - (20 * an(n-2))
  n=n+1;
end

tam = 100;
n = 3;
while n <= tam
  aux = an(n)/an(n-1)
  n=n+1;
end

