program IntegralCalculator
    implicit none

    ! 定义变量
    integer :: choice
    real :: a, b, integral
    integer :: n

    ! 界限和分割数
    a = 0.0
    b = 1.0
    n = 100

    print*, "选择计算方法:"
    print*, "1 - 矩形法"
    print*, "2 - 梯形法"
    print*, "3 - 辛普森法"
    read*, choice

    ! 根据用户选择调用相应方法
    select case (choice)
    case (1)
        integral = rectangleMethod(a, b, n)
        print*, "矩形法计算结果为：", integral
    case (2)
        integral = trapezoidMethod(a, b, n)
        print*, "梯形法计算结果为：", integral
    case (3)
        integral = simpsonMethod(a, b, n)
        print*, "辛普森法计算结果为：", integral
    case default
        print*, "无效选择"
    end select

contains
    ! 矩形法子程序
    function rectangleMethod(a, b, n) result(integral)
        real, intent(in) :: a, b
        integer, intent(in) :: n
        real :: integral, h, x
        integer :: i

        h = (b - a) / n
        integral = 0.0

        do i = 0, n - 1
            x = a + i * h
            integral = integral + f(x) * h
        end do
    end function rectangleMethod

    ! 梯形法子程序
    function trapezoidMethod(a, b, n) result(integral)
        real, intent(in) :: a, b
        integer, intent(in) :: n
        real :: integral, h, x
        integer :: i

        h = (b - a) / n
        integral = (f(a) + f(b)) / 2.0

        do i = 1, n - 1
            x = a + i * h
            integral = integral + f(x)
        end do

        integral = integral * h
    end function trapezoidMethod

    ! 辛普森法子程序
    function simpsonMethod(a, b, n) result(integral)
        real, intent(in) :: a, b
        integer, intent(in) :: n
        real :: integral, h, x
        integer :: i

        h = (b - a) / n
        integral = f(a) + f(b)

        do i = 1, n - 1, 2
            x = a + i * h
            integral = integral + 4 * f(x)
        end do

        do i = 2, n - 2, 2
            x = a + i * h
            integral = integral + 2 * f(x)
        end do

        integral = integral * h / 3
    end function simpsonMethod

    ! 被积函数定义
    function f(x) result(fx)
        real, intent(in) :: x
        real :: fx

        fx = sin(x)  ! 示例函数
    end function f

end program IntegralCalculator
