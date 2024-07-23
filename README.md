# Dialoger ( Диалогер )

This is our educational messenger pet-project

## Installation
```bash
git clone https://github.com/sonoma-org/dialoger
```

## Requirements

To work you need a PostgreSQL database ( You can find an example of docker compose here `docker/docker-compose.yaml` )

### Building and running the main service

*! Java 11+ must be installed !*
*You must also add an environment variable - `AUTH_ADDRESS` with the address of the authorization service*

###### Windows
```bash
gradlew build
gradlew run -D AUTH_ADDRESS=http://127.0.0.1:1211/
```
###### MacOS/Linux
```bash
chmod +x ./gradlew
./gradlew build
AUTH_ADDRESS=http://127.0.0.1:1211/ ./gradlew run
```
##### Docker
```bash
docker build -t <IMAGE_NAME> .
docker run docker run -p 8080:8080 <IMAGE_NAME>
```

### Building and running the auth service
*! Python 3.12+ must be installed !*
To run from a bot with the debug logging level, use:
`python app/main.py --debug=True`

**Before that:**
```bash
cd src/main/python/
```

###### Windows
```bash
pip install -r requirements.txt
python main.py
```
###### MacOS/Linux
```bash
pip3 install -r requirements.txt
python3 main.py
```
##### Docker
```bash
docker build -t <IMAGE_NAME> .
docker run docker run -p 1211:1211 <IMAGE_NAME>
```
