# 💻 IT Support Request System (Java Swing)

Aplicación de escritorio desarrollada en **Java Swing** para la gestión e ingreso de incidencias de soporte técnico de IT. Incluye formularios interactivos, menú desplegable de categorías, validación de campos y cuadro de diálogo de confirmación con `JOptionPane`.

---

## 📸 Demostración Visual / Pasos del Sistema

### Paso 1: Interfaz Limpia e Intuitiva
Formulario inicial diseñado con componentes Swing (`JLabel`, `JTextField`, `JComboBox`, `JButton`).

### Paso 2: Entrada de Datos y Categorización
El usuario ingresa el nombre del solicitante, la etiqueta del equipo y selecciona el tipo de incidencia (**Hardware**, **Software**, **Network**, **Internet**).

### Paso 3: Lógica Basada en Eventos y Confirmación
Al hacer clic en **Submit Request**, el sistema captura los datos, procesa la solicitud y genera un cuadro de diálogo descriptivo (`JOptionPane.showMessageDialog`) con el resumen de la incidencia.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Java (JDK 25)[cite: 9]
* **GUI Framework:** Java Swing
* **Gestor de Construcción:** Maven[cite: 9]
* **Entorno de Desarrollo:** NetBeans IDE

---

## 🚀 Cómo ejecutar el proyecto
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/mapg2310-png/java-swing-it-support-request.git](https://github.com/mapg2310-png/java-swing-it-support-request.git)
