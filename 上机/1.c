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
