program ConvertBases
    implicit none
    integer :: decimalNumber
    character(len=32) :: binary, octal, hexadecimal

    ! 用户输入十进制数字
    print*, '请输入一个十进制数:'
    read*, decimalNumber

    ! 十进制转换到其他进制
    call DecimalToBinary(decimalNumber, binary)
    call DecimalToOctal(decimalNumber, octal)
    call DecimalToHexadecimal(decimalNumber, hexadecimal)

    ! 显示结果
    print*, '二进制表示: ', trim(binary)
    print*, '八进制表示: ', trim(octal)
    print*, '十六进制表示: ', trim(hexadecimal)

contains
    ! 十进制转二进制
    subroutine DecimalToBinary(decimal, binary)
        integer, intent(in) :: decimal
        character(len=32), intent(out) :: binary
        integer :: n, i
        binary = ' '
        n = decimal
        i = 0
        do while (n > 0)
            i = i + 1
            binary(len(binary)-i+1:len(binary)-i+1) = char(iachar('0') + mod(n, 2))
            n = n / 2
        end do
    end subroutine DecimalToBinary

    ! 十进制转八进制
    subroutine DecimalToOctal(decimal, octal)
        integer, intent(in) :: decimal
        character(len=32), intent(out) :: octal
        integer :: n, i
        octal = ' '
        n = decimal
        i = 0
        do while (n > 0)
            i = i + 1
            octal(len(octal)-i+1:len(octal)-i+1) = char(iachar('0') + mod(n, 8))
            n = n / 8
        end do
    end subroutine DecimalToOctal

    ! 十进制转十六进制
    subroutine DecimalToHexadecimal(decimal, hexadecimal)
        integer, intent(in) :: decimal
        character(len=32), intent(out) :: hexadecimal
        integer :: n, i, remainder
        character(len=1), dimension(0:15) :: hexdigits
        data hexdigits /'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'/
        hexadecimal = ' '
        n = decimal
        i = 0
        do while (n > 0)
            i = i + 1
            remainder = mod(n, 16)
            hexadecimal(len(hexadecimal)-i+1:len(hexadecimal)-i+1) = hexdigits(remainder)
            n = n / 16
        end do
    end subroutine DecimalToHexadecimal

end program ConvertBases
