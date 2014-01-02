import static java.lang.System.*;

public class abundant
{
    public static void main(String[] args)
    {
        int limit = 20162;
        int total = 0;
        for (int i = 0; i < limit; i++)
        {
            if (canAdd(i)) 
            {
                total += i;  
            }
            //out.println(canAdd(28123));
        }
        out.println(total);
        //out.println(isAbundant(220));
    }

    public static boolean isAbundant(int n)
    {
        int total = 0;
        int factor = 1;
        while (factor*factor <= n)
        {
            if (n % factor == 0)
            {
                total += factor;
                if (factor != 1 && factor*factor < n)
                {
                    total += n/factor;
                }
            }
            factor++;
        }
        //out.println(total);
        return total > n;
    }

    public static boolean canAdd(int n)
    {
        boolean toAdd = true;
            for (int i = 1; i < n; i++)
            {
                if (isAbundant(i) && isAbundant(n-i))
                {
                    toAdd = false;
                    break;
                }
            }
        out.print(toAdd);
        out.print(": ");
        out.println(n);
        return toAdd;
    }
}