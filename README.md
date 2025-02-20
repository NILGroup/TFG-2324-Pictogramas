# TFG-2324-Pictogramas

Repositorio de LoRAs para generación de imágenes de pictogramas usando modelos de **Stable Diffusion**, con el objetivo ayudar a la Comunicación Aumentativa y Alternativa (CAA).

## Índice

1. [Introducción](#introducción)
2. [Guía de Uso](#guía-de-uso)
   - [1. Instalar GUI WebUI](#1-instalar-gui-webui)
   - [2. Descargar Modelos Compatibles](#2-descargar-modelos-compatibles)
   - [3. Descargar LoRAs](#3-descargar-loras)
   - [4. Generar Imágenes con LoRAs](#4-generar-imágenes-con-loras)
3. [LoRAs Stable Diffusion 1-5](#loras-stable-diffusion-1-5)
4. [LoRAs Stable Diffusion XL](#loras-stable-diffusion-xl)
5. [Recomendaciones de Modelos y LoRAs](#recomendaciones-de-modelos-y-loras)
6. [Notas Adicionales](#notas-adicionales)
7. [Enlaces Útiles](#enlaces-útiles)

---

## Introducción

Este repositorio contiene **LoRAs** entrenados para la generación de pictogramas utilizando modelos de **Stable Diffusion**. Los LoRAs están diseñados para generar imágenes con el estilo de pictogramas de la base de datos de **[ARASAAC](https://arasaac.org/)**, dos estilos disponibles Basico y Stickman.

---

## Guía de Uso

### 1. Instalar GUI WebUI
Para utilizar los LoRAs de manera sencilla, primero necesitarás instalar una interfaz gráfica de usuario (GUI) estilo **WebUI**. Este tipo de interfaz facilita la generación de imágenes con tus LoRAs y modelos preentrenados.

- **Recomendación**: Instalar [Stable Diffusion WebUI](https://github.com/lllyasviel/stable-diffusion-webui-forge?tab=readme-ov-file) o una GUI compatible.
  
> **Nota**: Asegúrate de seguir todas las instrucciones de instalación y cumplir con los requisitos del sistema.

### 2. Descargar Modelos Compatibles

Una vez instalada la GUI, necesitas descargar los modelos compatibles.

- **Modelos recomendados**:
   - **[DreamShaper](https://civitai.com/models/4384?modelVersionId=128713)**: Ideal para LoRAs entrenados con Stable Diffusion 1.5.
   - **[Juggernaut XL](https://civitai.com/models/133005/juggernaut-xl)**: Ideal para LoRAs entrenados con Stable Diffusion XL, es un modelo muy exigente.
   - **[DreamShaper XL Turbo](https://civitai.com/models/112902?modelVersionId=351306)**: LoRAs entrenados con Stable Diffusion XL, menos exigente y mas rapido que juggernaut XL.
     
 > **Nota**: Puedes elegir el modelo que más te convenga según tus necesidades. Este debe ser basado en Stable Diffusion 1.5 o Stable Diffusion XL, dependiendo del LoRA que elejido.

### 3. Descargar LoRAs

Ahora, descarga los LoRAs disponibles. Asegúrate de elegir el archivo correcto según el modelo que estás utilizando.

- **LoRAs disponibles**:
  - [Arasaac Stickman XL v1](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacXLv1/arasaacXLv1.safetensors)
  - [Arasaac Stickman XL v2](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacStickmanXLv2/arasaacStickmanXLv2.safetensors)

> **Recomendación**: Si tienes dudas sobre qué LoRA elegir, revisa la documentación adicional para obtener más detalles sobre las opciones disponibles.

### 4. Generar Imágenes con LoRAs

Una vez que hayas descargado el modelo y el LoRA, sigue estos pasos para generar imágenes:

1. **Cargar el modelo en la GUI WebUI**.
   - En la sección de "Modelo", selecciona el modelo adecuado (por ejemplo, DreamShaper).

2. **Activar el LoRA**.
   - En la sección de LoRAs, activa el archivo `.safetensors` correspondiente, en WebUI poner el LoRA en el prompt y el peso adecuado para este.

3. **Configurar los parámetros de generación**.
   - Clip Skip en 2 y otros parametros que quieras personalizar.

4. **Usar la palabra clave**.
   - En el campo de texto, **usa la palabra "arasaac"** para activar el LoRA.

5. **Generar la imagen**.
   - Escribir el prompt y observa cómo se crea tu pictograma.

---
## LoRAs Stable Diffusion 1-5
Estos LoRAs deben ser utilizados con un modelo basado en Stable Diffusion 1.5.

### Arasaac - Estilo: Base
- [Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main/LoRAs/StableDiffusion1.5/loraBaseStyle)
- [Modelo safetensors](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/StableDiffusion1.5/loraBaseStyle/arasaacStyle.safetensors)
- [Configuración](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/StableDiffusion1.5/loraBaseStyle/configuration.json)
- **Trigegr Word**: arasaac
- **Peso del LoRA**: recomendado 0.7, rango [0.6-1.1]
- **Parametros**: Clip Skip = 2
- **Resolución**: 512x512
- **Modelos de generación basados en SD 1.5**

### Arasaac - Estilo: Stickman
- [Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main/LoRAs/StableDiffusion1.5/loraStickman)
- [Modelo safetensors](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/StableDiffusion1.5/loraStickman/arasaacStickman.safetensors)
- [Configuración](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/StableDiffusion1.5/loraStickman/configuration.json)
- **Trigegr Word**: arasaac
- **Peso del LoRA**: $\pm 1.2$ 
- **Parametros**: Clip Skip = 2
- **Resolución**: 512x512
- **Modelos de generación basados en SD 1.5**

## LoRAs Stable Diffusion XL

Estos LoRAs deben ser utilizados con un modelo basado en Stable Diffusion XL.

### Arasaac XL - Estilo: Base
- [Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main/LoRAs/XL/arasaacXLv1)
- [Modelo safetensors](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacXLv1/arasaacXLv1.safetensors)
- [Configuración](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacXLv1/configuration.json)
- **Trigegr Word**: arasaac
- **Peso del LoRA**: $\pm 1$
- **Parametros**: Clip Skip = 2
- **Resolución**: 1024x1024
- **Modelos de generación basados en SDXL**

### Arasaac XL - Estilo: Stickman v1
- [Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main/LoRAs/XL/arasaacStickmanXLv1)
- [Modelo safetensors](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacStickmanXLv1/arasaacStickmanXLv1.safetensors)
- [Configuración](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacStickmanXLv1/configuration.json)
- **Trigegr Word**: arasaac
- **Peso del LoRA**: $\pm 1.1$
- **Parametros**: Clip Skip = 2
- **Resolución**: 1024x1024
- **Modelos de generación basados en SDXL**

### Arasaac XL - Estilo: Stickman v2
- [Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main/LoRAs/XL/arasaacStickmanXLv2)
- [Modelo safetensors](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacStickmanXLv2/arasaacStickmanXLv2.safetensors)
- [Configuración](https://huggingface.co/antuna01/Pictogram-LoRAs/resolve/main/LoRAs/XL/arasaacStickmanXLv2/configuration.json)
- **Trigegr Word**: arasaac
- **Peso del LoRA**: $\pm 1.1$
- **Parametros**: Clip Skip = 2
- **Resolución**: 1024x1024
- **Modelos de generación basados en SDXL**

> **Recomendación**: El valor de peso indicado en cada LoRA es genérico, probar diferentes pesos a la hora de generar con los LoRAs. Según el prompt se obtienen mejores resultados con valores mas altos o bajos. 
---

## Recomendaciones de Modelos y LoRAs

- **LoRAs XL**: Son ideales para usar con modelos basados en **Stable Diffusion XL** como **DreamShaper XL Turbo** o **Juggernaut XL**. Proporcionan imágenes detalladas y con mayor control sobre los resultados.
  
- **LoRAs estándar**: Funcionan bien con modelos basados en **Stable Diffusion 1.5** como **DreamShaper**.

> **Recomendación**: Los basado en SD 1.5 han sido mas probado y sus exigencias hardware son menores, además su velocidad de generacion es superior. Empieza con **Dreamshaper** junto con el LoRA **CAMBIARRRR**`arasaacXLv1` para obtener buenos resultados.

---

## Enlaces Útiles

- [Instalar GUI WebUI](https://github.com/lllyasviel/stable-diffusion-webui-forge?tab=readme-ov-file)
- [Descargar DreamShaper](https://civitai.com/models/4384?modelVersionId=128713) **-** [Descargar Juggernaut XL](https://civitai.com/models/133005/juggernaut-xl) **-** [Descargar DreamShaper XL Turbo](https://civitai.com/models/112902?modelVersionId=351306)
- [Proyecto en Huggingface](https://huggingface.co/antuna01/Pictogram-LoRAs/tree/main)

---

### **Resumen de uso rápido**:
1. **Instalar GUI**.
2. **Descargar Modelo** (modelo compatible con el LoRA que uses).
3. **Descargar LoRA**.
4. **Generar imágenes con "arasaac"** como palabra clave.

---

