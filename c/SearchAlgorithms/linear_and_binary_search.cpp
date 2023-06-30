#include <iostream>
using namespace std;
#define LEN 10


//Complexity O(log(n))
//Constraint: The list must be ordered
bool binary_search(int *values, int key){
	int begin, end, mid;
	begin = 0;
	end = LEN - 1;

	while(begin <= end){
		mid = (begin + end)/2;
		if(values[mid] == key){
			return true;
		}
		else if(values[mid]  < key){
			begin = mid + 1;
		}
		else{
			end = mid - 1;
		}
	}
	return false;
}	

//Complexity: O(n)
bool linear_search(int *values, int key){
	for(int i = 0; i < LEN; i++){
		if(values[i] == key){
			return true;
		}
	}
	return false;
}

int main(){
	int values[] = {1,2,3,4,5,6,7,8,9,10};
	cout << "-> Test1: all outputs should be true: " << endl;
	for(int i = 1; i <= LEN; i++){
		cout << "Linear search for "<< i <<" is: "<< linear_search(values, i) << "\n";
		cout << "Binary search for "<< i <<" is: "<< binary_search(values, i) << "\n\n";
	}

	cout << "\n\n-> Test2 all outputs should be false: " << endl;
	for(int i = 0; i <= LEN; i++){
		int key = i + 100;
		cout << "Linear search result: " << key <<" is: "<< linear_search(values, key + 100) << "\n";
		cout << "Binary search result: " << key <<" is: "<< binary_search(values, key + 100) << "\n\n";
	}
}

