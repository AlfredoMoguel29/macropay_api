import js2py

# Import JS database to python as an object
res_2 = js2py.run_file("data/fakedatabase.js")[0]
# Transform python object to list
res_2 = res_2.to_list()

def sorted_list(list=res_2):
    """
    Sort the list by name.

    Parameters
    ----------
    list : list
        Filename from data/fakedatabase,js.

    Returns
    -------
    sorted list
    
    """
    list.sort(key=lambda item: item.get("name"))
    return list