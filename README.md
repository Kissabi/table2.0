### Table2.0

The "Table2.0" is a project that demonstrates the usage of the dash-ag-Grid library to create an interactive table that displays images. Ag-Grid is a powerful data grid library that provides advanced features for displaying and manipulating tabular data.

Installation
Clone the repository:

```bash
git clone https://github.com/Kissabi/table2.0.git
cd table2.0
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
python3 app.py
```

Start an HTTP server for the files:

```bash
python3 -m http.server
```

Access the `dashAgGridComponentFunctions.js` file in the `assets` folder and edit the URL to the relative path of images on the file server:

```javascript
swal({
    title: elem.value,
    icon: "URL" + elem.value + ".jpg" // Edit this line
});
```

Access the URL http://localhost:5000 to view the interactive table with images.

Contributions are welcome! If you have suggestions, improvements, or corrections, feel free to submit a pull request or open an issue.
