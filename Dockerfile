FROM python:3.13-slim
RUN useradd --create-home app
WORKDIR /app
COPY security/lab/health_service.py /app/health_service.py
USER app
EXPOSE 8080
CMD ["python","/app/health_service.py"]
