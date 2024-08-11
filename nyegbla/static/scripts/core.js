/*!
* Start Bootstrap - Scrolling Nav v5.0.6 (https://startbootstrap.com/template/scrolling-nav)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-scrolling-nav/blob/master/LICENSE)
*/
//
// Scripts
// 
console.log
// window.addEventListener('DOMContentLoaded', event => {


//     //Swapping images on the footer
//     const imgContainer = document.querySelector(".slidding-image-container")
//     const imgSliding = document.querySelector(".sliding")
//     const imageDir = "/static/asset/sliding/";
//     const imgList = ['1.jpg', '2.jpg', '3.jpg'];
//     let imageIndex = 0;
//     if (imgSliding) {
//         imgSliding.src = imageDir + imgList[imageIndex];
//     } else {
//         console.error("Could not find element with class 'sliding'");
//     }
//     imgContainer.addEventListener('click', slideImages)
//     setInterval(slideImages, 4000);

//     function slideImages() {
//         imageIndex = (imageIndex + 1) % imgList.length
//         imgSliding.src = imageDir + imgList[imageIndex]
//         console.log("Image index: " + imgSliding.src)
//     }


    
    
// });


  // HIDE AND SHOW ALL STAFF PROFILE FORM

  $(document).ready(function(){
    $('#profile-btn').click(function(){
        $('#profile-form').toggle('hideform');
    });
    });

    $(document).ready(() =>{
        $('#prof-form').hide();
        $('#prof-btn').click(() =>{
            $('#prof-form').toggle('hideform');
        });
    });

    $(document).ready(() => {
        $('#promotion-form').hide();
        $('#promote-btn').click(() =>{
            $('#promotion-form').toggle('hideform')
        })
    })

   
    $(document).ready(() => {
        var counter = 0;
        $('#more_prof').click(() => {
            var newLabel = $('<label>').attr({
                'for': 'moreProf',
                'id': 'more_prof',
                'name': 'Institution',
            });
            var newInput = $('<input>').attr({
                'type': 'text',
                'for': 'moreProf',
                'id': 'more_prof',
                'name': 'more_prof',
                'placeholder': 'Enter staff profile',
            });
            $('#prof-form').append(newLabel).append(newInput).append('<br>');
        });
    });

   