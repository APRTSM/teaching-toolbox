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

    grades = [2 if i else 0 for i in grades]

    js_code = f"""
        var ids = {ids};
        var grades = {grades};
    """ + """
        
        var elements = document.querySelectorAll('[id^="stdAtt_"]');

        elements.forEach(function(element) {
            var id = element.id.replace(new RegExp("^" + "stdAtt_"), "");
            var student_index = ids.indexOf(id);
            if (student_index !== -1) {
                // Retrieve the desired value for this student
                var desiredValue = grades[student_index];

                // Get all option elements within the current select element
                var options = element.options;

                // Loop through all options and set the 'selected' attribute accordingly
                for (var i = 0; i < options.length; i++) {
                    if (options[i].value == desiredValue) {
                        options[i].selected = true;
                    } else {
                        options[i].selected = false;
                    }
                }
            }
        });
    """

    with open(output_js_file, 'w') as js_file:
        js_file.write(js_code)