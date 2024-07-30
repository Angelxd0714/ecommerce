# Usa una imagen base con JDK
FROM openjdk:21-jdk-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo JAR del servicio al contenedor
COPY target/auth-service.jar auth-service.jar

# Expone el puerto en el que la aplicación se ejecuta
EXPOSE 8090

# Comando para ejecutar la aplicación
ENTRYPOINT ["java", "-jar", "auth-service.jar"]
