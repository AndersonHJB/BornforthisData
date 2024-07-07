program TyphoonData
    implicit none
    character(len=200) :: line
    character(len=4) :: stormID
    integer :: i, j, num_records, num_typhoons, typhoon_idx
    character(len=100) :: filename
    real :: lat, lon, pressure, min_pressure
    integer, dimension(2000) :: typhoon_records
    real, dimension(2000) :: min_pressures
    character(len=5) :: input_id

    ! 打开文件
    filename = 'bst1951_2010.txt'
    open(unit=10, file=filename, status='old')

    ! 读取文件
    num_typhoons = 0
    do
        read(10, '(A)', iostat=i) line
        if (i /= 0) exit
        
        if (trim(adjustl(line(1:5))) == '66666') then
            if (len_trim(line) >= 14) then
                num_typhoons = num_typhoons + 1
                if (num_typhoons > 2000) then
                    print *, '台风数量超过数组限制'
                    exit
                end if
                read(line(7:10), '(I4)') typhoon_records(num_typhoons)
                read(line(12:14), '(I3)') num_records  ! 修正读取的格式
                min_pressure = 9999.0
                
                print *, '台风编号:', typhoon_records(num_typhoons), '记录数:', num_records  ! 调试输出

                do j = 1, num_records
                    read(10, '(A)', iostat=i) line
                    if (i /= 0) exit
                    if (len_trim(line) >= 33) then
                        read(line(21:24), '(F4.1)') lat
                        read(line(25:28), '(F4.1)') lon
                        read(line(29:33), '(F5.1)') pressure
                        
                        if (pressure < min_pressure) then
                            min_pressure = pressure
                        end if
                    end if
                end do
                
                min_pressures(num_typhoons) = min_pressure
            end if
        end if
    end do

    close(10)
    
    ! 打印台风数量以调试
    print *, '总共读取的台风数量:', num_typhoons
    
    ! 输入台风编号
    print *, '请输入台风编号 (如5204):'
    read *, input_id
    
    ! 查找并打印台风记录
    open(unit=10, file=filename, status='old')
    do
        read(10, '(A)', iostat=i) line
        if (i /= 0) exit
        
        if (trim(adjustl(line(1:5))) == '66666') then
            if (len_trim(line) >= 14) then
                read(line(7:10), '(A4)') stormID
                if (stormID == input_id) then
                    read(line(12:14), '(I3)') num_records  ! 修正读取的格式
                    
                    print *, '台风编号: ', stormID
                    print *, '记录数: ', num_records
                    
                    do j = 1, num_records
                        read(10, '(A)', iostat=i) line
                        if (i /= 0) exit
                        print *, line
                    end do
                end if
            end if
        end if
    end do
    
    close(10)
    
    ! 写入文件
    open(unit=20, file='min_pressures.txt', status='replace')
    do typhoon_idx = 1, num_typhoons
        write(20, '(I5, F8.1)') typhoon_records(typhoon_idx), min_pressures(typhoon_idx)
    end do
    close(20)

end program TyphoonData
! PROGRAM TyphoonData
!     IMPLICIT NONE
!     CHARACTER(LEN=100) :: line
!     CHARACTER(LEN=50) :: filename
!     INTEGER :: unit, i, typhoonNumber, numberOfRecords, numRecords, num, latitude, longitude, pressure
!     INTEGER, DIMENSION(:), ALLOCATABLE :: pressures
!     INTEGER :: minPressure
!     LOGICAL :: found
!     CHARACTER(LEN=50) :: typhoonName
!     CHARACTER(LEN=10) :: inputTyphoonNumber
!     INTEGER :: ioStatus
  
!     filename = 'bst1951_2010.txt'
!     unit = 10
!     OPEN(unit=unit, FILE=filename, STATUS='OLD', ACTION='READ')
  
!     WRITE(*,*) '请输入台风编号 (例如: 5204):'
!     READ(*,*) inputTyphoonNumber
!     READ(inputTyphoonNumber, '(I4)') typhoonNumber
  
!     ! 打开输出文件
!     OPEN(20, FILE='typhoon_min_pressures.txt', STATUS='NEW', ACTION='WRITE')
  
!     found = .FALSE.
!     DO WHILE (.NOT. found)
!       READ(unit, '(A)', IOSTAT=ioStatus) line
!       IF (ioStatus /= 0) EXIT
!       IF (TRIM(line(1:5)) == '66666') THEN
!         READ(line(7:10), '(I4)') num
!         READ(line(12:14), '(I3)') numberOfRecords
!         typhoonName = line(31:50)
!         ALLOCATE(pressures(numberOfRecords))
!         DO i = 1, numberOfRecords
!           READ(unit, '(A)', IOSTAT=ioStatus) line
!           IF (ioStatus /= 0) EXIT
!           READ(line(23:26), '(I4)') pressure
!           pressures(i) = pressure
!           IF (num == typhoonNumber) THEN
!             WRITE(*, '(A)', ADVANCE='NO') TRIM(line(1:10))
!             WRITE(*, '(I4, 1X)', ADVANCE='NO') latitude
!             WRITE(*, '(I4, 1X)', ADVANCE='NO') longitude
!             WRITE(*, '(I4)') pressure
!           END IF
!         END DO
!         minPressure = MINVAL(pressures)
!         WRITE(20, '(I5, 1X, I4)') num, minPressure
!         DEALLOCATE(pressures)
!         IF (num == typhoonNumber) found = .TRUE.
!       END IF
!     END DO
  
!     CLOSE(unit)
!     CLOSE(20)
  
!     IF (.NOT. found) THEN
!       WRITE(*,*) '未找到台风编号 ', typhoonNumber
!     ELSE
!       WRITE(*,*) '台风编号 ', typhoonNumber, ' 的记录已输出。'
!     END IF
  
!   END PROGRAM TyphoonData
  