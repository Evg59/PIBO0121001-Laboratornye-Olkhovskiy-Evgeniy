// See https://aka.ms/new-console-template for more information
//Абстрактный класс Equation
abstract class Function
{
    public abstract double Count(double x);
}

class Line : Function
{
    public readonly double A;
    public readonly double B;

    public Line(double a, double b)
    {
        A = a;
        B = b;
    }

    public override double Count(double x)
    {
        return A * x + B;
    }
}

