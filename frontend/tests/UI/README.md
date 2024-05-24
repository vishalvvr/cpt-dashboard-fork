[Playwright Framework Docs](https://playwright.dev/python/docs/intro)

# Run test locally
- Installing dependencies 
    ```console
    $ pip install -r requirements.txt
    ```
- Download browser drivers for playwright
    ```console
    $ playwright install
    ```
- Export env variables
    ```console
    $ export BASE_URL = "<url of CPT dashboard>"
    $ export API_URL = "<backend api endpoint>"
    ```
- Run test
    ```console
    $ pytest
    ```
# Run test in container
- Build container 
    make sure you have podman installed
    ```console
    $ podman build -t cpt-ui-test -f Dockerfile
    ```
- Run test
    ```console
    $ podman run -e BASE_URL=<base url> -e API_URL=<api url> --network=host -it localhost/cpt-ui-test 
    ```
    eg: 
    ```console
    $ podman run -e BASE_URL="http://localhost:3000" -e API_URL="http://localhost:8000/api/v1/cpt/jobs?pretty=true" --network=host -it localhost/cpt-ui-test
    ```