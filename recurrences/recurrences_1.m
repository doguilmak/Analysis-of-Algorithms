tam = 1000;
n = 2;
an = zeros(tam, 1);
an(1) = 0;
an(2) = 0;
an(3) = 0;

while n <= tam
  an(n) = ((((n-3) * an(n-1))/ n) + 1);
  n=n+1;
end

plot(an)
xlabel('n');
ylabel('an');
title('recurrences');

an(999)