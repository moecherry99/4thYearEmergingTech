#include <stdio.h>

int main(int argc, char (*argv[])){

    FILE *f = fopen("t10k-images.idx3-ubyte", "rb");
    int b = 0;

    printf("No of bytes in an int : %d\n", sizeof(b));

    for (int i = 0; i < 20; i++){
        fread(&b, 1, 1, f);
        printf("%02x\n", b);

    }
    printf("\n");
    
    return 0;
}
