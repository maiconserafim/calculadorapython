import time

def cronometro():
    input("Pressione Enter para iniciar o cronômetro...")
    print("Cronômetro iniciado. Pressione Enter para parar.")
    inicio = time.time()

    try:
        while True:
            if input() == "":
                tempo_decorrido = time.time() - inicio
                minutos, segundos = divmod(tempo_decorrido, 60)
                horas, minutos = divmod(minutos, 60)
                print(f"Tempo decorrido: {int(horas)}h {int(minutos)}m {int(segundos)}s")
    except KeyboardInterrupt:
        print("\nCronômetro parado.")

if __name__ == "__main__":
    cronometro()
