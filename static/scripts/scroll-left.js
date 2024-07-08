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