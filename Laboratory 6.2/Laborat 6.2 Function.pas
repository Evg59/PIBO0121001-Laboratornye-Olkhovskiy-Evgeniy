const a=8;
var n,i,k:integer;
    x,y,s:real;
begin
write('Количество разбиений n=');
readln(n);
randomize;
k:=0;
for i:=1 to n do
 begin
 //закидывем случайные точки в треугольник
  repeat
   x:=a*random;
   y:=a*random;
  until x+y<=a;
  //считаем те что попали в заштрихованную область
  if not(((x>=0)and(x<=1)and(y>=4)and(y<=5))or((x>=4)and(x<=6)and(y>=0)and(y<=2)))then inc(k);
 end;
s:=a*a*k/2/n;
write('S=',s:0:2)
end.