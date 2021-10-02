# Serverless Python Function

This is a simple repo that demo that shows how to write a serverless function in Python, based on this [blog post](https://newrelic.com/blog/best-practices/create-a-serverless-function-in-python) by Michael Lavers. Check out the post for more information about the end-to-end setup and deployment.

## Development

You'll need Node, NPM, and Python installed to invoke these functions locally.

Additionally, you'll need to install the Serverless Framework globally.

```bash
npm install -g serverless
```

## Invoke the functions locally

There are two functions included in this repo.

`simple` returns a static string in JSON.

```bash
serverless invoke local --function simple
```

`httprequest` makes an API call to the [Dog Facts API](https://dukengn.github.io/Dog-facts-API/), and returns 3 facts as JSON.

```bash
serverless invoke local --function httprequest
```

Check the [Serverless docs](https://www.serverless.com/framework/docs/providers/aws/cli-reference/invoke-local) for more information about running functions locally.
