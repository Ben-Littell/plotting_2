import matplotlib.pyplot as plt


def open_file(file_name):
    new_list1 = []
    new_list2 = []
    with open(file_name) as file:
        lines = file.readlines()
        for item in lines[1:]:
            new_list1.append(item.strip())
    for item in new_list1:
        new_list2.append(item.split('\t'))
    return new_list2


def split_values2(values):
    xs = []
    ys = []
    for item in values:
        xs.append(float(item[0]))
        ys.append(float(item[1]))
    return xs, ys


def split_values4(values):
    set1 = []
    set2 = []
    set3 = []
    set4 = []
    for item in values:
        set1.append(float(item[0]))
        set2.append(float(item[1]))
        set3.append(float(item[2]))
        set4.append(float(item[3]))
    return set1, set2, set3, set4


def find_centroid(x, y):
    counter_x = 0
    counter_y = 0
    for numb in x:
        counter_x += numb
    for numb in y:
        counter_y += numb
    x_centroid = counter_x / len(x)
    y_centroid = counter_y / len(y)
    return x_centroid, y_centroid


def draw_rectangle(x, y, x_width, y_width):
    left_x = x - x_width / 2
    top_y = y - y_width / 2
    right_x = x + x_width / 2
    bottom_y = y + y_width / 2


def plot_data(title, x, y, x_label, y_label, plot_code='-xr', centroid='n', horizontal='n', vertical='n'):
    x_min = min(x)
    x_max = max(x)
    y_max = max(y)
    y_min = min(y)
    x_centroid, y_centroid = find_centroid(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, plot_code)
    if centroid == 'y':
        plt.plot(x_centroid, y_centroid, 'xb')
        plt.text(x_centroid, y_centroid, 'This is the centroid')
        if vertical == 'y':
            plt.axvline(x=x_centroid)
        if horizontal == 'y':
            plt.axhline(y=y_centroid)
    plt.axis([x_min, x_max, y_min, y_max])
