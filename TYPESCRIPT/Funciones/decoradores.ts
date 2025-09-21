// decoradores-apunte.ts
/********************************************************************************************
 APUNTE COMPLETO DE DECORADORES EN TYPESCRIPT (modo clásico / experimentalDecorators)
---------------------------------------------------------------------------------------------
Objetivo:
- Entender qué son los decoradores, cuándo se ejecutan y cómo tiparlos correctamente.
- Ver ejemplos prácticos (clase, método, propiedad, accesor, parámetro) y patrones útiles.
- Evitar errores típicos como “The runtime will invoke the decorator with 2 arguments...”.

Requisitos en tsconfig.json:
{
  "compilerOptions": {
    "target": "ES2018",
    "module": "ESNext",              // o "CommonJS" si usas Node
    "moduleResolution": "node",
    "experimentalDecorators": true,  // <— OBLIGATORIO
    "emitDecoratorMetadata": true    // <— Opcional (requiere reflect-metadata)
  }
}

Si usas metadatos (tipos en tiempo de ejecución):
  npm i reflect-metadata
  // Descomenta la siguiente línea en tu entrypoint principal (no necesariamente aquí):
  // import 'reflect-metadata';

NOTA IMPORTANTE SOBRE “FIRMAS” Y PARA QUÉ SIRVE CADA PARÁMETRO:
---------------------------------------------------------------------------------------------
- Decorador de CLASE
  Firma: (constructor) => void | new (...args) => any
  • constructor: el constructor de la clase que estás decorando. Úsalo para:
    - Añadir campos/propiedades estáticas a la clase.
    - Leer o modificar metadatos de la clase.
    - Reemplazar el constructor devolviendo uno nuevo (patrón avanzado).

- Decorador de MÉTODO
  Firma: (target, propertyKey, descriptor) => PropertyDescriptor | void
  • target: el prototipo (para métodos de instancia) o la propia función constructora (para métodos estáticos).
  • propertyKey: nombre de la función (clave del método) como string o symbol.
  • descriptor: el descriptor del método (TypedPropertyDescriptor) que permite:
      - Leer/modificar la función original (descriptor.value).
      - Cambiar flags (enumerable, configurable, writable).
      - Envolver la función para hacer logging, validación, memoización, etc.

- Decorador de ACCESSOR (get/set)
  Firma: (target, propertyKey, descriptor) => PropertyDescriptor | void
  • target: igual que en método.
  • propertyKey: nombre del accessor.
  • descriptor: descriptor del accessor (get/set). Útil para:
      - Marcar readonly, interceptar lecturas/escrituras.
      - Reemplazar el getter/setter.

- Decorador de PROPIEDAD
  Firma: (target, propertyKey) => void            // ¡SOLO 2 argumentos!
  • target: el prototipo (instancia) o constructor (estática) donde vive la propiedad.
  • propertyKey: nombre de la propiedad.
  • Nota: aquí NO recibes descriptor. Si quieres validar o transformar asignaciones:
      - Crea un “backing field” (por ejemplo con un Symbol).
      - Usa Object.defineProperty para definir get/set y aplicar tu lógica.

- Decorador de PARÁMETRO
  Firma: (target, propertyKey, parameterIndex) => void
  • target: el prototipo del método (o el constructor si es parámetro del constructor).
  • propertyKey: el nombre del método donde está el parámetro (undefined si es del constructor).
  • parameterIndex: índice (0..n-1) del parámetro decorado.
  • Se usa para marcar parámetros (p. ej. @Required) y luego en runtime validar/leer esas marcas.

Orden de evaluación/aplicación (resumen):
- Las expresiones de decoradores se EVALUAN de arriba→abajo.
- Los decoradores se APLICAN (se llaman) de abajo→arriba por cada elemento.
- Prioridad: parámetros → (métodos/propiedades/accessors) → clase.

Buenas prácticas:
- Usa los tipos utilitarios de TS: ClassDecorator, MethodDecorator, PropertyDecorator, ParameterDecorator.
- Prefiere “decorator factories” (funciones que devuelven el decorador) para pasar opciones.
- En decoradores de propiedad, si necesitas lógica de get/set, define un backing field con Symbol y usa Object.defineProperty.

Error típico:
“Unable to resolve signature of method decorator... The runtime will invoke the decorator with 2 arguments, but the decorator expects 3”
→ Definiste un decorador con 3 args (método/accessor), pero lo aplicaste sobre una PROPIEDAD (que invoca con 2).
Solución: usa la firma correcta para el sitio correcto, o ajusta dónde lo aplicas.

********************************************************************************************/

/* =========================================================================================
   1) DECORADORES DE CLASE
   -----------------------------------------------------------------------------------------
   - Reciben el constructor de la clase.
   - Pueden añadir/alterar metadatos estáticos o incluso devolver un NUEVO constructor.
========================================================================================= */

// Tipo sugerido: ClassDecorator
function Sellable(tag: string): ClassDecorator {
  return (ctor) => {
    // ctor: constructor de la clase decorada
    Object.defineProperty(ctor, 'tag', {
      value: tag,
      writable: false,
      enumerable: true,
      configurable: false,
    });
  };
}

// Reemplazar constructor (patrón avanzado)
function ReplaceConstructor<T extends new (...args: any[]) => {}>(Replacement: T): ClassDecorator {
  return (_ctor) => {
    // _ctor: constructor original (lo ignoramos y devolvemos otro)
    return Replacement as any;
  };
}

@Sellable('producto')
class Producto {
  constructor(public nombre: string, public precio: number) {}
}

// Ejemplo de reemplazo de constructor (demostrativo)
class ClaseFalsa {
  fake = true;
}
@ReplaceConstructor(ClaseFalsa as any)
class DemoReemplazo {
  x = 1;
}


/* =========================================================================================
   2) DECORADORES DE MÉTODO
   -----------------------------------------------------------------------------------------
   - Firma: (target, propertyKey, descriptor)
   - Útiles para: logging, validación, memoización, medición de tiempo, “autobind”, etc.
========================================================================================= */

// Tipo sugerido: MethodDecorator
function LogCall(prefix = '[LOG]'): MethodDecorator {
  return (_target, propertyKey, descriptor) => {
    // _target: prototipo o constructor (si el método es estático)
    // propertyKey: nombre del método
    // descriptor: descriptor del método (value = función original)
    const original = descriptor.value as Function;
    descriptor.value = function (...args: any[]) {
      console.log(`${prefix} ${String(propertyKey)}(`, ...args, ')');
      const result = original.apply(this, args);
      console.log(`${prefix} ${String(propertyKey)} =>`, result);
      return result;
    };
    return descriptor; // devolver descriptor es recomendable cuando lo modificas
  };
}

// Medir tiempo de ejecución
function TimeIt(label?: string): MethodDecorator {
  return (_t, key, desc) => {
    const original = desc.value as Function;
    desc.value = function (...args: any[]) {
      const lbl = label ?? String(key);
      const start = performance.now?.() ?? Date.now();
      try {
        return original.apply(this, args);
      } finally {
        const end = performance.now?.() ?? Date.now();
        console.log(`[TimeIt:${lbl}] ${(end - start).toFixed(2)}ms`);
      }
    };
    return desc;
  };
}

// Auto-bind “this” (útil cuando pasas métodos como callbacks)
function AutoBind(): MethodDecorator {
  return (_t, k, desc) => {
    const original = desc.value as Function;
    return {
      configurable: true,
      get() {
        const bound = original.bind(this);
        Object.defineProperty(this, String(k), { value: bound, configurable: true, writable: true });
        return bound;
      },
    };
  };
}

class Calculadora {
  @LogCall('[Calc]')
  @TimeIt('sumar')
  sumar(a: number, b: number) {
    return a + b;
  }

  @AutoBind()
  anunciar() {
    console.log('¡Método con this autobind!', this);
  }
}


/* =========================================================================================
   3) DECORADORES DE PROPIEDAD
   -----------------------------------------------------------------------------------------
   - Firma: (target, propertyKey)  ← ¡solo 2 argumentos!
   - No reciben descriptor. Para validar/transformar, define un backing field con Symbol.
========================================================================================= */

// Validar longitud mínima de string
function MinLength(min: number): PropertyDecorator {
  const store = Symbol(`__minLen_${min}`);
  return (target, propertyKey) => {
    // target: prototipo/constructor, propertyKey: nombre de la propiedad
    Object.defineProperty(target, propertyKey, {
      get() {
        return (this as any)[store];
      },
      set(value: any) {
        if (typeof value === 'string' && value.length < min) {
          throw new Error(
            `La propiedad "${String(propertyKey)}" requiere longitud mínima de ${min}. Valor: "${value}"`
          );
        }
        (this as any)[store] = value;
      },
      enumerable: true,
      configurable: true,
    });
  };
}

// Transformar string a MAYÚSCULAS al asignar
function UpperCase(): PropertyDecorator {
  const store = Symbol('__upper');
  return (target, propertyKey) => {
    Object.defineProperty(target, propertyKey, {
      get() {
        return (this as any)[store];
      },
      set(value: any) {
        (this as any)[store] = typeof value === 'string' ? value.toUpperCase() : value;
      },
      enumerable: true,
      configurable: true,
    });
  };
}

class Usuario {
  @MinLength(3)
  @UpperCase()
  nombre!: string;

  constructor(nombre: string) {
    this.nombre = nombre; // se validará y se pondrá en mayúsculas
  }
}


/* =========================================================================================
   4) DECORADORES DE ACCESSOR (get/set)
   -----------------------------------------------------------------------------------------
   - Firma: (target, propertyKey, descriptor)
   - Parecidos a los de método, pero para accessors (getters/setters).
========================================================================================= */

function ReadonlyAccessor(): MethodDecorator {
  return (_t, _k, desc) => {
    // desc: descriptor del accessor (get/set)
    desc.configurable = false;
    return desc;
  };
}

class Config {
  private _token = 'abc123';

  @ReadonlyAccessor()
  get token() {
    return this._token;
  }

  // set token(_) { ... } // podrías prohibir el set para “readonly”
}


/* =========================================================================================
   5) DECORADORES DE PARÁMETRO
   -----------------------------------------------------------------------------------------
   - Firma: (target, propertyKey, parameterIndex)
   - Se usan para marcar parámetros y luego verificarlos en tiempo de llamada (con apoyo extra).
   - Con emitDecoratorMetadata + reflect-metadata puedes leer tipos en runtime (avanzado).
========================================================================================= */

// Marca parámetros como requeridos y valida en ejecución con un *wrapper* de método:
const requiredMetadataKey = Symbol('required_params');

function Required(): ParameterDecorator {
  return (target, propertyKey, parameterIndex) => {
    // target: prototipo, propertyKey: nombre del método, parameterIndex: índice del parámetro
    const existing: number[] = Reflect.getOwnMetadata?.(requiredMetadataKey, target, propertyKey!) ?? [];
    existing.push(parameterIndex);
    Reflect.defineMetadata?.(requiredMetadataKey, existing, target, propertyKey!);
  };
}

function ValidateParameters(): MethodDecorator {
  return (target, propertyKey, descriptor) => {
    const original = descriptor.value as Function;
    descriptor.value = function (...args: any[]) {
      const requiredParams: number[] =
        Reflect.getOwnMetadata?.(requiredMetadataKey, target, propertyKey!) ?? [];
      for (const index of requiredParams) {
        if (args[index] === null || args[index] === undefined) {
          throw new Error(`Parámetro #${index} de "${String(propertyKey)}" es requerido y llegó vacío.`);
        }
      }
      return original.apply(this, args);
    };
    return descriptor;
  };
}

class AuthService {
  @ValidateParameters()
  login(@Required() email?: string, @Required() password?: string) {
    return `Logueado como ${email}`;
  }
}


/* =========================================================================================
   6) METADATOS DE TIPOS (emitDecoratorMetadata) — OPCIONAL
   -----------------------------------------------------------------------------------------
   - Requiere: "emitDecoratorMetadata": true y `import 'reflect-metadata'` en tu entrypoint.
   - Puedes leer los tipos de parámetros/retorno en runtime (limitado).
========================================================================================= */

// Ejemplo: loggear tipos de parámetros de un método:
function LogParamTypes(): MethodDecorator {
  return (target, propertyKey, descriptor) => {
    // target: prototipo, propertyKey: nombre del método, descriptor: descriptor del método
    const types = Reflect.getMetadata?.('design:paramtypes', target, propertyKey!);
    const ret = Reflect.getMetadata?.('design:returntype', target, propertyKey!);
    console.log(`[MetaTypes] ${String(propertyKey)} paramtypes:`, types?.map((t: any) => t?.name));
    console.log(`[MetaTypes] ${String(propertyKey)} returntype:`, ret?.name);
    return descriptor;
  };
}

class DemoMeta {
  @LogParamTypes()
  x(a: number, b: string): boolean {
    return !!(a && b);
  }
}


/* =========================================================================================
   7) COMPOSICIÓN, ORDEN Y ERRORES COMUNES
   -----------------------------------------------------------------------------------------
   - Puedes encadenar varios decoradores en un mismo objetivo (como @LogCall @TimeIt).
   - Recuerda: evaluación arriba→abajo, aplicación abajo→arriba.
   - No mezcles firmas: método ≠ propiedad ≠ parámetro.
   - Propiedad no tiene descriptor: usa Symbol + defineProperty si necesitas validar.
========================================================================================= */

// Decorador deprecado: muestra warning en tiempo de ejecución
function Deprecated(msg = 'Este método está deprecado'): MethodDecorator {
  return (_t, key, desc) => {
    const original = desc.value as Function;
    desc.value = function (...args: any[]) {
      console.warn(`[DEPRECATED] ${String(key)}: ${msg}`);
      return original.apply(this, args);
    };
    return desc;
  };
}

// Memoización simple (solo por demo)
function Memoize(): MethodDecorator {
  const cacheMap = new WeakMap<object, Map<string, any>>();
  return (_t, key, desc) => {
    const original = desc.value as Function;
    desc.value = function (...args: any[]) {
      let instCache = cacheMap.get(this);
      if (!instCache) {
        instCache = new Map();
        cacheMap.set(this, instCache);
      }
      const k = JSON.stringify([key, args]);
      if (instCache.has(k)) return instCache.get(k);
      const result = original.apply(this, args);
      instCache.set(k, result);
      return result;
    };
    return desc;
  };
}

class MathOps {
  @Deprecated('Usa "fibFast" en su lugar')
  @Memoize()
  fib(n: number): number {
    return n < 2 ? n : this.fib(n - 1) + this.fib(n - 2);
  }
}


/* =========================================================================================
   8) TIPADO FINO DE DECORADORES (para evitar any)
   -----------------------------------------------------------------------------------------
   - Usa los tipos nativos de TS para describir exactamente lo que decoras.
========================================================================================= */

const StrictLog: MethodDecorator = (_t, key, desc) => {
  // desc: TypedPropertyDescriptor<any>
  return desc;
};

const StrictProp: PropertyDecorator = (_t, _k) => {
  // ...
};

const StrictClass: ClassDecorator = (_ctor) => {
  // ...
};


/* =========================================================================================
   9) MINI DEMO DE USO
========================================================================================= */

function miniDemo() {
  const prod = new Producto('Teclado', 999);
  console.log('Producto.tag (estático):', (Producto as any).tag);
  console.log('Producto:', prod);

  const calc = new Calculadora();
  calc.sumar(3, 4);
  const cb = calc.anunciar;
  cb(); // gracias a @AutoBind, this no se pierde

  const u1 = new Usuario('ana');    // => 'ANA'
  console.log('Usuario.nombre:', u1.nombre);
  // const u2 = new Usuario('ab');  // <- lanza error por MinLength(3)

  const auth = new AuthService();
  console.log(auth.login('user@mail.com', '1234')); // ok
  // auth.login('solo@mail.com'); // <- lanza error Required

  const m = new DemoMeta();
  m.x(10, 'ok');

  const mops = new MathOps();
  console.log('fib(10)=', mops.fib(10)); // verás [DEPRECATED] + cache en siguientes llamadas
}

miniDemo();

/********************************************************************************************
PREGUNTAS FRECUENTES (FAQ)
---------------------------------------------------------------------------------------------
1) “The runtime will invoke the decorator with 2 arguments, but the decorator expects 3”
   - Estás usando un decorador con firma de MÉTODO/ACCESSOR en una PROPIEDAD. Cambia la firma o dónde lo aplicas.

2) ¿Por qué mi decorador de PROPIEDAD no recibe descriptor?
   - Por definición en el sistema de decoradores clásico de TS. Si quieres lógica de get/set, usa backing field + defineProperty.

3) ¿Cuándo se ejecutan los decoradores?
   - En el momento de la definición de la clase (carga del módulo), no cuando instancias.

4) ¿Puedo leer tipos en runtime (como hace NestJS)?
   - Sí, con "emitDecoratorMetadata": true + reflect-metadata, pero es limitado y no existe para todo caso.

5) ¿Puedo devolver valores en decoradores?
   - Clase: puedes devolver un nuevo constructor. Método/Accessor: devolver un descriptor modificado.
   - Propiedad/Parámetro: su valor de retorno se ignora.

Consejo final:
- Empieza con factories simples (p. ej., @LogCall('prefix')).
- Tipar con MethodDecorator/PropertyDecorator/etc. te evita muchos errores.
- Mantén los decoradores PUROS y específicos; no mezcles muchas responsabilidades.
********************************************************************************************/
