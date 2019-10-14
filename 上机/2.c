#include<stdio.h>
#include<string.h>
int main(){
	int n;
	int k;
	printf( "Enter n:");
	gets(n);
	printf( "Enter k:");
	gets(k);

	printf("%d/n",numJewelsInStones(j,s));
	return 0;
}
int** combine(int n, int k, int** columnSizes, int* returnSize) {
    int i = 0;
    int* use = (int*)calloc(k, sizeof(int));
    int** result = NULL;
    while(i >= 0) {
        use[i]++;
        if(use[i] > n)
            i--;
        else if(i == k - 1) {
            (*returnSize)++;
            result = (int**)realloc(result, *returnSize * sizeof(int*));
            result[*returnSize - 1] = (int*)malloc(k * sizeof(int));
            memcpy(result[*returnSize - 1], use, k * sizeof(int));
        }
        else {
            i++;
            use[i] = use[i - 1];
        }
    }
    columnSizes[0] = (int*)malloc(*returnSize * sizeof(int));
    for(i = 0; i < *returnSize; i++)
        columnSizes[0][i] = k;
    free(use);
    return result;
}
