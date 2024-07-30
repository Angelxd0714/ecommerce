# Usa una imagen base con JDK
# Usa una imagen base con Maven y JDK
FROM maven:3.9.8-amazoncorretto-21 as build

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo pom.xml y el directorio src
COPY pom.xml .
COPY src ./src

# Construye el archivo JAR
RUN mvn clean package -DskipTests

# Usa una imagen base con JDK para ejecutar el archivo JAR
FROM openjdk:21-jdk-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo JAR del contenedor de construcción al contenedor de ejecución
COPY --from=build /app/target/auth-service.jar auth-service.jar

# Expone el puerto en el que la aplicación se ejecuta
EXPOSE 8090

# Comando para ejecutar la aplicación
ENTRYPOINT ["java", "-jar", "auth-service.jar"]

