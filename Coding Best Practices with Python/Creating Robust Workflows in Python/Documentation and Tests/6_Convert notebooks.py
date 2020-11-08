def nbconv(nb_name: str, exporter: str = "script") -> str:
    """Convert a notebook into various formats using different exporters."""
    # Instantiate the specified exporter class
    exp = get_exporter(exporter)()
    # Return the converted file"s contents string
    return exp.from_filename(nb_name)[0]

pprint(nbconv(nb_name="mynotebook.ipynb", exporter="html"))
