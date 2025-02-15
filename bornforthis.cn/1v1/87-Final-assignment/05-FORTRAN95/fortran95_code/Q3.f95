program GaussianElimination
    implicit none

    ! 定义变量
    integer, parameter :: n = 3
    real :: A(n, n+1) ! 增广矩阵
    real :: x(n)
    integer :: i, j, k
    real :: factor

    ! 初始化增广矩阵
    A = reshape([ &
        2.0, -1.0, 3.0, 12.0, & ! 示例方程1: 2x - y + 3z = 12
        -3.0, 4.0, -2.0, 30.0, & ! 示例方程2: -3x + 4y - 2z = 30
        1.0, -2.0, 1.0, 33.0], & ! 示例方程3: x - 2y + z = 33
        shape(A))

    ! 高斯消元法消元过程
    do k = 1, n-1
        do i = k+1, n
            factor = A(i, k) / A(k, k)
            do j = k, n+1
                A(i, j) = A(i, j) - factor * A(k, j)
            end do
        end do
    end do

    ! 回代过程
    x(n) = A(n, n+1) / A(n, n)
    do i = n-1, 1, -1
        x(i) = A(i, n+1)
        do j = i+1, n
            x(i) = x(i) - A(i, j) * x(j)
        end do
        x(i) = x(i) / A(i, i)
    end do

    ! 输出结果
    print *, "解为:"
    do i = 1, n
        print *, "x(", i, ") = ", x(i)
    end do

end program GaussianElimination
