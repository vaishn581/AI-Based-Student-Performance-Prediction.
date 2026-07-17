document.getElementById("predictionForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let studyHours = document.getElementById("study_hours").value;
    let attendance = document.getElementById("attendance").value;
    let previousMarks = document.getElementById("previous_marks").value;

    document.getElementById("result").innerHTML =
        "Prediction request sent successfully! (Backend will be connected next)";
});
