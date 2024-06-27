module student_module
    implicit none
    type :: student
        integer :: id
        real :: scores(5)
        real :: total
    end type student

    type :: class
        type(student), dimension(:), allocatable :: students
        real :: avg_scores(5)
        integer :: above_avg(5)
        integer :: below_avg(5)
    contains
        procedure :: compute_totals
        procedure :: compute_averages
        procedure :: count_above_below_avg
        procedure :: sort_by_total
        procedure :: query_student
    end type class
contains
    subroutine compute_totals(this)
        class(class), intent(inout) :: this
        integer :: i

        do i = 1, size(this%students)
            this%students(i)%total = sum(this%students(i)%scores)
        end do
    end subroutine compute_totals

    subroutine compute_averages(this)
        class(class), intent(inout) :: this
        integer :: i, j
        real :: sum_scores(5)

        sum_scores = 0.0
        do i = 1, size(this%students)
            do j = 1, 5
                sum_scores(j) = sum_scores(j) + this%students(i)%scores(j)
            end do
        end do
        this%avg_scores = sum_scores / size(this%students)
    end subroutine compute_averages

    subroutine count_above_below_avg(this)
        class(class), intent(inout) :: this
        integer :: i, j

        this%above_avg = 0
        this%below_avg = 0
        do i = 1, size(this%students)
            do j = 1, 5
                if (this%students(i)%scores(j) >= this%avg_scores(j)) then
                    this%above_avg(j) = this%above_avg(j) + 1
                else
                    this%below_avg(j) = this%below_avg(j) + 1
                end if
            end do
        end do
    end subroutine count_above_below_avg

    subroutine sort_by_total(this)
        class(class), intent(inout) :: this
        integer :: i, j
        type(student) :: temp

        do i = 1, size(this%students)-1
            do j = i + 1, size(this%students)
                if (this%students(i)%total < this%students(j)%total) then
                    temp = this%students(i)
                    this%students(i) = this%students(j)
                    this%students(j) = temp
                end if
            end do
        end do
    end subroutine sort_by_total

    subroutine query_student(this, id)
        class(class), intent(in) :: this
        integer, intent(in) :: id
        integer :: i, j

        do i = 1, size(this%students)
            if (this%students(i)%id == id) then
                print *, "Student ID:", this%students(i)%id
                print *, "Rank:", i
                print *, "Scores:", this%students(i)%scores
                print *, "Total Score:", this%students(i)%total
                return
            end if
        end do
        print *, "Student ID not found."
    end subroutine query_student
end module student_module

program class_evaluation
    use student_module
    implicit none
    type(class) :: my_class
    integer :: i, j
    integer, parameter :: n = 30
    real :: score
    character(len=30) :: filename

    allocate(my_class%students(n))

    filename = 'student_scores.txt'
    open(unit=10, file=filename, status='old')

    do i = 1, n
        read(10, *) my_class%students(i)%id, (my_class%students(i)%scores(j), j=1, 5)
    end do
    close(10)

    call my_class%compute_totals()
    call my_class%compute_averages()
    call my_class%count_above_below_avg()
    call my_class%sort_by_total()

    ! 输出排序后的成绩到文件
    open(unit=20, file='sorted_scores.txt', status='replace')
    do i = 1, n
        write(20, *) i, my_class%students(i)%id, my_class%students(i)%total
    end do
    close(20)

    ! 输出各门课程的平均分和高于、低于平均分的人数
    print *, "Average Scores:", my_class%avg_scores
    print *, "Above Average:", my_class%above_avg
    print *, "Below Average:", my_class%below_avg

    ! 查询学生成绩
    call my_class%query_student(1012)

end program class_evaluation
