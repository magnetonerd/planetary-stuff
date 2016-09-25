program Grav

  implicit none

  doubleprecision :: F,U1,U2,s,bigG,smallg,bigM,smallm,Re
  integer :: i,j,k

  bigG = 6.67d-11
  bigM = 5.98d24
  smallm = 1.0d0
  Re = 6.38d6
  smallg = bigG*bigM/Re**2
  F = smallm*smallg
  write(*,*) smallg,F

  s = 0.0d0

  open(1,file="gravnums.txt")
  
  do i=0,10000
     U1 = F*Re*(1-(1/(1+s)))
     U2 = F*Re*(s/(1+s))
     write(1,*)s,U1,U2
     s = s + 0.001d0
  end do
  

end program Grav
