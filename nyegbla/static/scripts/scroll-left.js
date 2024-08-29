// Create a CSS animation keyframe
const keyframes = `
@keyframes scrollLeft {
    70% {
        transform: translateX(-10%);
    }
    80% {
        transform: translateX(-20%);
    }
}`;

// Create a style element and append the keyframes to it
const style = document.createElement('style');
style.innerHTML = keyframes;
document.head.appendChild(style);

// Apply the animation to the text element
$(document).ready(function () {
    $('#welcome').css('animation', 'scrollLeft 10s linear infinite');
});



// Fade away the flask flash message after 4 seconds
$(document).ready(function () {
    // Automatically close alert messages after 5 seconds
    window.setTimeout(function () {
        var alerts = $(".alert");
        console.log("Alerts found:", alerts.length);
        $(".alert").fadeTo(500, 0).slideUp(500, function () {
            $(this).remove();
        });
    }, 5000); // 5000 milliseconds = 5 seconds
});


$(document).ready(() => {
    const $pro_form = $("#profile-form");
    var $save_upt = $('#save_upt');
    const $contain_name = $('#first_name');

    if ($contain_name.val().trim() !== '') {
        $save_upt.text("Update");
      // $pro_form.method = 'put'
    }
});

$(document).ready(function () {
    //load image from local disk
    var image = new Image();
    image.src = "/static/images/nyegbla.jpg";
});


//Logging Out a user
