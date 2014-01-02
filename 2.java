import java.lang.System.*;
import java.util.*;

public class fib 
{
    public static void main(String[] args)
    {
        int curr = 1;
        int prev = 0;
        int total = 0;
        Vector<Integer> fibs = new Vector<Integer>();
        while(curr < 4e6)
        {
            int temp = curr;
            curr += prev;
            prev = temp;
            fibs.add(curr);
        }
        for (int i = 0; i < fibs.size(); i++) 
        {
            int toTest = fibs.elementAt(i);
            if (toTest % 2 == 0) total += toTest;
        }
        System.out.println(total);
    }
}