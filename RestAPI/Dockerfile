FROM python:3.10
#port
EXPOSE 5000
#work directory
WORKDIR /app
# install statement needed
RUN pip install flask
#copys all the code in the current directory to the docker image
COPY . .
#command that runs the application
CMD ["flask", "run", "--host", "0.0.0.0"]

## Build docker image
  # `docker build -t <image-name> .`      (dot is for current directory)
## Run docker from command line:
  # `docker run -p 5005:5000 <image-name>`
    #(image name I've created: rest-apis-flask-python)
    # -p is the docker port to the app port
    # Ctrl + C to quit/stop the container
  # `docker run -d -p 5005:5000 rest-apis-flask-python`
    # -d runs the app in the background as a daemon so you can continue using the terminal
