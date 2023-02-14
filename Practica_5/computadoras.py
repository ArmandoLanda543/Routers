#Se importa la libreria de FastAPI, para hacer ROUTERS
from fastapi import APIRouter, HTTPException, status
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class Caracterisicas(BaseModel): ##ENTIDAD
    Id:int
    Marca:str
    Precio:int
    Descuento:int

computer_list = [Caracterisicas(Id=1, Marca='Intel', Precio=354403 , Descuento=40),
            Caracterisicas(Id=2, Marca='AMD', Precio= 150099 , Descuento=30)]

####################################################    GET     ######################################################
@router.get("/computadoras/{user_id}", status_code=status.HTTP_202_ACCEPTED) #PATH
async def get_user(user_id:int):
    for user in computer_list:
        if user.Id==user_id:
            return user
    raise HTTPException(status_code = 204, detail= "Equipo de Computo no Encontrado")


@router.get("/computadoras", status_code=status.HTTP_200_OK) #QUERY
async def get_users():
    return computer_list

####################################################    POST    ######################################################

@router.post("/computadoras", status_code=status.HTTP_201_CREATED) #QUERY
async def userclass(user:Caracterisicas):
    found=False

    for index, save_user in enumerate(computer_list):
        if save_user.Id == user.Id:
            raise HTTPException(status_code = 424, detail= "Este Equipo de computo ya existe" )
    else:
        computer_list.append(user)
        return {"message": "Equipo de computo Creado con Exito!!"}
        return user

###########################put############################################
@router.put("/computadoras/", status_code=status.HTTP_426_UPGRADE_REQUIRED)
async def userclass(user:Caracterisicas):

    found=False #Usamos bandera found para verificar si hemos encontrado el usuario o no

    for index, save_user in enumerate(computer_list):      ##TOMA LA POSICION DE DONDE ESTA EL USUARIO
        if save_user.Id == user.Id:     #Si el Id del usuario guardado es igual al Id del usuario nuevo
            computer_list[index]=user      #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
            found=True
    if not found:
        raise HTTPException(status_code = 404, detail= "No se encontro al Equipo de computo" )
    else:
        return user 
        return {"message": "Equipo de computo Actualizado con Exito!!"}
 
###########################DELETE############################################
@router.delete("/computadoras/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(computer_list):
        if saved_user.Id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del computer_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code = 410, detail= "El equipo de computo fue Eliminado" )
           return "El registro se ha eliminado"
       
    if not found:
        raise HTTPException(status_code = 404, detail= "El equipo de computo no fue encontrado" )