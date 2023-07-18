# using ubuntu LTS version
FROM ubuntu:20.04 AS builder-image

# avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update  \
    && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential \
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/*

# create and activate virtual environment
# using final folder name to avoid path issues with packages
RUN python3.9 -m venv /home/django/venv
ENV PATH="/home/django/venv/bin:$PATH"

# install requirements
COPY requirements.txt .
RUN pip3 install --no-cache-dir wheel -i https://mirrors.aliyun.com/pypi/simple
RUN pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

FROM ubuntu:20.04 AS runner-image

LABEL maintainer="heyares@163.com"

ENV TZ "Asia/Shanghai"

RUN apt-get update  \
    && apt-get install --assume-yes --no-install-recommends -y python3.9 python3-venv  \
    && apt-get clean  \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home django
COPY --from=builder-image /home/django/venv /home/django/venv

USER django
RUN mkdir -p /home/django/workspace
WORKDIR /home/django/workspace
COPY . .

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/home/django/venv
ENV PATH="/home/django/venv/bin:$PATH"

#USER django
CMD ["bash", "-c", "./entrypoint.sh"]