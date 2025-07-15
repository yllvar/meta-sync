# Use a Windows Server Core base image
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# Install Python
RUN powershell -Command \
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.10/python-3.10.10-amd64.exe " -OutFile python-installer.exe; \
    Start-Process -FilePath python-installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait; \
    Remove-Item python-installer.exe

# Install MetaTrader 5
RUN powershell -Command \
    Invoke-WebRequest -Uri "https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/metaquotes-software.corp/mt5/MetaTrader5Setup.exe " -OutFile mt5-installer.exe; \
    Start-Process -FilePath mt5-installer.exe -ArgumentList "/silent" -Wait; \
    Remove-Item mt5-installer.exe

# Set environment variables
ENV PATH="C:\Python310\Scripts;C:\Python310;C:\Program Files\MetaTrader 5\terminal64.exe;%PATH%"

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]