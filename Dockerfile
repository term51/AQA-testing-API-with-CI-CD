#  базовый образ, легковесный alpine3 с python
FROM python:3.10-alpine3.19

# Устанавливаем зависимости OS
RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz && \
    apk add --no-cache python3-dev

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/workspace

# Копируем файлы в контейнер
COPY ./requirements.txt /usr/workspace

# Устанавливаем зависимости APP
RUN pip3 install -r requirements.txt

# Указываем команду для запуска приложения
#CMD ["python", "app.py"]
