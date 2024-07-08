/*!
* Start Bootstrap - Scrolling Nav v5.0.6 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 
console.log
window.addEventListener('DOMContentLoaded', event => {


    // Activate Bootstrap scrollspy on the main nav element
    // const mainNav = document.body.querySelector('#mainNav');
    // if (mainNav) {
    //     new bootstrap.ScrollSpy(document.body, {
    //         target: '#mainNav',
    //         rootMargin: '0px 0px -40%',
    //     });
    // };

    // Collapse responsive navbar when toggler is visible
    // const navbarToggler = document.body.querySelector('.navbar-toggler');
    // const responsiveNavItems = [].slice.call(
    //     document.querySelectorAll('#navbarResponsive .nav-link')
    // );
    // responsiveNavItems.map(function (responsiveNavItem) {
    //     responsiveNavItem.addEventListener('click', () => {
    //         if (window.getComputedStyle(navbarToggler).display !== 'none') {
    //             navbarToggler.click();
    //         }
    //     });
    // });
    //Swapping images on the footer
    const imgContainer = document.querySelector(".slidding-image-container")
    const imgSliding = document.querySelector(".sliding")
    const imageDir = "/static/asset/sliding/";
    const imgList = ['1.jpg', '2.jpg', '3.jpg'];
    let imageIndex = 0;
    if (imgSliding) {
        imgSliding.src = imageDir + imgList[imageIndex];
    } else {
        console.error("Could not find element with class 'sliding'");
    }
    imgContainer.addEventListener('click', slideImages)
    setInterval(slideImages, 4000);

    function slideImages() {
        imageIndex = (imageIndex + 1) % imgList.length
        imgSliding.src = imageDir + imgList[imageIndex]
        console.log("Image index: " + imgSliding.src)
    }

});


