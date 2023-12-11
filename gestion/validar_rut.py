rut = input("ingrese su rut sin el numero verificador :")
rut_list_in = list(rut)
rut_list_in.reverse()
metodo_rut = (2,3,4,5,6,7,2,3)
sumar = 0 

for i in range(8):    
    sumar += metodo_rut[i] * int(rut_list_in[i])

resto = sumar % 11
digito_verificador = 11- resto

if digito_verificador == 10 :
    digito_verificador = 'k'
if digito_verificador == 11:
    digito_verificador = '0'

rut_con_verificador = f"{rut}-{digito_verificador}"
print(f"RUT con dígito verificador: {rut_con_verificador}")