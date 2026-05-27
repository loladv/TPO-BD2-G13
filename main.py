# main.py — dispatcher de las 15 consultas/servicios
import sys
# main minimo para probar codespaces:
def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <numero_consulta> [args...]")
        print("Ej: python main.py 1")
        sys.exit(1)
    n = sys.argv[1]
    print(f"Consulta/servicio #{n} todavía no implementado.")

if __name__ == "__main__":
    main()
