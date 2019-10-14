#include<stdio.h>
#include<string.h>
int main(){
	char j[100];
	char s[100];
	printf( "Enter j:");
	gets(j);
	printf( "Enter s:");
	gets(s);
	printf("%d\n",numJewelsInStones(j,s));
	return 0;
}

int numJewelsInStones(char* J,char* S) {
    int i,j,count=0;
    for(i=0;i<strlen(J);i++){
        for(j=0;j<strlen(S);j++){
            if(J[i]==S[j]){
                count++;
            }
        }
    }
    return count;
}
