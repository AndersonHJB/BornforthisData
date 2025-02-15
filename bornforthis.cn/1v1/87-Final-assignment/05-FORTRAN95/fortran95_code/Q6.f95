program SectionProperties
    implicit none
    integer :: NSHAPE
    real :: A, Yc, Xc, I

    ! 用户输入选择形状
    print *, '输入形状代码（1=矩形，2=圆端形，3=圆形，4=空心圆形）：'
    read *, NSHAPE

    select case (NSHAPE)
    case (1)
        call Rectangle(A, Yc, Xc, I)
    case (2)
        call TShape(A, Yc, Xc, I)  ! 假设已有圆端形计算函数
    case (3)
        call Circle(A, Yc, Xc, I)
    case (4)
        call HollowCircle(A, Yc, Xc, I)
    end select

    print *, '面积: ', A
    print *, '形心位置: (', Yc, ',', Xc, ')'
    print *, '惯性矩: ', I
end program SectionProperties

! 矩形函数定义
subroutine Rectangle(A, Yc, Xc, I)
    real, intent(out) :: A, Yc, Xc, I
    real :: b, h
    print *, '输入矩形的宽度和高度:'
    read *, b, h
    A = b * h
    Yc = h / 2
    Xc = b / 2
    I = b * h**3 / 12
end subroutine Rectangle

! 圆形函数定义
subroutine Circle(A, Yc, Xc, I)
    real, intent(out) :: A, Yc, Xc, I
    real :: r
    print *, '输入圆形的半径:'
    read *, r
    A = 3.14159 * r**2
    Yc = 0.0
    Xc = 0.0
    I = 3.14159 * r**4 / 4
end subroutine Circle

! 空心圆形函数定义
! subroutine HollowCircle(A, Yc, Xc, I)
!     real, intent(out) :: A, Yc, Xc, I
!     real :: R, r
!     print *, '输入外圆和内圆的半径:'
!     read *, R, r
!     A = 3.14159 * (R**2 - r**2)
!     Yc = 0.0
!     Xc = 0.0
!     I = 3.14159 * (R**4 - r**4) / 4
! end subroutine HollowCircle
subroutine HollowCircle(A, Yc, Xc, I)
    real, intent(out) :: A, Yc, Xc, I
    real :: outerRadius, innerRadius  ! 更明确的变量名

    print *, '输入外圆和内圆的半径:'
    read *, outerRadius, innerRadius
    A = 3.14159 * (outerRadius**2 - innerRadius**2)
    Yc = 0.0
    Xc = 0.0
    I = 3.14159 * (outerRadius**4 - innerRadius**4) / 4
end subroutine HollowCircle

! 圆端形（T形）函数定义（示例）
subroutine TShape(A, Yc, Xc, I)
    real, intent(out) :: A, Yc, Xc, I
    real :: b, h, r
    print *, '输入T形的宽度、高度和圆端半径:'
    read *, b, h, r
    A = b * h + 3.14159 * r**2
    Yc = (h * b * (h / 2) + 3.14159 * r**2 * (h + r)) / A
    Xc = b / 2
    I = (b * h**3 / 12) + (3.14159 * r**4 / 4) + (3.14159 * r**2 * (h + r - Yc)**2)
end subroutine TShape
