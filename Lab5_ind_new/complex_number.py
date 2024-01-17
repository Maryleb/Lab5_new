import math


#trigonometry |z|(cos phi + i sin phi)
#exponential |z|*e^(i* phi)
class Complex:

    module : float
    phi : float

    def __init__(self, _modulo, _phi):
        self.phi=_phi
        self.module = _modulo

    def __add__(self, o):
        pass 
    def __sub__(self,o):
        pass
    def __truediv__(self, o):
        return Complex(self.module/o.module,self.phi-o.phi)
    def __mul__(self, o):
        return Complex(self.module*o.module,self.phi+o.phi)  


def compl_division(first_module,first_phi,second_module,second_phi, format):
    new_number = Complex(first_module/second_module,first_phi-second_phi)
    new_number.module=round(new_number.module,3)
    new_number.phi=round(new_number.phi,3)
    if format=="показательная":
        return str(new_number.module) + "e^(i*" +str(new_number.phi) +")"
    return str(new_number.module) + "(cos(" +str(new_number.phi) +") + i * sin (" + str(new_number.phi)+"))"



def compl_sub(first_module,first_phi,second_module,second_phi,format):
    first_a = first_module*math.cos(first_phi)
    first_b = first_module*math.sin(first_phi)
    second_a = second_module*math.cos(second_phi)
    second_b = second_module*math.sin(second_phi)
    new_a = first_a-second_a
    new_b = first_b-second_b
    new_module = math.sqrt(new_a**2+new_b**2)
    new_phi = math.acos(new_a/new_module)
    new_number = Complex(new_module,new_phi)
    
    new_number.module=round(new_number.module,3)
    new_number.phi=round(new_number.phi,3)
    if format=="показательная":
        return str(new_number.module) + "e^(i*" +str(new_number.phi) +")"
    return str(new_number.module) + "(cos(" +str(new_number.phi) +") + i * sin (" + str(new_number.phi)+"))"


def compl_sum(first_module,first_phi,second_module,second_phi,format):
    first_a = first_module*math.cos(first_phi)
    first_b = first_module*math.sin(first_phi)
    second_a = second_module*math.cos(second_phi)
    second_b = second_module*math.sin(second_phi)
    new_a = first_a+second_a
    new_b = first_b+second_b
    new_module = math.sqrt(new_a**2+new_b**2)
    new_phi = math.acos(new_a/new_module)
    new_number = Complex(new_module,new_phi)
    
    new_number.module=round(new_number.module,3)
    new_number.phi=round(new_number.phi,3)
    if format=="показательная":
        return str(new_number.module) + "e^(i*" +str(new_number.phi) +")"
    return str(new_number.module) + "(cos(" +str(new_number.phi) +") + i * sin (" + str(new_number.phi)+"))"

do_operation={
    "частное": compl_division,
    "разность": compl_sub,
    "сумма" : compl_sum
}