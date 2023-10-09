# image pythonu
FROM python:3.11
RUN pip install pdm
# vypise se po spusteni image v dockerDesktop
CMD ls -al
# pyproject.toml
# src folder
# pdm.lock

# spusteni buildovani dockeru 
# docker build .
# pojmenovany
# docker build -t cv2 . 
