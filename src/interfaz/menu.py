"""
Módulo de menú principal.
Gestiona la interfaz de consola y la navegación del usuario.
"""


def mostrar_menu_principal():
    """
    Muestra el menú principal y gestiona las opciones del usuario.
    """
    while True:
        print("\n" + "=" * 70)
        print("  MENÚ PRINCIPAL")
        print("=" * 70)
        print("\nRecuperación de Información en la Web")
        print("-" * 70)
        print()
        print("1. Consultar artículos científicos (OpenAlex)")
        print("2. Consultar patentes (The Lens)")
        print("3. Consultar próximos eventos y ferias (Web Scraping)")
        print("4. Consultar últimas noticias de comercio exterior (RSS)")
        print("5. Ver archivos CSV generados")
        print("6. Acerca de")
        print("7. Salir")
        print()

        opcion = input("Seleccione una opción [1-7]: ").strip()

        if opcion == "1":
            print("\n⚠️  Función no implementada aún.")
            print("📝 TODO: Implementar consulta a OpenAlex API")
        elif opcion == "2":
            print("\n⚠️  Función no implementada aún.")
            print("📝 TODO: Implementar consulta a The Lens API")
        elif opcion == "3":
            print("\n⚠️  Función no implementada aún.")
            print("📝 TODO: Implementar web scraping de eventos")
        elif opcion == "4":
            print("\n⚠️  Función no implementada aún.")
            print("📝 TODO: Implementar procesamiento de RSS feeds")
        elif opcion == "5":
            print("\n⚠️  Función no implementada aún.")
            print("📝 TODO: Implementar visualización de archivos CSV")
        elif opcion == "6":
            mostrar_acerca_de()
        elif opcion == "7":
            confirmar = input("\n¿Está seguro que desea salir? [S/N]: ").strip().upper()
            if confirmar == "S":
                print("\n✅ ¡Gracias por usar el sistema!")
                print("📚 Documentación disponible en: ./docs/")
                print("\n¡Hasta luego! 👋\n")
                break
        else:
            print("\n❌ Opción inválida. Por favor, seleccione una opción del 1 al 7.")

        input("\nPresiona Enter para continuar...")


def mostrar_acerca_de():
    """
    Muestra información sobre el proyecto.
    """
    print("\n" + "=" * 70)
    print("  ACERCA DE")
    print("=" * 70)
    print()
    print("📚 Trabajo Práctico: Recuperación de Información en la Web")
    print()
    print("🎓 Universidad Nacional de Tres de Febrero")
    print("   Licenciatura en Informática")
    print("   Estructuras de Datos y Algoritmos")
    print()
    print("👥 Equipo de Desarrollo:")
    print("   - [Completar con nombres del equipo]")
    print()
    print("📅 Fecha: Noviembre 2025")
    print()
    print("🛠️ Tecnologías utilizadas:")
    print("   - Python 3.x")
    print("   - requests (APIs y HTTP)")
    print("   - BeautifulSoup (Web Scraping)")
    print("   - feedparser (RSS)")
    print("   - pandas (Manipulación de datos)")
    print()
    print("🌐 Fuentes de datos:")
    print("   - OpenAlex (artículos científicos)")
    print("   - The Lens (patentes)")
    print("   - eventseye.com, nferias.com, 10times.com (eventos)")
    print("   - WTO y UN Comtrade (noticias RSS)")
    print()
