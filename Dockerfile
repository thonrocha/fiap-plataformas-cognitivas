FROM python:3-alpine
COPY . .
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt
CMD ["python", "./teste.py"]
