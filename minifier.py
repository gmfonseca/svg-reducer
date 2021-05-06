svg_data = "YOUR_SVG_HERE"


def minify_svg_data(data, with_precision=False):
    final_data = ''
    i = 0
    while i in range(len(data)):
        try:
            int(data[i])
            final_data += data[i]
        except ValueError:
            if data[i] == '.':
                if with_precision and int(data[i + 1]) > 0:
                    final_data += data[i] + data[i + 1]
                i += 1
                try:
                    while i < len(data):
                        int(data[i])
                        i += 1
                except ValueError:
                    final_data += data[i]
            else:
                final_data += data[i]
        i += 1
    return final_data


def save_file(filename, data):
    file = open(filename, 'w')
    file.write(data)


save_file("mini_svg.txt", minify_svg_data(svg_data, True))
