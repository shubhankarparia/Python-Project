# Calculator-Flask

A clean, responsive calculator built with **Flask**, **HTML**, **CSS**, and **vanilla JavaScript**.

The UI runs entirely client-side for instant feedback (no page reloads), while
Flask serves the app and also exposes a small JSON API for server-side
evaluation of expressions.

## Features

- 🎨 Distinctive "instrument panel" design — graphite case, amber LED-style display
- 📱 Fully responsive (mobile, tablet, desktop)
- ⌨️ Keyboard support (numbers, `+ - * /`, `Enter` for `=`, `Esc` to clear, `Backspace`)
- ➗ Handles chained operations, decimals, percentages, sign flip, division-by-zero
- 🧮 Optional server-side calculation API using a safe AST-based evaluator (no `eval()`)
- 🚫 Custom 404 and 500 error pages matching the app's theme

## Project structure

```
Calculator-Flask/
├── app.py                 # Flask app, routes, error handlers, safe expression evaluator
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Calculator page
│   ├── 404.html             # Not found page
│   └── 500.html             # Server error page
├── static/
│   ├── css/
│   │   └── style.css       # Responsive styling / design system
│   ├── js/
│   │   └── script.js       # Calculator logic + keyboard support
│   └── images/
│       └── logo.png        # App mark / favicon
└── README.md
```

## Getting started

1. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   python app.py
   ```

4. Open your browser at **http://127.0.0.1:5000**

## API reference

`POST /api/calculate`

Request body:

```json
{ "expression": "12 + 4 * 2" }
```

Response:

```json
{ "expression": "12 + 4 * 2", "result": 20 }
```

Errors (e.g. division by zero, invalid characters) return HTTP `400` with an
`error` message. Only digits and the operators `+ - * / % ^ ( )` are accepted
— the expression is parsed as a Python AST and evaluated node-by-node against
a strict whitelist, so arbitrary code can never run.

## Customizing

- **Colors / fonts** — all design tokens live at the top of `static/css/style.css` as CSS variables (`--amber`, `--case`, `--font-display`, etc.).
- **Buttons** — add or remove keys directly in `templates/index.html`; each button uses a `data-num`, `data-op`, or `data-action` attribute that `script.js` reads.
- **Error pages** — edit `templates/404.html` / `templates/500.html`; they share the same visual language as the calculator.

## Tech stack

- [Flask](https://flask.palletsprojects.com/) (Python)
- HTML5 / CSS3 (custom properties, CSS Grid, `clamp()` for fluid type)
- Vanilla JavaScript (no frameworks, no build step)

