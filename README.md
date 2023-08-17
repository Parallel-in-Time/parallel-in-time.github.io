# How to setup the project for local development

## I. Requirements

- You need docker installed on your computer
  - Link to [Docker Engine](https://docs.docker.com/engine/install/)
  - Link to [Docker Desktop (optional)](https://docs.docker.com/get-docker/)

## II. Run the local development

### Install all dependencies

We use **docker** to *prevent version* and *system differences*. So please, especially if you are a mac user, use the docker container.

#### Run this in your console to update your dependencies

```bash
docker-compose -f docker-compose-bundle.yml up
```

### Start the live preview of the page

**Note:** The **live reload** of jekyll is not perfect. Therefore, **don't expect** it to work as intended. Sometimes, you need to <u>re-run the command</u> in order to see the **newest changes**.

#### Run this in your console to start the local preview

```bash
docker-compose up
```

## III. Troubleshooting

If the live preview fails and you don't know the cause, follow these steps:

1. You installed the dependencies in the past

    Chances are that the dependencies are not compatible if you once installed the dependencies a long time ago.

    Steps to fix it:
    - delete `vendor` folder
    - delete `Gemfile.lock` folder
    - re-install dependencies

2. Your ports are already used by an other program

    If you are running another program that requires either **port 4000** or **port 35729**, the preview will fail.

    Steps to fix it:
    - either close the program(s) that need(s) the port(s)
    - or specify another port

    If you want to specify another port go to the docker compose file, append one of the args to the bash script that the docker container will run:

    - `--port [YOUR PORT]` (the port where the page is accessible at)
    - `--livereload-port [YOUR PORT]` (the port where the live reload script is accessible at)

    &rarr; append the arg(s) to the bash command:

    ```bash
     ... && bundle exec jekyll serve --livereload --host=0.0.0.0 --port=[PORT] --livereload-port=[PORT]
    ```

3. You decided not to run it in the docker container

    If you did, then please run it in the container.

4. Other causes

    If you tried every troubleshooting method and none of them worked: We are sorry, but you need to find the error by your own.
