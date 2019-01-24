#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define DISPLACEMENT 13

int main(){
	char text[200];
	printf("Enter your message (max size - 200 chars):\n");
	gets(&text);
	int len = strlen(text);
	stringToUpperCase(text,len);
	while(len--)
		if(text[len] >= 'A' && text[len] <= 'Z')
			text[len] = (text[len] - 'A' + DISPLACEMENT) % 26 + 'A';
	printf("Your crypted message is: \n%s\n", text);
	return 0;
}

int stringToUpperCase(char* str, int length){
	while(length--)
		if(str[length] >= 'a' && str[length] <= 'z')
			str[length] = str[length] - 'a' + 'A';
	return 0;
}
