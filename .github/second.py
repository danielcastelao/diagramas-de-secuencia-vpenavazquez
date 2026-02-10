class Second:
    def mensaje(self):
        print("second: procesando mensaje")

        valor_retorno = "Hola desde second"

        return valor_retorno

def main():
    print("Main: iniciando interaccion")

    second = Second()

    respuesta = second.mensaje()

    print("main: valor retornado", respuesta)

if __name__ == "__main__":
    main()