package LinearAndBinarySearch;

public class LinearAndBinarySearch{
    public static void main(String []args){
        int []values = new int[10];
        //popular os valores
        for(int i = 0; i < values.length; i++){
            values[i] = i;
        }

        //realizar os testes
        for(int i = 0; i < values.length; i++){
            System.out.println("Linear search result: " + linearSearch(values, i));
            System.out.println("Binary search result: " + binarySearch(values, i));
        }
    }

    private static boolean linearSearch(int []values, int key){
        for(int i = 0; i < values.length; i++){
            if(values[i] == key){
                return true;
            }
        }
        return false;
    }
    
    private static boolean binarySearch(int []values, int key){
        int top, bot, mid; 
        top = values.length;
        bot = 0;
        
        while (top > bot){
            mid = (top + bot) / 2;
            if (mid == key)
                return true;
            else if (key > mid){
                bot = mid;
            }
            else{
              top = mid;  
            }
        }
        return false; 	
    }

}