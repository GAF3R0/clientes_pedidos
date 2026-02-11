from fastapi import FastAPI
import uvicorn
from examentaller4.Paciente.Infrastructure.repository.paciente_repository_impl import InMemoryPacienteRepository
from examentaller4.Paciente.application.services.paciente_services import PacienteService
from examentaller4.Paciente.Infrastructure.api.main import router, init_routes

app = FastAPI(title="Microservicio Paciente - UNACH")


repo = InMemoryPacienteRepository()

service = PacienteService(repo)


app.include_router(init_routes(service))

if __name__ == "__main__":
  
    uvicorn.run(app, host="0.0.0.0", port=8001)