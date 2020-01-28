svg_data = "M90,47.6933V47.7504C90,50.1101 89.0719,52.3258 87.3888,53.992L43.0439,98.2898C42.4585,98.8843 41.4395,98.473 41.4395,97.6413V93.6814C41.4395,92.9158 41.1332,92.1803 40.5873,91.6399L2.311,53.6888C0.7218,52.1156 -0.1122,49.945 0.0122,47.7234C0.0122,47.7169 0.0113,47.7113 0.0105,47.7062C0.0098,47.7017 0.0091,47.6975 0.0091,47.6933C0.0091,45.3366 0.9371,43.1209 2.6203,41.4547L44.0144,0.4053C44.5602,-0.1351 45.4458,-0.1351 45.9917,0.4053L87.3918,41.4547C89.075,43.1209 90,45.3366 90,47.6933ZM41.4514,78.298L41.691,68.1445C41.6971,67.9314 41.6152,67.7272 41.4666,67.5771L15.7822,41.6109C15.4638,41.2896 14.9421,41.2866 14.6206,41.6049L10.76,45.4267C10.4688,45.7599 9.9654,46.4835 9.9654,47.5553C9.9654,48.9873 10.8843,49.8159 10.8843,49.8159L40.1018,78.8324C40.5931,79.3218 41.4362,78.9886 41.4514,78.298ZM41.9251,58.3184C41.913,58.8618 41.267,59.144 40.8515,58.7867L18.3061,39.3593C17.8966,39.0081 17.8754,38.3836 18.2575,38.0053L28.3657,27.9989C28.7327,27.6357 29.3241,27.6357 29.691,27.9989L42.1496,40.3201C42.2739,40.4432 42.3437,40.6143 42.3406,40.7884L41.9251,58.3184ZM41.8275,34.2282C42.0883,34.4504 42.4947,34.2733 42.5008,33.934L42.9617,14.5307C42.9708,14.1674 42.5281,13.9782 42.2672,14.2364L31.8285,24.5701C31.5283,24.8673 31.5465,25.3537 31.8649,25.6299L41.8275,34.2282ZM47.0439,14.5309C47.0378,14.1646 47.4806,13.9785 47.7414,14.2367L58.1801,24.5703C58.4804,24.8676 58.4622,25.3539 58.1438,25.6301L48.1812,34.2285C47.9203,34.4537 47.514,34.2765 47.5049,33.9343L47.0439,14.5309ZM47.8571,40.3171C47.7327,40.4401 47.663,40.6113 47.666,40.7854L48.0815,58.3154C48.0936,58.8588 48.7396,59.141 49.1551,58.7837L71.7006,39.3563C72.11,39.0051 72.1342,38.3836 71.7491,38.0023L61.6409,27.9959C61.274,27.6357 60.6826,27.6357 60.3156,27.9959L47.8571,40.3171ZM80.0434,47.5583C80.0464,48.9903 79.1245,49.819 79.1245,49.819L49.9069,78.8355C49.4156,79.3248 48.5725,78.9916 48.5574,78.3011L48.3178,68.1475C48.3117,67.9374 48.3936,67.7332 48.5422,67.5801L74.2266,41.6139C74.545,41.2926 75.0666,41.2896 75.3881,41.6079L79.2488,45.4297C79.54,45.76 80.0434,46.4865 80.0434,47.5583Z"


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