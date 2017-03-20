/* https://www.reddit.com/r/dailyprogrammer/comments/5yoo87/20170310_challenge_305_hard_numbers_for_sale/?st=j0i9a93n&sh=535a356b
Challenge #305 [Hard] Numbers for Sale */

#include <stdio.h>

int count[15][70];

int main() {
    int i,j,k;

    count[0][0] = 1;

    for(i=1;i<=14;i++) {
        for(j=0;j<=69;j++) {
            for(k=0;k<10;k++) {
                count[i][j] += count[i-1][j-k];
            }

            count[i][j] %= 1000000;
        }
    }

    printf("%d\n", count[14][69]);

    return 0;
}