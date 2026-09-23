# Actividad 6 — Resolución completa

**Materia:** Auditoría de Sistemas de Información
**Teoría aplicada:** Clase 5 — Errores, faltas y fallas · Casos de prueba (estructura, tipos y métodos)
**Fecha:** 23/09/2026 · *Consigna actualizada*

> **Criterio de calificación (consigna actualizada).** El Ejercicio 1 se califica como **Satisfactoria (S) / No Satisfactoria (NS)**. Los Ejercicios 2 a 5 se califican como **Favorable (F) / No Favorable (NF)**, según los alcances de la cátedra: **F = se encontraron errores** (la ejecución evidenció fallas) · **NF = funciona correctamente** (sin errores).

---

## Marco teórico aplicado (Clase 5)

- **Prueba (test):** proceso de ejecutar un programa con el fin de encontrar fallas.
- **Caso de prueba:** datos de entrada, condiciones de ejecución y resultado esperado (identificador, descripción, precondiciones, pasos, datos de entrada, resultados esperados y reales).
- **Tipos de casos de prueba:** funcionales, no funcionales, de regresión y de seguridad.
- **Métodos:** *caja blanca* (se parte del código) y *caja negra* (se parte de los requerimientos: se introducen entradas y se examinan las salidas).

---

## Ejercicio 1 — Login de acceso a Historias Clínicas «sysMED» (Sanatorio «San Martín Salud»)

**Objetivo:** diseñar y ejecutar cinco casos de prueba que validen el módulo de ingreso de médicos y enfermeros.

### Precondiciones generales del entorno

1. sysMED desplegado y accesible desde la red del sanatorio.
2. Base de usuarios con credenciales vigentes y roles asignados (Médico, Enfermero).
3. Servicio de autenticación operativo y registro de auditoría (log) habilitado.

### Tabla de casos de prueba y resultados

| N° | Caso de prueba | Precondiciones | Resultado esperado | Resultado obtenido | Calificación |
|:--:|---|---|---|---|:--:|
| 1 | Login exitoso de un médico con credenciales válidas | Usuario «dr.gomez» activo, rol Médico, contraseña vigente | El sistema valida las credenciales y accede al panel de Historias Clínicas con las funciones del rol Médico; registra el ingreso en el log | Acceso concedido; panel del rol Médico disponible; ingreso asentado en el log de auditoría | **S** |
| 2 | Login exitoso de un/a enfermero/a con credenciales válidas | Usuario «enf.lopez» activo, rol Enfermero, contraseña vigente | Acceso a las funciones de enfermería (registro de signos vitales y consulta de HC), sin permisos de prescripción | Acceso concedido; menú restringido correctamente al rol Enfermero | **S** |
| 3 | Contraseña incorrecta | Usuario «dr.gomez» activo; se ingresa una contraseña errónea | Deniega el acceso con mensaje genérico («Usuario o contraseña incorrectos»), sin crear sesión, y registra el intento | Acceso denegado; mensaje genérico mostrado; sin sesión iniciada; intento registrado en el log | **S** |
| 4 | Campos obligatorios vacíos | Formulario de login desplegado, sin datos ingresados | Muestra «Debe completar usuario y contraseña» y no envía la solicitud de autenticación | Validación mostrada; la petición no se envió | **S** |
| 5 | Bloqueo por intentos fallidos reiterados (fuerza bruta) | Cuenta activa; política de seguridad vigente: bloqueo tras 3 intentos fallidos | Al tercer intento fallido bloquea la cuenta (p. ej., 15 minutos), informa la situación y genera alerta en el log de seguridad | Permitió intentos ilimitados, sin bloqueo, demora ni alerta: la cuenta permaneció siempre disponible | **NS** |

### Conclusión del Ejercicio 1

4 casos satisfactorios y 1 no satisfactorio. **Hallazgo:** ausencia de control de intentos fallidos, lo que habilita un ataque de fuerza bruta contra las credenciales del personal médico. **Recomendación:** implementar bloqueo temporal tras N intentos fallidos y alerta en el log de seguridad.

---

## Ejercicio 2 — Módulo de Créditos de «sysVentas» (Distribuidora «Pérez Hermanos»)

**Reglas de negocio**

1. Un vendedor estándar puede aplicar descuentos de hasta el **15%**.
2. Descuentos superiores al 15% (y hasta el **30%** máximo) requieren **aprobación del Jefe de Ventas**.
3. El sistema nunca debe permitir descuentos **negativos ni superiores al 30%**.

**Datos base:** cliente «Supermercado San Juan», cuenta corriente activa, pedido cargado por un subtotal de **$100.000**.

**Consigna (actualizada):** completar la tabla de resultados para los casos dados con sus respectivas **calificaciones como Favorable (F) o No Favorable (NF)**.

### Tabla de casos de prueba y resultados

| N° | Caso de prueba | Precondiciones | Resultado esperado | Resultado obtenido | Calificación |
|:--:|---|---|---|---|:--:|
| 1 | Descuento válido dentro del límite estándar. Datos: usuario **vendedor**, 10% | Usuario vendedor (perfil estándar) activo; pedido de $100.000 cargado sobre cuenta corriente activa | Aplica el 10% (≤ 15%), importe final $90.000 y confirma la venta sin autorización | Descuento aplicado; importe final $90.000; venta confirmada y registrada | **NF** |
| 2 | Intento de descuento excesivo por perfil sin autorización (segregación de funciones). Datos: usuario **vendedor**, 20% | Usuario vendedor estándar activo; sin autorización del Jefe de Ventas | Bloquea la aplicación directa del 20% (supera el 15% del perfil) y exige aprobación del Jefe de Ventas; sin aprobación, la venta no se confirma | El sistema bloqueó el descuento y mostró «Descuento superior al límite de su perfil: requiere autorización del Jefe de Ventas»; la venta quedó pendiente de aprobación | **NF** |
| 3 | Ingreso de porcentaje de descuento negativo (falla de validación de entrada). Datos: usuario **jefe de ventas**, −15% | Usuario Jefe de Ventas activo; pedido de $100.000 cargado | Rechaza el valor fuera de rango (−15% < 0%) con el mensaje «Descuento inválido: debe estar entre 0% y 30%»; el importe no se modifica | Aceptó −15% y calculó un importe final de $115.000 (el descuento negativo incrementó el total), sin mensaje de error | **F** |

> NF = No Favorable (la ejecución funciona correctamente; no se encontraron errores) · F = Favorable (se encontraron errores).

### Conclusión del Ejercicio 2

Casos 1 y 2 **«No Favorables»** (funciona correctamente): el sistema aplicó y bloqueó los descuentos conforme a las reglas (límite por perfil y segregación de funciones). Caso 3 **«Favorable»** (se encontraron errores): el control de rango no funciona → el sistema acepta descuentos negativos y los suma al importe. **Recomendación:** validar el rango 0%–30% tanto en la interfaz como en el servidor (validación doble).

---

## Ejercicio 3 — Inventario: Recepción de Mercancía (CP-002)

- **Resultados obtenidos** (simulación de ejecución *«No Favorable» — funciona correctamente*):
  1. El inventario del producto «ABD2» (Aceite Natura) se actualizó a **150 unidades** (100 + 50).
  2. El estado del pedido #456 cambió de «Pendiente» a **«Recibido»**.
  3. El sistema generó el registro de la recepción, incluyendo la fecha, el usuario «InvAdmin01» y las 50 unidades recibidas.
- **¿Los resultados fueron satisfactorios o no?** **Ejecución «No Favorable» (funciona correctamente):** los tres resultados obtenidos coinciden con los esperados; no se encontraron errores.
- **Tipo de prueba:** **Funcional** — verifica el cumplimiento de los requisitos funcionales del módulo de Inventario.
- **Método utilizado:** **Caja negra** — se ejecuta la funcionalidad desde la interfaz con datos de entrada y se comparan las salidas contra la especificación, sin acceder al código.

---

## Ejercicio 4 — Registro de Personal: Validación de edad mínima (CP-003)

- **Resultados obtenidos** (simulación de ejecución *«Favorable» — se encontraron errores*):
  1. El sistema **no** mostró el mensaje de error y **guardó** el legajo de Roberto Gómez (fecha de nacimiento 15/04/2010; 16 años).
  2. El registro quedó almacenado en la base de datos de empleados activos, sin alerta alguna.
- **¿Los resultados fueron satisfactorios o no?** **Ejecución «Favorable» (se encontraron errores):** el control preventivo automático es ineficaz → incumplimiento de la normativa laboral (contratación de menores) y pérdida de integridad de los datos.
- **Tipo de prueba:** **Funcional** — valida una regla de negocio (control automático de integridad de datos).
- **Método utilizado:** **Caja negra** — se prueban datos de entrada no conformes y se observa la respuesta del sistema, sin inspeccionar el código.

---

## Ejercicio 5 — Acceso remoto al servidor de base de datos: 2FA (CP-004)

- **¿Los resultados fueron Favorables o no?** **Favorables (se encontraron errores)** — hallazgo crítico:
  1. Una falla de configuración del servicio habilitó el botón «Omitir»: el ingreso se produjo solo con usuario y contraseña.
  2. El auditor accedió al escritorio del servidor y visualizó las tablas de saldos de clientes sin validar el segundo factor → **compromiso de la confidencialidad** de la información.
  3. No se registró ninguna alerta en el log del sistema → **falla de trazabilidad** del evento de seguridad.
- **Tipo de prueba:** **De seguridad** — identifica vulnerabilidades en los controles de acceso al perímetro lógico.
- **Método utilizado:** **Caja negra** — el auditor actúa como usuario externo (conexión desde fuera de la red local) y observa el comportamiento del sistema sin conocer su implementación.
- **Recomendaciones:** eliminar la posibilidad de omitir el 2FA (validar en el servidor, nunca en el cliente); denegar por defecto toda conexión externa que no complete ambos factores; registrar y alertar los eventos de seguridad fallidos.

---

## Conclusión general

| Ejercicio | Tipo de prueba | Método | Resultado |
|---|:--:|:--:|:--:|
| 1 — Login sysMED | Funcional (con componente de seguridad) | Caja negra | 4 S / 1 NS |
| 2 — Créditos sysVentas | Funcional | Caja negra | 2 NF / 1 F |
| 3 — Inventario CP-002 | Funcional | Caja negra | NF |
| 4 — Legajos CP-003 | Funcional | Caja negra | F |
| 5 — 2FA CP-004 | De seguridad | Caja negra | F (crítico) |

Las pruebas de caja negra, derivadas de los requerimientos y ejecutadas sobre la interfaz, permitieron verificar los requisitos funcionales principales (login, descuentos, actualización de inventario) y detectar tres defectos de control: ausencia de bloqueo por fuerza bruta, falta de validación de rango en descuentos y evasión del factor de doble autenticación.
