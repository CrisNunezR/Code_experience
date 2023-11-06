#include <stdio.h>

int main(void)
{

//type DWORD AS UINTEGER
//type WORD AS USHORT

    type MyBitMapHeader field=1
        bfType as WORD
        bfSize as DWORD
        bfReserved1 as WORD
        bfReserved2 as WORD
        bfOffBits as DWORD
        biSize as DWORD
        biWidth as LONG
        biHeight as LONG
        biPlanes as WORD
        biBitCount as WORD
        biCompression as DWORD
        biSizeImage as DWORD
        biXPelsPerMeter as LONG
        biYPelsPerMeter as LONG
        biClrUsed as DWORD
        biClrImportant as DWORD
    end type

    DIM PictHeader AS MyBitMapHeader
    DIM BmpName AS STRING

    BmpName = COMMAND

    OPEN BmpName FOR BINARY AS #1
    GET #1,1,PictHeader
    PictHeader.biHeight = -PictHeader.biHeight
    PUT #1,1,PictHeader
    CLOSE #1
}
