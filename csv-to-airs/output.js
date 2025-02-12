var ids = ['22101535', '22102918', '22002783', '22102475', '22002306', '22001859', '22103625', '22102248', '22003097', '22301131', '22103729', '22103156', '22002299', '22003396', '22103885', '22103524', '22102692', '22103341', '22103759', '22101852', '22103034', '22101911', '22002756', '22002722', '21901476', '22101038', '22101920', '22101643', '22101018', '21903151', '22103163', '22102409', '22102825', '22002275', '22003920', '22102144', '22102198', '22002730', '22002885', '22101343', '22103582', '22102932', '22103111', '22003330', '22101310', '22102544'];
var grades = ['22.22', '27.78', '61.11', '22.22', '77.78', '72.22', '11.11', '22.22', '33.33', '88.89', '22.22', '11.11', '83.33', '83.33', '77.78', '66.67', '83.33', '38.89', '44.44', '44.44', '11.11', '27.78', '27.78', '44.44', '22.22', '61.11', '50', '55.56', '33.33', '77.78', '61.11', '44.44', '77.78', '44.44', '72.22', '27.78', '38.89', '77.78', '66.67', '94.44', '11.11', '33.33', '27.78', '83.33', '61.11', '27.78'];

var elements = document.querySelectorAll('[id^="stdSubGrades_"]');

elements.forEach(function(element) {
    var id = element.id.replace(new RegExp("^stdSubGrades_"), "");
    var student_index = ids.indexOf(id);
    if (student_index !== -1) {
        element.value = grades[student_index];
    } else {
        console.log("ID not found:", id); // Logging out the ID if not found in the list
    }
});
