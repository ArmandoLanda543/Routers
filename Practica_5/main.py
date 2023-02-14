
from fastapi import FastAPI, HTTPException, status
#Importamos la librerias
import bundesliga, eredivise,liga_mx, ligue_1, premier, serie_a, la_liga, computadoras, programas
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel


app=FastAPI()

#Incluir las demás libreria
app.include_router(bundesliga.router)
app.include_router(eredivise.router)
app.include_router(liga_mx.router)
app.include_router(ligue_1.router)
app.include_router(premier.router)
app.include_router(serie_a.router)
app.include_router(la_liga.router)
app.include_router(computadoras.router)
app.include_router(programas.router)







class User(BaseModel): ##ENTIDAD
    PassengerId:int
    Survived:int
    Pclass:int
    Name:str   
    Sex:str
    Age:int

users_list=[User(PassengerId=1, Survived=0, Pclass=3, Name='Braund, Mr. Owen Harris', Sex='male', Age=22),
            User(PassengerId=2, Survived=1, Pclass=1, Name='Cumings, Mrs. John Bradley (Florence Briggs Thayer)', Sex='female',Age=38),
            User(PassengerId=3, Survived=1, Pclass=3, Name= 'Heikkinen, Miss. Laina', Sex='female', Age=26),
            User(PassengerId=4, Survived=1, Pclass=1, Name='Futrelle, Mrs. Jacques Heath (Lily May Peel)', Sex='female', Age=35),]

####################################################    GET     ######################################################
@app.get("/main/{user_id}", status_code=status.HTTP_202_ACCEPTED) #PATH
async def get_user(user_id:int):
    for user in users_list:
        if user.PassengerId==user_id:
            return user
    raise HTTPException(status_code = 204, detail= "Usuario no encontrado")


@app.get("/main", status_code=status.HTTP_200_OK) #QUERY
async def get_users():
    return users_list

####################################################    POST    ######################################################

@app.post("/main", status_code=status.HTTP_201_CREATED) #QUERY
async def userclass(user:User):
    found=False

    for index, save_user in enumerate(users_list):
        if save_user.PassengerId == user.PassengerId:
            raise HTTPException(status_code = 424, detail= "El usuario ya existe" )
    else:
        users_list.append(user)
        return {"message": "Usuario creado exitosamente"}
        return user

###########################put############################################
@app.put("/main/", status_code=status.HTTP_426_UPGRADE_REQUIRED)
async def userclass(user:User):

    found=False #Usamos bandera found para verificar si hemos encontrado el usuario o no

    for index, save_user in enumerate(users_list):      ##TOMA LA POSICION DE DONDE ESTA EL USUARIO
        if save_user.PassengerId == user.PassengerId:     #Si el Id del usuario guardado es igual al Id del usuario nuevo
            users_list[index]=user      #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
            found=True
    if not found:
        raise HTTPException(status_code = 404, detail= "El usuario no existe" )
    else:
        return user
        return {"message": "Usuario actualizado exitosamente"}

###########################DELETE############################################
@app.delete("/main/{id}")
async def usersclass(id:int):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassengerId ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
           found=True
           raise HTTPException(status_code = 410, detail= "El registro se ha eliminado" )
           return "El registro se ha eliminado"
       
    if not found:
        raise HTTPException(status_code = 404, detail= "El registro no se ha encontrado" )