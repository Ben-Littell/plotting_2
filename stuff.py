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


def string_to_int(file):
    new_list = []
    for item in file:
        for numb in item:
            new_list.append(int(numb))
    return new_list


def split_values2(values):
    xs = []
    ys = []
    for item in values:
        xs.append(float(item[0]))
        ys.append(float(item[1]))
    return xs, ys


def split_values3(values):
    set1 = []
    set2 = []
    set3 = []
    for item in values:
        set1.append(item[0])
        set2.append(float(item[1]))
        set3.append(float(item[2]))
    return set1, set2, set3


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


def draw_rectangle(cx, cy, x_width, y_width, x_data, y_data):
    range_y = max(y_data) - min(y_data)
    range_x = max(x_data) - min(x_data)
    left_x = cx - x_width * range_x / 2
    top_y = cy - y_width * range_y / 2
    right_x = cx + x_width * range_x / 2
    bottom_y = cy + y_width * range_y / 2
    x_rect = [left_x, right_x, right_x, left_x, left_x]
    y_rect = [top_y, top_y, bottom_y, bottom_y, top_y]
    plt.fill(x_rect, y_rect, 'b')


def plot_data(title, x, y, x_label, y_label, plot_code='-xr', centroid='n', horizontal='n', vertical='n',
              rectangle='n'):
    x_min = min(x)
    x_max = max(x)
    y_max = max(y)
    y_min = min(y)
    x_centroid, y_centroid = find_centroid(x, y)
    if rectangle == 'y':
        draw_rectangle(x_centroid, y_centroid, 1, 1, x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(x, y, plot_code)
    if centroid == 'y':
        plt.plot(x_centroid, y_centroid, 'xr')
        plt.text(x_centroid, y_centroid, 'This is the centroid')
        if vertical == 'y':
            plt.axvline(x=x_centroid)
        if horizontal == 'y':
            plt.axhline(y=y_centroid)
    plt.axis([x_min, x_max, y_min, y_max])


def plot_histogram(x1, n_bins, title1, y_label1):
    plt.title(title1)
    plt.ylabel(y_label1)
    plt.hist(x1, n_bins)


def plot_py_chart(title1, title2, x1, x2, label1, label2, colors):
    plt.subplot(1, 2, 1)
    plt.title(title1)
    plt.pie(x1, labels=label1, colors=colors)
    plt.axis('equal')
    plt.subplot(1, 2, 2)
    plt.title(title2)
    plt.pie(x2, labels=label2, colors=colors)
    plt.axis('equal')


t_p_file = open_file('temp_and_pressure.txt')
x_t_p, y_t_p = split_values2(t_p_file)
plot_data('Temp to Pressure', x_t_p, y_t_p, 'Temp', 'Pressure', centroid='y', plot_code='xg', rectangle='y')
plt.show()
t_s_file = open_file('test_scores.txt')
int_t_s_file = string_to_int(t_s_file)
plot_histogram(int_t_s_file, [60, 70, 80, 92, 100], 'Test Scores', 'Counts')
plt.show()
p_s_data = open_file('sales_data.txt')
names, data1, data2 = split_values3(p_s_data)
color_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'green']
plot_py_chart('Sales to Person', 'Dollar to Person', data1, data2, names, names, color_list)
plt.show()
