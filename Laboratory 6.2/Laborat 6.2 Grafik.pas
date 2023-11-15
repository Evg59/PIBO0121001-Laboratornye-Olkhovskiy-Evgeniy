Program Graphik;
Uses GraphABC;
Function F (x:Real) : Real ; { Функция, для графика }
begin
 F:=x*x*exp(-abs(x))
end;
Const a=-3;
      b=3;
      n=500;
      x0=windowwidth div 2;{ координаты }
      y0=windowheight-60;
Procedure Koord(var mx,my:real);
{ Процедура, выводящая на экран оси координат, единичные  метки,
стрелки и сами координаты (числа) }
var i:byte;
    s:string;
    x,max:real;
begin
line(0,y0,2*x0-10,y0);{оси}
line(2*x0-10,y0,2*x0-20,y0+5);
line(2*x0-10,y0,2*x0-20,y0-5);
line(x0,y0,x0,10);
line(x0,10,x0-5,20);
line(x0,10,x0+5,20);
textout(x0+10,10,'Y');
textout(2*x0-20,y0-20,'X');
{найдем макс значение функции для масштаба по Y}
x:=a;
max:=F(x);
while x<=b do
 begin
  if F(x)>max then max:=F(x);
  x:=x+0.01
 end;
mx:=(x0-30)/b;{масштвб по Х}
my:=(y0-60)/max;{масштаб по Y}
for i:=1 to 6 do  {засечки и подписи на осях}
 begin
  line(x0+round(i*mx),y0-3,x0+round(i*mx),y0+3);
  line(x0-round(i*mx),y0-3,x0-round(i*mx),y0+3);
  line(x0-3,y0-round(i*my/10),x0+3,y0-round(i*my/10));
  str(i,s);
  textout(x0+round(i*mx),y0+10,s);
  textout(x0-round(i*mx),y0+10,'-'+s);
  str(i/10:0:1,s);
  textout(x0-20,y0-round(i*my/10),s);
 end;
end;
var t,h,mx,my:real;
begin
Koord(mx,my);
t:=a;
h:=(b-a)/n; {шаг перемещения от a к b}
setpencolor(clRed);
moveto(x0+round(a*mx),y0-round(F(a)*my));
while t<=b do
 begin
  t:=t+h;
  lineto(x0+round(t*mx),y0-round(F(t)*my));
 end;
end.