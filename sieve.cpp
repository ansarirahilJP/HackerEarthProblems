function sieve(n){
    S = [];
    S[1] = 0; // 1- not a prime number
    / / fill it with figures one
    for(k=2; k<=n; k++)
        S[k]=1;
     
    for(k=2; k*k<=n; k++){
        / / if k is a simple (not crossed out)
        if(S[k]==1){
            / / then we cross out multiples of k
            for(l=k*k; l<=n; l+=k){
                S[l]=0;
                }
            }
        }
    return S;
    }