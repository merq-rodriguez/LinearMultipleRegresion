import numpy as np    
import pylab as pl    
from decimal import * 
import math
import pandas as pd

class LeastSquares:
        def __init__(self, x, y):
            self.__x = x
            self.__y = y
            self.R   = 0 # Coeficiente de correlacion
            self.R2  = 0 # Coeficiente de determinacion
            self.A1  = 0 # Pendiente
            self.A0  = 0 # Interseccion
            self.err = 0 # Error estandar
            self.__n = len(x)
        
        def getX(self):
            return self.__x
        
        def getY(self):
            return self.__y
        
        def setErr(self, err):
            self.__err = err
        
        def getSize(self): # Funcion que retorna el numero total de datos 
            return self.__n
        
        def summation(self, array): # Funcion para sumar todos los varores de un vector
            return np.sum(array)
    
        def mean(self, array): # Funcion que calcula la media de un vector
            return np.sum(array)/len(array)
         
        def standardDeviationX(self): # Funcion que calcula la desviacion estandar de X
            return math.sqrt(np.sum(self.DiferenceXAndMediaXSquares())/self.getSize())
        
        def standardDeviationY(self): #Funcion que calcula la desviacion estandar de Y
            return math.sqrt(np.sum(self.DiferenceYAndMediaYSquares())/self.getSize())
        
        def covariance(self): #Funcion que calcula la covarianza
            return np.sum(self.ProductYMediaY_XMediaX()) / self.getSize()
        
        def standardErr(self): #Funcion que calcula el error estandar
            self.err = math.sqrt(np.sum(self.SquareResidue()) / (self.getSize() - 2))
    
        def correlationCoefficient(self): #Funcion que calcula el coeficiente de correlacion del modelo
            self.R = self.covariance() /(self.standardDeviationX() * self.standardDeviationY())
        
        def determinationCoefficient(self): #Funcion que calcula el coeficiente de determinacion del modelo
            self.R2 =  (self.covariance() /(self.standardDeviationX() * self.standardDeviationY()))**2
        
        def normalEquationsB(self): # Ecuacion normal A1  de minimos cuadrados
            numerador = self.getSize() * np.sum(self.ProductXY()) - np.sum(self.getX()) * np.sum(self.getY())
            denominador = self.getSize() * np.sum(self.getX()**2) - (np.sum(self.getX()))**2
            self.A1 =  numerador / denominador
        
        def normalEquationsA(self): # Ecuacion normal A0  de minimos cuadrados
            self.A0 =  self.mean(self.getY()) - self.A1 * self.mean(self.getX())
        
        def DiferenceXAndMediaXSquares(self): # Funcion que calcula el cuadrado de  la diferenia entre las x y la media de las x.
            return (self.getX() - self.mean(self.  getX()))**2
        
        def DiferenceYAndMediaYSquares(self):  # Funcion que calcula el cuadrado de  la diferenia entre las y  la media de las y.
            return (self.getY() - self.mean(self.getY()) )**2
        
        def ProductYMediaY_XMediaX(self): # Funcion que calcula el producto entre  (x-xmedia)(y-ymedia)
            return (self.getX() - self.mean(self.  getX())) * (self.getY() - self.mean(self.getY()))
        
        def ProductXY(self): # Funcion que calcula el producto xy
            return self.getY() * self.getX()
        
        def DiferenceXAndMediaX(self): # Funcion que calcula x - xmedia
            return (self.getX() - self.mean(self.  getX()))
        
        def DiferenceYAndMediaY(self): # Funcion que calcula y - ymedia
            return (self.getY() - self.mean(self.getY()))
        
         #Funcion que calcula la distancia vertical entre el dato y la
         #medida de tendencia central: la línea recta.
        def SquareResidue(self):
            return (self.getY() - self.A0 - self.A1 * self.getX())**2
        
	

        #Funcion que retorna el listado de los resultados del modelo en una tabla
        def getResultTotal(self):
            
            res = [
                np.sum(self.getX()),
                np.sum(self.getY()),
                np.sum(self.getX()**2),
                np.sum(self.getY()**2),
                np.sum(self.DiferenceXAndMediaXSquares()),
                np.sum(self.DiferenceYAndMediaYSquares()),
                np.sum(self.ProductYMediaY_XMediaX()),
                np.sum(self.ProductXY()),
                np.sum(self.SquareResidue()),
                self.R,
                self.R2,
                self.A1,
                self.A0,
                self.err
            ]
            df = pd.DataFrame(res, 
            index=['Σx', 'Σy', 'x²', 'y²', '(x-x̄)²', '(y-ȳ)²', '(x-x̄)(y-ȳ)', 'xy', '(y – A0 - A1X)²', 'R', 'R²', 'Pendiente','Intersección','Error Estandar'], columns=[''])
            return df
       
        # Funcion que retorna el listado de los datos calculados del modelo
        def getData(self):
            data = {
            '(x-x̄)(y-ȳ)' : self.ProductYMediaY_XMediaX(), 
            'x²' : self.getX()**2,
            'y²' : self.getY()**2,
            'x-x̄' : self.DiferenceXAndMediaX(),
            'y-ȳ' : self.DiferenceYAndMediaY(),
            '(x-x̄)²' : self.DiferenceXAndMediaXSquares(),
            '(y-ȳ)²' : self.DiferenceYAndMediaYSquares(),
            'xy' : self.ProductXY(),
            '(y – A0 - A1x)²' : self.SquareResidue()
            }
            self.normalEquationsB()         # Cargamos A1
            self.normalEquationsA()         # Cargamos A0
            self.correlationCoefficient()   # Cargamos R
            self.determinationCoefficient() # Cargamos R2
            self.standardErr()
            df = pd.DataFrame(data)
            return df
        
        def getDataInitial(self): # Visualizar x y y 
            data = {
                'y' : self.getY(),
                'x' : le.getX()
            }
            df = pd.DataFrame(data)
            return df
        
        def getScatterDiagram(self, X, Y): #VIsualizar diagrama de dispersion 
            pl.plot(X,Y, 'o', label='Datos')
            pl.xlabel('x')
            pl.ylabel('y')
            pl.title('Regresion lineal')
            pl.grid()
            pl.legend(loc=4)
            pl.show()
        
        def getAdjustmentLine(self): # VIsualizar linea de ajuste por minimos cuadrados
            A1 = self.A1
            A0 = self.A0
            print(A1)
            print(A0)
            pl.plot(self.getX(),self.getY(), 'o', label='Datos')
            pl.plot(self.getX(),  A1*self.getX() +A0 , label="Ajuste")
            pl.xlabel('x')
            pl.ylabel('y')
            pl.title('Regresion lineal')
            pl.grid()
            pl.legend(loc=4)
            pl.show()
