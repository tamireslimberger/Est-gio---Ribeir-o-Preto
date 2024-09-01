import time
import random

def simular_lampadas():
    """Simula a conexão entre interruptores e lâmpadas."""
    interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
    lampadas = ["Lâmpada A", "Lâmpada B", "Lâmpada C"]
    random.shuffle(lampadas)  # Embaralha a lista de lâmpadas
    return dict(zip(interruptores, lampadas))

def mostrar_estado_lampadas(lampadas, estados):
    """Mostra o estado atual das lâmpadas (acesa ou apagada)."""
    for interruptor, lampada in lampadas.items():
        estado = estados.get(lampada, "Desconhecido")
        print("{} controla {} e a lâmpada está {}.".format(interruptor,lampada,estado))

def main():
    print("Simulação do controle das lâmpadas:")

    # Simulação das lâmpadas
    lampadas = simular_lampadas()

    # Estado das lâmpadas: "acesa" ou "apagada"
    estados = {
        lampadas["Interruptor 1"]: "quente e apagada",  # A primeira lâmpada ligada por um tempo
        lampadas["Interruptor 2"]: "acesa",  # A segunda lâmpada ligada agora
        lampadas["Interruptor 3"]: "apagada"  # A terceira lâmpada nunca ligada
    }

    print("\nPrimeira ida às lâmpadas:")
    mostrar_estado_lampadas(lampadas, estados)

    # Simula a segunda ida e verificação das lâmpadas
    print("\nSegunda ida às lâmpadas:")
    for interruptor in lampadas:
        print("{}: {}".format(interruptor,lampadas[interruptor]))

if __name__ == "__main__":
    main()