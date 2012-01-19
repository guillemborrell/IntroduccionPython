module rhs_tur2d
  use, intrinsic :: iso_c_binding
  implicit none
  include 'fftw3.f03'

  real(kind = 8):: Lx__=1
  real(kind = 8):: Ly__=1
  real(kind = 8):: pi__ = 4.0d0*atan(1.0d0)
  integer:: nx__ = 64
  integer:: ny__ = 64
  integer:: Re__ = 10000

  contains


    !!!! ACHTUNG
    !!!! These helper functions depend on Fortran Indexing.

    function init()
      use, intrinsic :: iso_c_binding
      implicit none
      include 'fftw3.f03'
      integer:: init
      
      init = fftw_init_threads()

    end function init


    function kx(i,j)
      implicit none
      !Compute the kx wavenumbers
      integer, intent(in):: i,j
      real(kind = 8):: kx
      
      if (i-1 < nx__/2) then
         kx = i-1
      else
         kx = -nx__ + (i-1)
      end if

      kx = 2.0d0*pi__/Lx__*kx
         
    end function kx

    function ky(i,j)
      implicit none
      !Compute the ky wavenumbers
      integer, intent(in):: i,j
      real(kind = 8):: ky

      if (j-1 < ny__/2) then
         ky = j-1
      else
         ky = -ny__ + (j-1)
      end if

      ky = 2.0d0*pi__/Ly__*ky
    end function ky

    function lap(i,j)
      implicit none
      !Compute the Laplace Operator
      integer, intent(in):: i,j
      real(kind = 8):: lap

      lap = -(kx(i,j)**2+ky(i,j)**2)
    end function lap

    function poisson(i,j)
      implicit none
      !Compute the Poisson operator
      integer, intent(in):: i,j
      real(kind = 8)::  poisson

      if (i==1 .and. j==1) then
         poisson = 1.0d0
      else
         poisson = -(kx(i,j)**2+ky(i,j)**2)
      end if
    end function poisson

    function u_hat_f(omega,nx,ny)
      implicit none
      ! U from omega
      ! it is -ddy/poisson
      !f2py depend(nx) u_hat_f
      !f2py depend(ny) u_hat_f
      integer, intent(in):: nx,ny
      complex(kind = 8), dimension(nx,ny), intent(in):: omega
      complex(kind = 8), dimension(nx,ny):: u_hat_f

      integer:: i,j

      !!!!!!!!! ACHTUNG !!!!!!!!!
      ! I don't have any idea why ky indices must be swapped
      !!!!!!!!! ACHTUNG !!!!!!!!!

      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            u_hat_f(i,j) = -cmplx(0,1)*ky(j,i)*omega(i,j)/poisson(i,j)
         end do
      end do

      !$OMP END PARALLEL DO
    end function u_hat_f

    function v_hat_f(omega,nx,ny)
      implicit none
      ! V from omega
      ! it is ddx/poission
      !f2py depend(nx) v_hat_f
      !f2py depend(ny) v_hat_f
      integer, intent(in):: nx,ny
      complex(kind = 8), dimension(nx,ny), intent(in):: omega
      complex(kind = 8), dimension(nx,ny):: v_hat_f

      integer:: i,j

      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            v_hat_f(i,j) = cmplx(0,1d0)*kx(j,i)/poisson(i,j)*omega(i,j)
         end do
      end do
      !$OMP END PARALLEL DO
    end function v_hat_f

    function ddx(omega,nx,ny)
      implicit none
      !x partial derivative in fourier space
      !f2py depend(nx) ddx
      !f2py depend(ny) ddx
      integer, intent(in):: nx,ny
      complex(kind = 8), dimension(nx,ny), intent(in):: omega
      complex(kind = 8), dimension(nx,ny):: ddx

      integer:: i,j

      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            ddx(i,j) = cmplx(0,1d0)*kx(j,i)*omega(i,j)
         end do
      end do
      !$OMP END PARALLEL DO
    end function ddx

    function ddy(omega,nx,ny)
      implicit none
      !y partial derivative in 
      !f2py depend(nx) ddy
      !f2py depend(ny) ddy
      integer, intent(in):: nx,ny
      complex(kind = 8), dimension(nx,ny), intent(in):: omega
      complex(kind = 8), dimension(nx,ny):: ddy

      integer:: i,j

      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            ddy(i,j) = cmplx(0,1d0)*ky(j,i)*omega(i,j)
         end do
      end do
      !$OMP END PARALLEL DO
    end function ddy

    function dealias(omega,nx,ny)
      implicit none
      ! Dealias operator
      ! Inplace operator
      !f2py depend(nx) dealias
      !f2py depend(ny) dealias
      integer, intent(in):: nx,ny
      complex(kind = 8), dimension(nx,ny), intent(in):: omega
      complex(kind = 8), dimension(nx,ny):: dealias

      integer:: i,j

      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            if (abs(kx(i,j)*Lx__/(2*pi__)) < nx/3 .and. &
                 & abs(ky(i,j)*Ly__/(2*pi__)) < ny/3) then
               dealias(i,j) = omega(i,j)
            else
               dealias(i,j) = (0d0,0d0)
            end if
         end do
      end do
      !$OMP END PARALLEL DO
    end function dealias
    
    subroutine fw_fortran_serial(omega_hat,rhs,u,v,nx,ny)
      !TODO. Separate plan creation from plan execution.
      use, intrinsic :: iso_c_binding
      implicit none
      include 'fftw3.f03'

      integer, intent(in):: nx,ny
      integer:: n,omp_get_num_threads
      complex(kind = 8), dimension(nx,ny), intent(in):: omega_hat
      complex(kind = 8), dimension(nx,ny), intent(out):: rhs,u,v

      !Aux variables. More than needed, you can clean up.
      complex(kind = 8), dimension(nx,ny):: u_hat,v_hat
      complex(kind = 8), dimension(nx,ny):: omega_x_hat,omega_y_hat
      complex(kind = 8), dimension(nx,ny):: omega_x,omega_y
      complex(kind = 8), dimension(nx,ny):: conv

      integer:: i,j
      type(c_ptr):: planu,planv,planox,planoy,planconv

      call fftw_plan_with_nthreads(omp_get_num_threads())
            
      planu = fftw_plan_dft_2d(ny,nx,u_hat,u,FFTW_BACKWARD,FFTW_ESTIMATE)
      planv = fftw_plan_dft_2d(ny,nx,v_hat,v,FFTW_BACKWARD,FFTW_ESTIMATE)
      planox = fftw_plan_dft_2d(ny,nx,omega_x_hat,omega_x,&
           &FFTW_BACKWARD,FFTW_ESTIMATE)
      planoy = fftw_plan_dft_2d(ny,nx,omega_y_hat,omega_y,&
           &FFTW_BACKWARD,FFTW_ESTIMATE)
      planconv = fftw_plan_dft_2d(ny,nx,conv,rhs,FFTW_FORWARD,FFTW_ESTIMATE)

      u_hat = u_hat_f(omega_hat,nx,ny)
      v_hat = v_hat_f(omega_hat,nx,ny)
      omega_x_hat = ddx(omega_hat,nx,ny)
      omega_y_hat = ddy(omega_hat,nx,ny)

      call fftw_execute_dft(planu,u_hat,u)
      call fftw_execute_dft(planv,v_hat,v)
      call fftw_execute_dft(planox,omega_x_hat,omega_x)
      call fftw_execute_dft(planoy,omega_y_hat,omega_y)

      conv = (u*omega_x + v*omega_y)/(nx*ny)
      call fftw_execute_dft(planconv,conv,rhs)
      
      !Renormalize after forward fft
      rhs = rhs/(nx*ny)
      !Dealias with the 3/2 rule
      rhs = dealias(rhs,nx,ny)
      
      !Compute the rhs part of the NS equation.
      !$OMP PARALLEL DO PRIVATE(i,j)
      do j = 1,ny
         do i = 1,nx
            rhs(i,j) = lap(i,j)*omega_hat(i,j)/Re__ - rhs(i,j)
         end do
      end do
      !$END OMP PARALLEL DO

      call fftw_destroy_plan(planu)
      call fftw_destroy_plan(planv)
      call fftw_destroy_plan(planox)
      call fftw_destroy_plan(planoy)
      call fftw_destroy_plan(planconv)

    end subroutine fw_fortran_serial

    function cleanup()
      use, intrinsic :: iso_c_binding
      implicit none
      include 'fftw3.f03'
      integer:: cleanup
      
      call fftw_cleanup_threads()
    end function cleanup


end module rhs_tur2d
