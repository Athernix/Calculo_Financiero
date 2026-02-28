# Calculo_Financiero

## Descripción
Calculadora financiera multi-propósito con interfaz gráfica desarrollada en Python usando Tkinter.

## Características
- Interfaz gráfica moderna y responsive
- Diseño limpio con colores corporativos
- Sistema de pestañas para diferentes cálculos financieros
- Formulario de bienvenida con validación
- Diseño adaptable a diferentes tamaños de pantalla

## Tecnologías
- **Lenguaje**: Python 3.x
- **GUI**: Tkinter (biblioteca estándar de Python)
- **Diseño**: Grid y Pack geometry managers
- **Iconos**: Pillow (PIL) para manejo de imágenes

## Estructura del Proyecto
```
Calculo_Financiero/
├── main.py                 # Punto de entrada de la aplicación
├── README.md              # Este archivo
├── UI/
│   ├── __init__.py
│   └── Views/
│       ├── __init__.py
│       ├── ui_manin.py    # Ventana principal con pestañas
│       └── ui_welcome.py  # Pantalla de bienvenida
└── assets/
    └── images/
        └── logo.png         # Logo de la aplicación
```

## Requisitos
- Python 3.6 o superior
- Bibliotecas estándar de Python (tkinter, os, sys, math)
- Pillow (para manejo de imágenes): `pip install Pillow`

## Instalación
1. Clonar o descargar el repositorio
2. Navegar al directorio del proyecto
3. Instalar dependencias (si aplica):
   ```bash
   pip install Pillow
   ```

## Uso
Ejecutar la aplicación:
```bash
python main.py
```

## Características Principales

### 1. Pantalla de Bienvenida
- Formulario con validación de campos
- Botón de inicio de sesión
- Manejo de errores con mensajes visuales
- Diseño responsive con colores corporativos

### 2. Ventana Principal
- **Pestaña 1**: Cálculo de Interés Simple
- **Pestaña 2**: Cálculo de Interés Compuesto
- **Pestaña 3**: Cálculo de Anualidades
- **Pestaña 4**: Cálculo de Amortización
- **Pestaña 5**: Cálculo de Valor Presente Neto (VPN)
- **Pestaña 6**: Cálculo de Tasa Interna de Retorno (TIR)

### 3. Diseño Responsive
- Adaptable a diferentes tamaños de pantalla
- Layout optimizado para resoluciones estándar
- Colores corporativos: #003366 (azul), #FFFFFF (blanco), #F0F0F0 (gris claro)

## Personalización
El código está estructurado para facilitar la adición de nuevas funcionalidades:
1. Crear un nuevo archivo en `UI/Views/` con la lógica del cálculo
2. Importar el archivo en `ui_manin.py`
3. Agregar una nueva pestaña en la ventana principal
4. Conectar los widgets con la lógica del cálculo

## Contribución
1. Fork el repositorio
2. Cree una rama para su feature (`git checkout -b feature/AmazingFeature`)
3. Commit sus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abra un Pull Request

## Licencia
[Indique aquí la licencia del proyecto]

## Contacto
[Información de contacto del desarrollador]

## Notas Adicionales
- El código utiliza programación orientada a objetos para mejor mantenibilidad
- Los colores corporativos están definidos como constantes en `ui_welcome.py`
- El diseño es completamente responsive y se adapta a diferentes tamaños de pantalla
- La aplicación incluye validación de entrada de datos en todos los formularios
