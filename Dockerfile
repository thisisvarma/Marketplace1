from python:3.8.6

RUN mkdir /code
workdir /code
copy . /code

RUN echo "deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list

RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections

# RUN apt-get update && \
# 	apt-get -y install mysql-server-5.7 && \
# 	mkdir -p /var/lib/mysql && \
# 	mkdir -p /var/run/mysqld && \
# 	mkdir -p /var/log/mysql && \
# 	chown -R mysql:mysql /var/lib/mysql && \
# 	chown -R mysql:mysql /var/run/mysqld && \
# 	chown -R mysql:mysql /var/log/mysql

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server=${MYSQL_VERSION}* \
 && rm -rf ${MYSQL_DATA_DIR} \
 && rm -rf /var/lib/apt/lists/*

# UTF-8 and bind-address
RUN sed -i -e "$ a [client]\n\n[mysql]\n\n[mysqld]"  /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[client\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysql\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && \
	sed -i -e "s/\(\[mysqld\]\)/\1\ninit_connect='SET NAMES utf8'\ncharacter-set-server = utf8\ncollation-server=utf8_unicode_ci\nbind-address = 0.0.0.0/g" /etc/mysql/my.cnf

VOLUME /var/lib/mysql

COPY ./startup.sh /root/startup.sh
RUN chmod +x /root/startup.sh

ENTRYPOINT ["/root/startup.sh"]

EXPOSE 3306
CMD ["/usr/bin/mysqld_safe"]

# arg database_hostname
# arg databse_username
# arg database_password
# arg database_port
#
# env database_hostname = ${database_hostname}
# env databse_username = ${databse_username}
# env database_password = ${database_password}
# env database_port = ${database_port}

run python -m pip install --upgrade pip
run pip install -r requirements.txt
# run python3 /code/GiveUp/manage.py runserver 8080