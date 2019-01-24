#include <stdio.h>

int main(){
	int mass[10];
	printf("Enter 10 values:");
	for(int i=0;i<10;i++){
		scanf("%d",(mass+i));
	}
	for(int i=9;i>0;i--)for(int j=1;j<=i;j++){
		if(mass[j-1]>mass[j]){
			int temp=mass[j];
			mass[j]=mass[j-1];
			mass[j-1]=temp;
		}
	}
	printf("Sorted values:\n");
	for(int i=0;i<10;i++){
		printf("%d ",mass[i]);
	}
	return 0;
}