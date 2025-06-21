class Auto:
    def __init__(auto_tipo, marca, modelo):
        auto_tipo.marca = marca
        auto_tipo.modelo = modelo
        auto_tipo.velocidad = 0
        auto_tipo.encendido = False
    
    def encender(auto_tipo):
        if not auto_tipo.encendido:
            auto_tipo.encendido = True
            print(f"El auto {auto_tipo.marca} {auto_tipo.modelo} está encendido.")
        else:
            print("El auto ya estaba encendido.")
    
    def apagar(auto_tipo):
        if auto_tipo.encendido:
            if auto_tipo.velocidad == 0:
                auto_tipo.encendido = False
                print("El auto se apagó.")
            else:
                print("No se puede apagar mientras está en movimiento.")
        else:
            print("El auto ya está apagado.")
    
    def acelerar(auto_tipo, cantidad):
        if auto_tipo.encendido:
            auto_tipo.velocidad += cantidad
            print(f"Velocidad actual: {auto_tipo.velocidad} km/h")
        else:
            print("No se puede acelerar un auto apagado.")
    
    def frenar(auto_tipo, cantidad):
        auto_tipo.velocidad = max(0, auto_tipo.velocidad - cantidad)
        print(f"Velocidad actual: {auto_tipo.velocidad} km/h")
    
    def mostrar_estado(auto_tipo):
        estado = "encendido" if auto_tipo.encendido else "apagado"
        print(f"{auto_tipo.marca} {auto_tipo.modelo} - Velocidad: {auto_tipo.velocidad} km/h - Estado: {estado}")

# Probemos el auto como en el ejemplo
print("\n--- Ejemplo de uso ---")
auto1 = Auto("Toyota", "Corolla")
auto1.mostrar_estado()      # Toyota Corolla - Velocidad: 0 km/h - Estado: apagado
auto1.acelerar(20)          # No se puede acelerar un auto apagado
auto1.encender()            # El auto Toyota Corolla está encendido
auto1.acelerar(20)          # Velocidad actual: 20 km/h
auto1.frenar(10)            # Velocidad actual: 10 km/h
auto1.apagar()              # No se puede apagar mientras está en movimiento
auto1.frenar(10)            # Velocidad actual: 0 km/h
auto1.apagar()              # El auto se apagó