#include <stdio.h>
#include <stdint.h>
// from https://web.microsoftstream.com/video/dfdc58cb-da0c-411b-a9d7-b1199252c312?referrer=https:%2F%2Flearnonline.gmit.ie%2Fcourse%2Fview.php%3Fid%3D135
// mnist c file for recognising digits in files
int main(int argc, char *argv[])
{
    // opens files
    
    FILE *f = fopen("../files/t10k-images-idx3-ubyte", "rb"); // rb = read binary
    FILE *labels = fopen("../files/t10k-labels-idx1-ubyte", "rb"); // rb = read binary

    uint8_t b, lblB; 
    int i, j, k;

    // reads 1 bit 
    for(i = 0; i < 16; i++) 
    {
        fread(&b, 1, 1, f);
        printf("%02x ", b);
    }

    printf("\n");

    // reads in first part of label file ../files/t10k-labels-idx1-ubyte
    for(i = 0; i < 8; i ++)
    {
        fread(&lblB, 1, 1, labels);
        printf("%02x ", lblB);
    }

    printf("\n");

    for(k = 0; k < 3; k++)
    {
        fread(&lblB, 1, 1, labels);
        printf("%02x \n", lblB);

        for(i = 0; i < 28; i++ )
        {
            for(j = 0; j < 28; j++)
            {
                fread(&b, 1, 1, f);
				// current bit = 127
                printf("%s", (b > 127) ? "0" : "."); 
                
            }

            printf("\n");
        }
        printf("\n");
    }
    
    printf("\n");
    return 0;
}