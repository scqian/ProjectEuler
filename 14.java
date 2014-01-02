import static java.lang.System.*;

public class collatz
{
    public static void main(String[] args)
    {
        long longLen = 0;
        long start = 0;
        long curr;
        for(int i = 2; i < 1e6; i++) 
        {
            long length = 1;
            curr = i;
            while (curr != 1)
            {
                if ((curr % 2) == 0) 
                {
                    curr = curr/2;
                }
                else
                {
                    curr = curr * 3 + 1;
                }
                length++;
            }
            if (length > longLen) 
            {
                longLen = length;
                start = i;
            }
            
        }
        out.println(start);
    }

    /*private static int chainLength(int num)
    {
        int num = 837799;
        out.println(num*3 + 1);
        int count = 1;
        while (num != 1) 
        {
            if (num % 2 == 0)
            {
                num = num/2;
            }
            else
            {
                num = 3*num + 1;
            }
            count++;
            out.println(num);
        }
        out.println(count);
        return count;
    }*/
}