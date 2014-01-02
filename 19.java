import static java.lang.System.*;
import java.util.*;

public class sundays
{
    public static int startDay;
    public static HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    public static void main(String[] args)
    {
        int sundays = 0;
        int year = 1901;
        startDay = 2;
        initializeMap();
        while (year < 2001)
        {
            sundays += sInYears(year);
            year++;
        }
        out.println(sundays);
    }

    public static int sInYears(int year)
    {
        out.println("NEW YEAR!!!!!");
        boolean leap = isLeap(year);
        int day = startDay;
        int dayNum = 1;
        int month = 1;
        int toReturn = 0;
        /*if (year == 1900)
        {
            day = 1;
        }*/
        //Loops over 12 months
        for (; month < 13; month++) 
        {
            if (month == 2 && leap)
            {
                month = 14;
            }
            //loops over the number of days in said month
            while (dayNum < map.get(month) + 1)
            {
                out.println(map.get(month));
                out.println(dayNum);
                out.println(day);
                 if (day == 7)
                 {
                    if (dayNum == 1) {
                        out.println("added");
                        toReturn++;
                    }
                    dayNum++;
                    day = 1;
                 }
                 else 
                 {
                    day++;
                    dayNum++;
                 }
            }
            if (month == 14) 
            {
                month = 2;
            } 
            dayNum = 1;
        }
        startDay = day;
        return toReturn;
    }

    public static void initializeMap()
    {
        map.put(1, 31);
        map.put(2, 28);
        map.put(3, 31);
        map.put(4, 30);
        map.put(5, 31);
        map.put(6, 30);
        map.put(7, 31);
        map.put(8, 31);
        map.put(9, 30);
        map.put(10, 31);
        map.put(11, 30);
        map.put(12, 31);
        map.put(14, 29);
    }

    public static boolean isLeap(int year)
    {
        String strYear = Integer.toString(year);
        if (year%4 == 0)
        {
            if (strYear.substring(2).equals("00"))
            {
                return year%400 == 0;
            }
            return true;
        }
        return false;
    }
    
}