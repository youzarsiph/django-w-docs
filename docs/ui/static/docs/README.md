# UI Styles

Basic commands to get started.

First `cd` into dir:

```console
cd docs/ui/static/docs
```

To generate the styles:

```console
npm install
cd docs/ui/static/docs
npx @tailwindcss/cli -i ../static/docs/css/app.css -o ../static/docs/css/styles.css --cwd ../../templates -m -w
```

To format the templates:

```console
npx prettier -w ../../templates
```
