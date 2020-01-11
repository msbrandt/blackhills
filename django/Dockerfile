FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get -y install sqlite3 

RUN apt-get -y install gdal-bin binutils libproj-dev libgdal-dev

##GEOS
#RUN wget http://download.osgeo.org/geos/geos-3.7.0.tar.bz2 \
#    && tar xjf geos-3.7.0.tar.bz2 \
#    && cd geos-3.7.0 \
#    && ./configure \
#    && make \
#    &&  make install \
#    && cd ..

##PROJ.6
#RUN wget http://download.osgeo.org/proj/proj-6.2.1.tar.gz \
#    && wget http://download.osgeo.org/proj/proj-datumgrid-1.8.tar.gz \
#    && tar xzf proj-6.2.1.tar.gz \
#    && cd proj-6.2.1 \
#    && tar xzf ../../proj-datumgrid-1.8.tar.gz \
#    && ./configure \
#    && make \
#    && make install \
#    && cd .. 

##GDAL
#RUN wget http://download.osgeo.org/gdal/3.0.1/gdal-3.0.1.tar.gz \
#    && tar xzf gdal-3.0.1.tar.gz \
#    && cd gdal-3.0.1 \
#    && ./configure \
#    && make \
#    && make install

##NEEDED JAVA FOR A DIFFERENT PACKAGE. NO LONGER NEED THIS..
#todo: weget slim-java so we do not need to include it in the repo...
#RUN rm -rf /var/lib/apt/lists/* && apt-get clean && apt-get update && apt-get upgrade -y \
#    && apt-get install -y --no-install-recommends curl ca-certificates \
#    && rm -rf /var/lib/apt/lists/*
#
#ENV JAVA_VERSION jdk-11.0.2+7
#
#COPY slim-java* /usr/local/bin/
#
#RUN set -eux; \
#    ARCH="$(dpkg --print-architecture)"; \
#    case "${ARCH}" in \
#       ppc64el|ppc64le) \
#         ESUM='c18364a778b1b990e8e62d094377af48b000f9f6a64ec21baff6a032af06386d'; \
#         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.1%2B13/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.1_13.tar.gz'; \
#         ;; \
#       s390x) \
#         ESUM='e39aacc270731dadcdc000aaaf709adae7a08113ccf5b4a045bc87fc13458d71'; \
#         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11%2B28/OpenJDK11-jdk_s390x_linux_hotspot_11_28.tar.gz'; \
#         ;; \
#       amd64|x86_64) \
#         ESUM='d89304a971e5186e80b6a48a9415e49583b7a5a9315ba5552d373be7782fc528'; \
#         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.2%2B7/OpenJDK11U-jdk_x64_linux_hotspot_11.0.2_7.tar.gz'; \
#         ;; \
#       aarch64|arm64) \
#         ESUM='b66121b9a0c2e7176373e670a499b9d55344bcb326f67140ad6d0dc24d13d3e2'; \
#         BINARY_URL='https://github.com/AdoptOpenJDK/openjdk11-binaries/releases/download/jdk-11.0.1%2B13/OpenJDK11U-jdk_aarch64_linux_hotspot_11.0.1_13.tar.gz'; \
#         ;; \
#       *) \
#         echo "Unsupported arch: ${ARCH}"; \
#         exit 1; \
#         ;; \
#    esac; \
#    curl -Lso /tmp/openjdk.tar.gz ${BINARY_URL}; \
#    sha256sum /tmp/openjdk.tar.gz; \
#    mkdir -p /opt/java/openjdk; \
#    cd /opt/java/openjdk; \
#    echo "${ESUM}  /tmp/openjdk.tar.gz" | sha256sum -c -; \
#    tar -xf /tmp/openjdk.tar.gz; \
#    jdir=$(dirname $(dirname $(find /opt/java/openjdk -name javac))); \
#    mv ${jdir}/* /opt/java/openjdk; \
#    export PATH="/opt/java/openjdk/bin:$PATH"; \
#    apt-get update; apt-get install -y --no-install-recommends binutils; \
#    /usr/local/bin/slim-java.sh /opt/java/openjdk; \
#    apt-get remove -y binutils; \
#    rm -rf /var/lib/apt/lists/*; \
#    rm -rf ${jdir} /tmp/openjdk.tar.gz;
#
#ENV JAVA_HOME=/opt/java/openjdk \
#    PATH="/opt/java/openjdk/bin:$PATH"
#ENV JAVA_TOOL_OPTIONS="-XX:+UseContainerSupport"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install -r requirements.txt
#RUN pip install -r requirements.txt
#RUN python -m pip install djangorestframework
COPY . /code/

