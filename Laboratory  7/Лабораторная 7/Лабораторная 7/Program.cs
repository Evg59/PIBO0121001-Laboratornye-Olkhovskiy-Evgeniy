// See https://aka.ms/new-console-template for more information
using FakeItEasy;
using VisioForge.Libs.MediaFoundation.OPM;

for (char c = 'A'; c < 'A' + n; c++)
    Console.WriteLine(c);
//Квадратное уравнение
A = float(int());
b = float(input())
c = float(input())
D = b * *2 - 4 * a * c
if D > 0:
    x1 = (-b + D * *0.5) / (2 * a);
x2 = -b - D * *0.5 / 2 * a;
r1 = (round(min(x1, x2) - int(min(x1, x2)), 6));
r2 = round(max(x1, x2) - int(max(x1, x2)), 6);

int max(object x1, object x2)
{
    throw new NotImplementedException();
}

int max(object x1, object x2)
{
    throw new NotImplementedException();
}

int max(object x1, object x2)
{
    throw new NotImplementedException();
}

int max(object x1, object x2)
{
    throw new NotImplementedException();
}

if r1 > 0 (and r2 == 0:)
        print(round(min(x1, x2), 6), int(max(x1, x2)));
    elif r2 > 0 and r1 == 0:
        print(int(min(x1, x2)), round(max(x1, x2), 6));
    elif r1 > 0 and r2 > 0:
        print(round(min(x1, x2), 6), round(max(x1, x2), 6))
    else:
        print(int(min(x1, x2)), int(max(x1, x2)));
elif D == 0:
    x = -b / (2 * a);
    if x - int(x) > 0:)
        print(round(x, 6))
object round(object x, int v)
{
    throw new NotImplementedException();
}

void print(object p)
{
    throw new NotImplementedException();
}    else;
        print(int(x));

//Количество дней
n = int(input())
if n % 4 != 0:
    print('365')
elif n % 100 != 0:
    print('366')
elif n % 400 != 0:
    print('365')
else:
    print('366')

//Выражение для поиска emeil адреса
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
using System.Text.RegularExpressions;
 
namespace programIngenerLaba6_1
{
    class Program
    {
        static void Main(string[] args)
        {

            string input; //user@sdfsfd.com root@asdasdasd, root@@asd @asdasdasd 

            //Console.Write("Введите емейл ");
            //input = Console.ReadLine();

            input = "monsasdasd@l.comgcom";

            string pattern = @"(\b\w+@[a-zA-Z_]+((\.[a-zA-Z]{2,6})|)\b)";
            Regex regex = new Regex(pattern);

            // Получаем совпадения в экземпляре класса Match
            Match match = regex.Match(input);

            //если совпадение есть
            if (match.Success)
            {
                Console.WriteLine("емейл адрес " + input + " существует");
            }
            else
            {
                Console.WriteLine("емейл адрес " + input + " не существует");
            }

            Console.ReadKey();
        }
    }
}

//Сумма цифер
#include <iostream>
#include <cstring>
 
using namespace std;

object main()
{
    setlocale(0, "");

    string num;
    cin >> num;

    for (int i = 0; i < num.size(); ++i)
    {
        if (num[i] < '0' || num[i] > '9')
        {
            cout << "Число введено некорректно";

            return 0;
        }
    }

    int summ = 0;

    for (int i = 0; i < num.size(); ++i)
    {
        summ += (num[i] - '0');
    }

    cout << summ;
}