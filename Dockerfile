FROM python:3

# Exposes this container's port 8888 to other containers.
EXPOSE 8888

# Sets the workdir of our container to dir below.
WORKDIR /usr/src/app/Frontman

# Copies our project and its requirements.txt over to the dir above.
COPY Frontman .
COPY config.yml .
COPY requirements.txt .

# Installs the requirements of our project.
RUN pip install --no-cache-dir -r requirements.txt

# Runs the API when the container is ran.
CMD [ "python", "broker.py" ]
