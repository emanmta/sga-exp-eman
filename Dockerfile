FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install UV
RUN pip install uv

COPY pyproject.toml uv.lock /app/

RUN sed -i '/pywin32/d' /app/uv.lock
RUN uv pip sync --system /app/uv.lock


# Copy the rest of the code
# Copy the application code into the container
COPY ./app /app/app
COPY run.py /app/

# Expose port
EXPOSE 8000

# Command to run FastAPI
# Command to run the application using our custom script
CMD ["python", "run.py"]
