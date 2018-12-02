
def load_file_iterative_function(file_name, some_func, **kwargs):
    """Loads a file from an absolute path and then does something to its input with each iteration.

    :param file_name: The file name to open.
    :param some_func: The function to perform on each line of input.
    This function should return the formatted line item and result of its calculation.
    :param kwargs: The arguments that you might need to pass to the function, as keyword arguments.
    :return: The file's contents as a list and the results of the function as a list
    """
    file = open(file_name, 'r')
    line_list = list()
    result_list = list()
    for line in file:
        formatted_line, output_entry = some_func(line, **kwargs)
        line_list.append(formatted_line)
        result_list.append(output_entry)
    file.close()
    return line_list, result_list


def load_file_list_function(file_name, format_func, some_func, **kwargs):
    """Loads a file from an absolute path and then does a function on the resulting list.

    :param file_name: The file name to open.
    :param some_func: The function to perform on the list we get.
    :param format_func: The function to use on the input to format it in the way the function wants.
    :param kwargs: The arguments that you might need to pass to the function, as keyword arguments.
    :return: The file's contents as a list and the results of the function.
    """

    file = open(file_name, 'r')
    line_list = list()
    for line in file:
        formatted_line = format_func(line)
        line_list.append(formatted_line)
    file.close()
    print(f"Lines in file: {len(line_list)}")
    return line_list, some_func(line_list, **kwargs)
