program student_scores_multiarray
    implicit none
    integer, parameter :: n = 30, m = 5
    integer :: i, j, k, student_id(n), rank(n)
    real :: scores(n, m), total_scores(n), average(m)
    real :: above_avg(m), below_avg(m)
    character(len=100) :: filename
    real :: temp_score
    integer :: temp_id
    character(len=50) :: query_id
    integer :: query_index
    character(len=10) :: student_id_str(n), query_id_str

    ! 初始化
    total_scores = 0.0
    average = 0.0
    above_avg = 0
    below_avg = 0

    ! 读取数据
    open(unit=1, file='student_scores.txt', status='old')
    do i = 1, n
        read(1, *) student_id(i), (scores(i, j), j = 1, m)
    end do
    close(1)

    ! 转换学号为字符串
    do i = 1, n
        write(student_id_str(i), '(I10)') student_id(i)
    end do

    ! 计算总分和各科平均分
    do i = 1, n
        total_scores(i) = sum(scores(i, :))
        do j = 1, m
            average(j) = average(j) + scores(i, j)
        end do
    end do
    average = average / n

    ! 统计高于和低于平均分的人数
    do j = 1, m
        do i = 1, n
            if (scores(i, j) > average(j)) then
                above_avg(j) = above_avg(j) + 1
            else if (scores(i, j) < average(j)) then
                below_avg(j) = below_avg(j) + 1
            end if
        end do
    end do

    ! 按总分排序
    do i = 1, n
        rank(i) = i
    end do
    do i = 1, n-1
        do j = i+1, n
            if (total_scores(rank(i)) < total_scores(rank(j))) then
                temp_score = total_scores(rank(i))
                temp_id = rank(i)
                rank(i) = rank(j)
                rank(j) = temp_id
            end if
        end do
    end do

    ! 输出排序结果
    open(unit=2, file='sorted_scores.txt', status='replace')
    write(2, '(A8, A10, A10)') 'Rank', 'StudentID', 'TotalScore'
    do i = 1, n
        write(2, '(I8, A10, F10.2)') i, trim(student_id_str(rank(i))), total_scores(rank(i))
    end do
    close(2)

    ! 查询功能
    print *, "请输入要查询的学号:"
    read(*, '(A)') query_id
    query_index = -1

    ! 转换查询学号为字符串
    query_id_str = adjustl(query_id)

    do i = 1, n
        if (adjustl(student_id_str(i)) == query_id_str) then
            query_index = i
            exit
        end if
    end do

    if (query_index == -1) then
        print *, "未找到该学号的学生。"
    else
        do i = 1, n
            if (rank(i) == query_index) then
                print *, "名次:", i
                exit
            end if
        end do
        print *, "学号:", student_id(query_index)
        print *, "各科成绩:", (scores(query_index, j), j = 1, m)
        print *, "总分:", total_scores(query_index)
    end if

end program student_scores_multiarray
