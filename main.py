from fastapi import FastAPI
import uvicorn
from TallerUsaPed.Usuarios.infrastructure.repository.user_repository_impl import InMemoryUserRepository
from TallerUsaPed.Usuarios.application.services.user_services import UserService
from TallerUsaPed.Usuarios.infrastructure.api.main import router, init_routes

app = FastAPI(title="Microservicio Usuario - UNACH")


repo = InMemoryUserRepository()

service = UserService(repo)


app.include_router(init_routes(service))

if __name__ == "__main__":
  
    uvicorn.run(app, host="0.0.0.0", port=8001)