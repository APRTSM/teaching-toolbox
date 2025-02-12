
var ids = ['21901440', '22001482', '22001734', '22001736', '22002553', '22002600', '22002672', '22101362', '22101539', '22102084', '22102101', '22102334', '22102541', '22102898', '22103231', '22103294', '22103340', '22103640', '22103867', '22201182', '22201438', '22201439', '22201590', '22201668', '22201690', '22201809', '22201926', '22202461', '22202977', '22203014', '22203112', '22203238', '22203317', '22203340', '22203360', '22203367', '22203673', '22203818'];
var grades = [2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2];


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
