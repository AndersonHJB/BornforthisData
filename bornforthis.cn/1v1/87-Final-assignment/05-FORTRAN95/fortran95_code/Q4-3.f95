module student_module
    implicit none
    type :: Student
        integer :: id
        real :: scores(5)
        real :: total
        integer :: rank
    end type Student

    type :: Class
        type(Student), dimension(30) :: students
        real, dimension(5) :: avg_scores
        integer, dimension(5) :: above_avg, below_avg
    contains
        procedure :: calculate_totals
        procedure :: calculate_averages
        procedure :: count_above_below_avg
        procedure :: sort_by_total
        procedure :: query_student
    end type Class
contains
    subroutine calculate_totals(this)
        class(Class), intent(inout) :: this
        integer :: i

        do i = 1, 30
            this%students(i)%total = sum(this%students(i)%scores)
        end do
    end subroutine calculate_totals

    subroutine calculate_averages(this)
        class(Class), intent(inout) :: this
        integer :: i, j

        this%avg_scores = 0.0
        do j = 1, 5
            do i = 1, 30
                this%avg_scores(j) = this%avg_scores(j) + this%students(i)%scores(j)
            end do
            this%avg_scores(j) = this%avg_scores(j) / 30.0
        end do
    end subroutine calculate_averages

    subroutine count_above_below_avg(this)
        class(Class), intent(inout) :: this
        integer :: i, j

        this%above_avg = 0
        this%below_avg = 0
        do j = 1, 5
            do i = 1, 30
                if (this%students(i)%scores(j) > this%avg_scores(j)) then
                    this%above_avg(j) = this%above_avg(j) + 1
                else
                    this%below_avg(j) = this%below_avg(j) + 1
                end if
            end do
        end do
    end subroutine count_above_below_avg

    subroutine sort_by_total(this)
        class(Class), intent(inout) :: this
        integer :: i, j
        type(Student) :: temp

        do i = 1, 29
            do j = i + 1, 30
                if (this%students(i)%total < this%students(j)%total) then
                    temp = this%students(i)
                    this%students(i) = this%students(j)
                    this%students(j) = temp
                end if
            end do
        end do

        do i = 1, 30
            this%students(i)%rank = i
        end do
    end subroutine sort_by_total

    subroutine query_student(this, id)
        class(Class), intent(inout) :: this
        integer, intent(in) :: id
        integer :: i

        do i = 1, 30
            if (this%students(i)%id == id) then
                print *, "Student ID: ", this%students(i)%id
                print *, "Rank: ", this%students(i)%rank
                print *, "Scores: ", this%students(i)%scores
                print *, "Total Score: ", this%students(i)%total
                return
            end if
        end do
        print *, "Student ID not found!"
    end subroutine query_student
end module student_module

program student_evaluation
    use student_module
    implicit none
    type(Class) :: myclass
    integer :: i, j, id
    character(len=20) :: filename
    character(len=100) :: line
    real :: score

    filename = "student_scores.txt"
    open(unit=10, file=filename, status="old", action="read")

    do i = 1, 30
        read(10, *) myclass%students(i)%id, myclass%students(i)%scores
    end do
    close(10)

    call myclass%calculate_totals()
    call myclass%calculate_averages()
    call myclass%count_above_below_avg()
    call myclass%sort_by_total()

    open(unit=20, file="sorted_scores.txt", status="replace", action="write")
    do i = 1, 30
        write(20, '(I4, 2X, I4, 2X, F6.2)') myclass%students(i)%rank, myclass%students(i)%id, myclass%students(i)%total
    end do
    close(20)

    print *, "Enter Student ID to query: "
    read *, id
    call myclass%query_student(id)

end program student_evaluation
