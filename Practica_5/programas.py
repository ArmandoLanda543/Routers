#Se importa la libreria de FastAPI, para hacer ROUTERS
from fastapi import APIRouter, HTTPException, status
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class Team(BaseModel): ##ENTIDAD
    Id:int
    Name:str
    CreationYear:int
    UserForYear:int

team_list = [Team(Id=1, Name='Python', CreationYear= 1991 , UserForYear=100000),
            Team(Id=2, Name='JAVA', CreationYear= 1995 , UserForYear=210000)]

####################################################    GET     ######################################################
@router.get("/programas/{user_id}", status_code=status.HTTP_202_ACCEPTED) #PATH
async def get_user(user_id:int):
    for user in team_list:
        if user.Id==user_id:
            return user
    raise HTTPException(status_code = 204, detail= "Lenguaje de Programacion Encontrado")


@router.get("/programas", status_code=status.HTTP_200_OK) #QUERY
async def get_users():
    return team_list

####################################################    POST    ######################################################

@router.post("/programas", status_code=status.HTTP_201_CREATED) #QUERY
async def userclass(user:Team):
    found=False

    for index, save_user in enumerate(team_list):
        if save_user.Id == user.Id:
            raise HTTPException(status_code = 424, detail= "Lenguaje de Programacion ya existe" )
    else:
        team_list.append(user)
        return {"message": "Lenguaje de Programacion creado con Exito!!"}
        return user

###########################put############################################
@router.put("/programas/", status_code=status.HTTP_426_UPGRADE_REQUIRED)
async def userclass(user:Team):

    found=False #Usamos bandera found para verificar si hemos encontrado el usuario o no

    for index, save_user in enumerate(team_list):      ##TOMA LA POSICION DE DONDE ESTA EL USUARIO
        if save_user.Id == user.Id:     #Si el Id del usuario guardado es igual al Id del usuario nuevo
            team_list[index]=user      #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
            found=True
    if not found:
        raise HTTPException(status_code = 404, detail= "No se encontro Lenguaje de Programacion" )
    else:
        return user
        return {"message": "Lenguaje de Programacion Actualizado con Exito!!"}

###########################DELETE############################################
@router.delete("/programas/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(team_list):
        if saved_user.Id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del team_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code = 410, detail= "Lenguaje de Programacion eliminado" )
           return "El registro se ha eliminado"
       
    if not found:
        raise HTTPException(status_code = 404, detail= "Lenguaje de Programacion no se encontró" )