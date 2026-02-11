from fastapi import FastAPI
import uvicorn
from examentaller4.Doctor.Infrastructure.repository.doctor_repository_impl import InMemoryDoctorRepository
from examentaller4.Doctor.application.services.doctor_services import DoctorService
from examentaller4.Doctor.Infrastructure.api.main import router, init_routes

app = FastAPI(title="Microservicio Doctores - UNACH")


repo = InMemoryDoctorRepository()

service = DoctorService(repo)


app.include_router(init_routes(service))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)