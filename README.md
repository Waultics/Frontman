# Frontman

Frontman is a micro-project to initialize [ProxyBroker](https://github.com/constverum/ProxyBroker) serve functionality within a docker container and with a designated `config.yml` file. Once Frontman is built and ran as a container, it is easy to route any other container's traffic through it.

---

## Building Frontman

To build Frontman it is recommended you use the `Dockerfile` included in this repo. To do so, run the following commands:

```
docker build -t frontman .
docker run -p 8888:8888 frontman
```

---

## Routing Traffic

If you want to route the traffic of another container through Frontman you will have to utilize an `.env` and `docker-compose.yml` file.

#### `.env`
```
http_proxy=http://frontman:8888
https_proxy=http://frontman:8888
```

#### `docker-compose.yml`
```
frontman:
    image: frontman
    ports:
        - "8888:8888"

my-service:
  image: ...
  environment:
      http_proxy: ${http_proxy}
      https_proxy: ${https_proxy}
```

---

## `config.yml` File

The config file is separated into two portions; one is the `broker`, which initializes the ProxyBroker `Broker` object, and the other is `serve`, which is the function `Broker.serve()` which serves the local proxy.

`Default` can be utilized in the configuration file for optional variables below.

### [`broker`](https://proxybroker.readthedocs.io/en/latest/api.html#broker)
* `timeout (int) – (optional)`: Timeout of a request in seconds.
* `max_conn (int) – (optional)`: The maximum number of concurrent checks of proxies.
* `max_tries (int) – (optional)`: The maximum number of attempts to check a proxy.
* `judges (list) – (optional)`: Urls of pages that show HTTP headers and IP address.
* `providers (list) – (optional)` Urls of pages where to find proxies.
* `verify_ssl (bool) – (optional)` Flag indicating whether to check the SSL certificates (True to check).

### [`serve`](https://proxybroker.readthedocs.io/en/latest/api.html#proxybroker.api.Broker.serve)
* `host (str) – (optional)`: Host of local proxy server
* `port (int) – (optional)`: Port of local proxy server
* `limit (int) – (optional)`: When will be found a requested number of working proxies, checking of new proxies will be lazily paused. Checking will be resumed if all the found proxies will be discarded in the process of working with them (see max_error_rate, max_resp_time). And will continue until it finds one working proxy and paused again. The default value is 100
* `max_tries (int) – (optional)`: The maximum number of attempts to handle an incoming request. If not specified, it will use the value specified during the creation of the Broker object. Attempts can be made with different proxies. The default value is 3
* `min_req_proxy (int) – (optional)`: The minimum number of processed requests to estimate the quality of proxy (in accordance with max_error_rate and max_resp_time). The default value is 5
* `max_error_rate (int) – (optional)`: The maximum percentage of requests that ended with an error. For example: 0.5 = 50%. If proxy.error_rate exceeds this value, proxy will be removed from the pool. The default value is 0.5
* `max_resp_time (int) – (optional)`: The maximum response time in seconds. If proxy.avg_resp_time exceeds this value, proxy will be removed from the pool. The default value is 8
* `prefer_connect (bool) – (optional)`: Flag that indicates whether to use the CONNECT method if possible. For example: If is set to True and a proxy supports HTTP proto (GET or POST requests) and CONNECT method, the server will try to use CONNECT method and only after that send the original request. The default value is False
* `http_allowed_codes (list) – (optional)`: Acceptable HTTP codes returned by proxy on requests. If a proxy return code, not included in this list, it will be considered as a proxy error, not a wrong/unavailable address. For example, if a proxy will return a 404 Not Found response - this will be considered as an error of a proxy. Checks only for HTTP protocol, HTTPS not supported at the moment. By default the list is empty and the response code is not verified
* `backlog (int) – (optional)`: The maximum number of queued connections passed to listen. The default value is 100
* `types (list) – Types (protocols)`: that need to be check on support by proxy. Supported: HTTP, HTTPS, SOCKS4, SOCKS5, CONNECT:80, CONNECT:25 And levels of anonymity (HTTP only): Transparent, Anonymous, High
* `data – (optional)`: String or list with proxies. Also can be a file-like object supports read() method. Used instead of providers
* `countries (list) – (optional)`: List of ISO country codes where should be located proxies
* `post (bool) – (optional)`: Flag indicating use POST instead of GET for requests when checking proxies
* `strict (bool) – (optional)`: Flag indicating that anonymity levels of types (protocols) supported by a proxy must be equal to the requested types and levels of anonymity. By default, strict mode is off and for a successful check is enough to satisfy any one of the requested types
* `dnsbl (list) – (optional)`: Spam databases for proxy checking. Wiki
* `limit (int) – (optional)`: The maximum number of proxies
