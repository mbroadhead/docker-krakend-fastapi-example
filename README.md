This is a basic example of how you could use [krakend](https://www.krakend.io) with [api_keys and roles](https://www.krakend.io/docs/enterprise/authentication/api-keys/) to protect a FastAPI microservice.
Note that api_keys is an enterprise feature of krakend and will currently not work with the community edition.
The [FastAPI](https://fastapi.tiangolo.com) app contains three routes:
 * GET /guest (public)
 * GET /member (Protected by one api_key and the "member" role)
 * GET /admin (Protected by an api_key that contains the "admin" role)

