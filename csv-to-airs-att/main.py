import csv

def csv_to_js_array(csv_file):
    ids = []
    grades = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=' ')

        for row in reader:
            row = row[0].split(',')
            ids.append(row[0])
            grades.append(row[1])

    return ids, grades

if __name__ == "__main__":
    csv_file = 'data.csv'
    output_js_file = 'output.js'
    ids, grades = csv_to_js_array(csv_file)

    js_code = f"""
        var ids = {ids}
        var grades = {grades};
    """ + """
        
        var elements = document.querySelectorAll('[id^="stdSubGrades_"]');

        elements.forEach(function(element) {
            id = element.id.replace(new RegExp("^" + "stdSubGrades_"), "")
            student_index = ids.indexOf(id);
            if (student_index !== -1) {
            element.value = grades[student_index]
            }
        });
    """

    with open(output_js_file, 'w') as js_file:
        js_file.write(js_code)