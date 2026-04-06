"""
Guia de Scrapy enfocada en metodos, parametros, argumentos y atributos.

Scrapy es un framework de scraping y crawling. Te ayuda a:
- Enviar requests HTTP y seguir enlaces
- Parsear HTML con selectores CSS/XPath
- Extraer datos en items (diccionarios o clases Item)
- Exportar resultados a JSON, CSV, JSONL, etc.

Instalacion:
    pip install scrapy

Crear proyecto:
    scrapy startproject mi_proyecto
    cd mi_proyecto

Crear spider:
    scrapy genspider productos ejemplo.com

Ejecutar spider:
    scrapy crawl productos

Exportar salida:
    scrapy crawl productos -O productos.json
    scrapy crawl productos -O productos.csv
"""

import scrapy


class ProductosSpider(scrapy.Spider):
    """
    ATRIBUTOS DE CLASE IMPORTANTES EN UNA SPIDER
    --------------------------------------------
    name (str):
        Nombre unico de la spider para ejecutarla con `scrapy crawl name`.

    allowed_domains (list[str]):
        Lista opcional de dominios permitidos. Evita seguir enlaces fuera
        de esos dominios cuando usas follow/follow_all.

    start_urls (list[str]):
        URLs iniciales. Scrapy crea requests GET automaticamente y llama
        a parse(response) con cada respuesta.

    custom_settings (dict):
        Configuracion solo para esta spider.
    """

    name = "productos"
    allowed_domains = ["ejemplo.com"]
    start_urls = ["https://ejemplo.com/productos"]
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "ROBOTSTXT_OBEY": True,
    }

    def start_requests(self):
        """
        METODO: start_requests
        ----------------------
        Es el punto de inicio opcional cuando quieres mas control que
        start_urls. Si lo defines, puedes agregar headers, cookies, meta,
        metodo HTTP, etc.

        No recibe argumentos personalizados; Scrapy lo llama internamente.
        Debe hacer yield de objetos Request.
        """
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                headers={"User-Agent": "Mozilla/5.0 (compatible; ApuntesBot/1.0)"},
                meta={"fuente": "listado_principal"},
            )

    def parse(self, response):
        """
        METODO: parse
        -------------
        Firma tipica: parse(self, response)

        Parametros:
        - self: instancia de la spider.
        - response (scrapy.http.Response): respuesta HTTP de la pagina actual.

        Que puede devolver (yield):
        - dict o Item: datos extraidos.
        - Request: nuevas peticiones para seguir navegando.
        """
        for card in response.css(".producto"):
            url_relativa = card.css("a::attr(href)").get()

            # Extrae un item (datos)
            yield {
                "nombre": card.css("h2::text").get(default="").strip(),
                "precio": card.css(".precio::text").get(default="").strip(),
                "url": response.urljoin(url_relativa) if url_relativa else None,
            }

            # Sigue al detalle del producto
            if url_relativa:
                yield response.follow(
                    url_relativa,
                    callback=self.parse_detalle,
                    cb_kwargs={"origen": "listado"},
                )

        siguiente = response.css("a.siguiente::attr(href)").get()
        if siguiente:
            # response.follow(url, callback=...) arma la URL absoluta automaticamente
            yield response.follow(siguiente, callback=self.parse)

    def parse_detalle(self, response, origen):
        """
        METODO: parse_detalle
        ---------------------
        Ejemplo de callback con argumento adicional.

        Firma:
            parse_detalle(self, response, origen)

        Parametros:
        - response: pagina de detalle.
        - origen: argumento pasado desde cb_kwargs en response.follow.

        Nota:
        - En Scrapy moderno se recomienda cb_kwargs para pasar argumentos
          al callback en vez de usar solo response.meta para todo.
        """
        yield {
            "titulo_detalle": response.css("h1::text").get(default="").strip(),
            "descripcion": " ".join(response.css(".descripcion ::text").getall()).strip(),
            "origen": origen,
            "url_actual": response.url,
        }


"""
PARAMETROS Y ARGUMENTOS FRECUENTES EN SCRAPY
-------------------------------------------
1) scrapy.Request(...)
   Parametros comunes:
   - url (str): URL destino.
   - callback (callable): funcion que procesa la respuesta.
   - method (str): GET, POST, etc.
   - headers (dict): cabeceras HTTP.
   - cookies (dict): cookies para la request.
   - meta (dict): datos internos para transportar contexto.
   - dont_filter (bool): si True, evita filtro de duplicados.
   - cb_kwargs (dict): argumentos para la funcion callback.

2) response.css(query)
   - query (str): selector CSS.
   Retorna un SelectorList.

3) response.xpath(query)
   - query (str): expresion XPath.
   Retorna un SelectorList.

4) .get(default=None)
   - default: valor por defecto si no encuentra nada.
   Devuelve un solo resultado (str o None).

5) .getall()
   Devuelve una lista con todos los resultados.

6) response.follow(url, callback=None, cb_kwargs=None, meta=None)
   - url: enlace relativo o absoluto.
   - callback: metodo que procesara esa respuesta.
   - cb_kwargs: argumentos extra para callback.
   - meta: contexto adicional en request/response.


DIFERENCIA RAPIDA: PARAMETRO VS ARGUMENTO
----------------------------------------
- Parametro: variable definida en la funcion.
  Ejemplo: def parse_detalle(self, response, origen):
           -> `response` y `origen` son parametros.

- Argumento: valor real que envias al llamar la funcion.
  Ejemplo: cb_kwargs={"origen": "listado"}
           -> "listado" es el argumento que recibira el parametro `origen`.


OTROS ATRIBUTOS UTILES DE CLASE/SPIDER
--------------------------------------
- handle_httpstatus_list = [404, 500]
  Permite procesar codigos HTTP concretos en callbacks.

- handle_httpstatus_all = True
  Permite procesar cualquier status HTTP.

- logger
  Objeto de logging ya disponible en la spider:
      self.logger.info("Mensaje")


BUENAS PRACTICAS
----------------
- Respetar robots.txt y terminos del sitio.
- Configurar USER_AGENT y DOWNLOAD_DELAY.
- Manejar nulos con get(default="") o validaciones.
- Separar extraccion, limpieza y persistencia (pipelines).
- Evitar saturar servidores con demasiada concurrencia.


RESUMEN
-------
En Scrapy, dominar metodos (parse, start_requests, callbacks),
parametros/argumentos (Request, follow, selectores) y atributos de clase
(`name`, `allowed_domains`, `start_urls`, `custom_settings`) te da control
total del crawler.
"""
