# -*- coding: utf-8 -*-


from __future__ import division
import numpy,pylab

class Vorticity2D(object):
    """                                                    
    Solves Navier-Stokes equations in 2D using the vorticity-current
    function formulation for incompressible flows.
    
    Original code from Adrian Lozano, March 22nd 2011
    Modified version in Matlab by Guillem Borrell, May 23rd 2011
    Ported to Python by Guillem Borrell, December 30th 2011 
    """ 
    def __init__(self,Lx,Ly,Re,CFL):
        """
        The constructor takes the following arguments
              
          *Lx*: float
            Length of the box in the x direction
        
          *Ly*: float
            Length of the box in the y direction
        
          *Re*: float
            Reynolds nuber based on *Lx* or *Ly
        
          *CFL*: float
            CFL number for temporal integration
        """
        self.Re = Re
        self.CFL = CFL
        # Estimate the Kolmogorov scale in the 2D turbulence: 
        # eta = cte/sqrt(Re) 
        nx = 2*numpy.round(0.64*Lx*numpy.sqrt(Re)/2)  # x-modes
        ny = 2*numpy.round(0.64*Ly*numpy.sqrt(Re)/2)  # y-modes
        self.dl = numpy.min([Lx/(nx-1),Ly/(ny-1)]) # minimum mesh size
        
        print 'Lx, Ly: ',Lx,', ',Ly
        print 'number of nx modes: ',nx
        print 'number of ny modes: ',ny
        
        # Low storage RK-4
        self.b   = numpy.array([0,1/6,1/3,1/3,1/6])
        self.a   = numpy.array([0,1/2,1/2,1])
        self.dtv = CFL*self.dl**2*Re
        
        self.kx,self.ky = numpy.meshgrid(
            numpy.mod(numpy.arange(1,nx+1)-numpy.ceil(nx/2+1),nx)-\
                numpy.floor(nx/2),
            numpy.mod(numpy.arange(1,ny+1)-numpy.ceil(ny/2+1),ny)-\
                numpy.floor(ny/2))

        self.kx = self.kx*2*numpy.pi/Lx
        self.ky = self.ky*2*numpy.pi/Ly
        self.Lap = -(self.kx**2+self.ky**2)
        self.poisson = self.Lap
        self.poisson[0,0] = 1
        self.dealias = numpy.logical_and(
            numpy.less(numpy.abs(self.kx*Lx/(2*numpy.pi)),nx/3),
            numpy.less(numpy.abs(self.ky*Ly/(2*numpy.pi)),ny/3))
            
        self.t = 0
        self.dt = 0
        self.omega_hat = numpy.zeros(self.dealias.shape,dtype='complex')
        self.S1 = numpy.zeros(self.omega_hat.shape,dtype='complex')
        
        # Useful to create initial conditions
        self.nx = nx
        self.ny = ny
        

    def set_initial(self,omega):
        """
        Set initial vorticity field once the instance has been created.
        Make sure that the array is (self.nx,self.ny) shaped or you
        will be on serious trouble. 
        """
        self.omega_hat = numpy.fft.fft2(omega)
        self.omega_hat = self.dealias*self.omega_hat
    
    def __FW(self):
        """
        Solve the right hand side, both linear and nonlinear terms
        """
        # Solve poisson equation for psi
        psi_hat = -self.omega_hat/self.poisson
        
        # compute u,v
        u_hat = 1j*self.ky*psi_hat
        v_hat = -1j*self.kx*psi_hat
        
        # convective terms
        u       = numpy.fft.ifft2(u_hat).real
        v       = numpy.fft.ifft2(v_hat).real
        omega_x = numpy.fft.ifft2(1j*self.kx*self.omega_hat).real
        omega_y = numpy.fft.ifft2(1j*self.ky*self.omega_hat).real
        conv    = u*omega_x + v*omega_y
        conv_hat = numpy.fft.fft2(conv)
        conv_hat = self.dealias*conv_hat
        
        return (self.Lap*self.omega_hat/self.Re-conv_hat,u,v)
        
        
    def step(self):
        """
        Integrates a single Runge Kutta time step.
        
        It uses a fourth order low-storage RK scheme and the timestep
        is evaluated at the first substep.
        """
        self.S1 = self.omega_hat+(self.a[0]-self.b[0])*self.dt*self.S1
        self.S1,u,v = self.__FW()
        vmax = numpy.sqrt(u**2+v**2).max()
        self.dt = numpy.min([self.dtv,self.CFL*self.dl/vmax,0.5])
        self.omega_hat = self.omega_hat+self.b[1]*self.dt*self.S1
        
        # Rest of Runge Kutta substeps
        for i in range(1,4):
            self.S1 = self.omega_hat+(self.a[i]-self.b[i])*self.dt*self.S1
            self.S1 = self.__FW()[0]
            self.omega_hat = self.omega_hat+self.b[i+1]*self.dt*self.S1
            
        self.t += self.dt
        
    def result(self):
        """
        Transforms vorticity from Fourier to physical space to make
        pretty plots.
        """
        return numpy.fft.ifft2(self.omega_hat).real

    def velocities(self):
        """
        Returns the velocity components of the result obtained from
        the vorticity field.
        """
        # Solve poisson equation for psi
        psi_hat = -self.omega_hat/self.poisson
        
        # compute u,v
        u_hat = 1j*self.ky*psi_hat
        v_hat = -1j*self.kx*psi_hat
        return (numpy.fft.ifft2(u_hat).real,
                numpy.fft.ifft2(v_hat).real)


def test_tur2d(fign,Lx,Ly):
    """Test a vortex soup"""

    Re = 10000
    CFL = 0.2
    V = Vorticity2D(Lx,Ly,Re,CFL)
    # Genera la distribución inicial

    x,y = numpy.meshgrid(numpy.linspace(-Lx/2,Lx/2,V.nx),
                         numpy.linspace(-Ly/2,Ly/2,V.ny))

    ### Sopa de vórtices. 2-3 segundos por paso.
    omega = numpy.zeros(x.shape)
    nvx= numpy.int(2*Lx);
    nvy= numpy.int(2*Ly);
    vii=2;
    rii=30;
    
    for i in range(nvx):
        for j in range(nvy):
            if j==2 and i==1:
                continue
            if j==3 and i==1:
                continue
            else:
                omega += (-1)**(i+j)*vii*\
                    numpy.exp(-rii*((x+(i-nvx)*Lx/nvx+Lx/2+Lx/nvx/2)**2+\
                                        (y+(j-nvy)*Ly/nvy+Lx/2+Ly/nvy/2)**2))

            
    pylab.figure(fign)
    pylab.clf()
    pylab.imshow(omega,cmap=pylab.cm.RdBu)
    pylab.colorbar()
    pylab.title('Configuracion inicial')


    V.set_initial(omega)
    V.t = 0

    nsteps = 1000
    for i in range(nsteps):
        V.step()
        if i%100 == 0:
            print i,'/',nsteps


    pylab.figure(fign+1)
    pylab.clf()
    pylab.imshow(V.result(),cmap=pylab.cm.RdBu)
    pylab.colorbar()

    return V


def test_kh(fign,Lx,Ly):
    """Test a Kelvin-Helmholtz instability"""
    Re = 10000
    CFL = 0.2

    V = Vorticity2D(Lx,Ly,Re,CFL)
    # Uniform grid mesh
    x,y = numpy.meshgrid(numpy.linspace(-Lx/2,Lx/2,V.nx),
                         numpy.linspace(-Ly/2,Ly/2,V.ny))
    
    # Two shear layers simetrically perturbed. Like a planar
    # infinite jet

    omega = (1+0.1*numpy.cos(numpy.pi*x[0]))*numpy.exp(-300*(y+Ly/4.)**2)
    omega += -(1+0.1*numpy.cos(numpy.pi*x[0]))*numpy.exp(-300*(y-Ly/4.)**2)
        
    pylab.figure(fign)
    pylab.clf()
    pylab.imshow(omega,cmap=pylab.cm.RdBu)
    pylab.colorbar()
    pylab.title('Configuracion inicial')

    V.set_initial(omega)
    V.t = 0
    nsteps = 1000
    for i in range(nsteps):
        V.step()
        if i%100 == 0:
            print i,'/',nsteps

    pylab.figure(fign+1)
    pylab.clf()
    pylab.imshow(V.result(),cmap=pylab.cm.RdBu)

    return V

if __name__ == '__main__':
    #Vort = test_tur2d(1,2.0,2.0)
    KH = test_kh(3,4.0,4.0)

    pylab.show()
