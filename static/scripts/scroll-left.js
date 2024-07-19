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
const textElement = document.getElementById('welcome');
textElement.style.animation = 'scrollLeft 10s linear infinite';

// Fade away the flask flash message after 4 seconds
$(document).ready(function() {
    // Automatically close alert messages after 5 seconds
    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 5000); // 5000 milliseconds = 5 seconds
});
