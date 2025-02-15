program root_finding
    implicit none
    ! 定义变量
    integer :: method
    real :: root

    ! 文本菜单
    print *, '请选择求根方法:'
    print *, '1 - 迭代法'
    print *, '2 - 牛顿迭代法'
    print *, '3 - 二分法'
    read *, method

    ! 根据选择执行不同的方法
    select case (method)
    case (1)
        call fixed_point_iteration(root)
    case (2)
        call newton_raphson(root)
    case (3)
        call bisection(root)
    case default
        print *, '无效的输入。'
    end select

    print *, '方程的根是: ', root
end program root_finding

! 定义方程 f(x) = x^3 - x - 2
real function f(x)
    real, intent(in) :: x
    f = x**3 - x - 2
end function f

! 定义导数 f'(x) = 3x^2 - 1
real function df(x)
    real, intent(in) :: x
    df = 3*x**2 - 1
end function df

! 迭代法
subroutine fixed_point_iteration(root)
    real, intent(out) :: root
    real :: x0, x1, lambda, tol
    integer :: i, max_iter

    x0 = 1.0       ! 初值
    lambda = 0.1   ! 步长系数
    tol = 1.0e-6
    max_iter = 10000

    do i = 1, max_iter
        x1 = x0 - lambda * f(x0)
        if (abs(x1 - x0) < tol) then
            root = x1
            return
        end if
        x0 = x1
    end do
    print *, '迭代可能未收敛'
end subroutine fixed_point_iteration

! 牛顿迭代法
subroutine newton_raphson(root)
    real, intent(out) :: root
    real :: x0, tol
    integer :: i, max_iter

    x0 = 1.0
    tol = 1.0e-6
    max_iter = 10000

    do i = 1, max_iter
        root = x0 - f(x0) / df(x0)
        if (abs(root - x0) < tol) exit
        x0 = root
    end do
end subroutine newton_raphson

! 二分法
subroutine bisection(root)
    real, intent(out) :: root
    real :: a, b, c, fa, fc, tol
    integer :: i, max_iter

    a = 1.0
    b = 3.0
    tol = 1.0e-6
    max_iter = 10000

    fa = f(a)
    do i = 1, max_iter
        c = (a + b) / 2.0
        fc = f(c)
        if (fc == 0.0 .or. (b - a) / 2.0 < tol) then
            root = c
            return
        end if
        if (sign(1.0, fa) == sign(1.0, fc)) then
            a = c
            fa = fc
        else
            b = c
        end if
    end do
    root = c
end subroutine bisection