package LinearAndBinarySearch;

public class LinearAndBinarySearch{
    public static void main(String []args){
        int []values = new int[10];
        //popular os valores
        for(int i = 0; i < values.length; i++){
            values[i] = i;
        }
        for(int i = 0; i < values.length; i++){
           System.out.println(values[i]);
        }

        //realizar os testes
        System.out.println("Test1: All the results must be true");
        for(int i = 0; i < values.length; i++){
            System.out.println("Linear search result: " + linearSearch(values, i));
            System.out.println("Binary search result: " + binarySearch(values, i));
        }

        System.out.println("\n\n");
        
        System.out.println("Test2: All the results must be false");
        for(int i = 0; i < values.length; i++){
            System.out.println("Linear search result: " + linearSearch(values, i + 100));
            System.out.println("Binary search result: " + binarySearch(values, i + 100));
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
        int begin, end, mid; 
        end = values.length - 1;
        begin = 0;
        while (begin <= end){
            mid = (begin + end) / 2;
            if (values[mid] == key){
                return true;
            }
            else if (key > values[mid]){
                begin = mid + 1;
            }
            else{
              end = mid - 1;  
            }
        }
        return false; 	
    }

}