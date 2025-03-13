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


    //Swapping images on the footer
    const imgContainer = document.querySelector("#drugless")
    const imgSliding = document.querySelector(".sele")  
    const imageDir = "/static/asset/images/drugless/";
    const imgList = ['at-kwame-nkrumah-center.jpg', 'at-parliament-hourse-1.jpg', 'at-parliament-hourse.jpg','IMG-20240809-WA0088.jpg'];
    let imageIndex = 0;
    if (imgSliding) {
        imgSliding.src = imageDir + imgList[imageIndex];
    } else {
        console.error("Could not find element with class 'sliding'");
    }
    imgContainer.addEventListener('click', slideImages)


    function slideImages() {
        imageIndex = (imageIndex + 1) % imgList.length
        imgSliding.src = imageDir + imgList[imageIndex]
        console.log("Image index: " + imgSliding.src)
    }

});

// Drugless program galery  
console.log
 window.addEventListener('DOMContentLoaded', event => {


    //Swapping images on the footer
    const imgContainer = document.querySelector("#hpm")
    const imgSliding = document.querySelector(".sele")  
    const imageDir = "/static/asset/images/hpm/";
    const imgList = ['form_one.jpg', 'level100_at_praise.jpg', 'praise_leader.jpg','praises.jpg'];
    let imageIndex = 0;
    if (imgSliding) {
        imgSliding.src = imageDir + imgList[imageIndex];
    } else {
        console.error("Could not find element with class 'sliding'");
    }
    imgContainer.addEventListener('click', slideImages)


    function slideImages() {
        imageIndex = (imageIndex + 1) % imgList.length
        imgSliding.src = imageDir + imgList[imageIndex]
        console.log("Image index: " + imgSliding.src)
    }

});


//HIV program galery

console.log
 window.addEventListener('DOMContentLoaded', event => {
    
    //Swapping images on the footer
    const imgContainer = document.querySelector('#background')                     
    const imageDir = "/static/asset/images/home_back/";
    const imgList = ['prams_admin.jpg', 'campus.jpg','form_two.jpg'];
    let imageIndex = 0;
    if (imgContainer) {
        imgContainer.style.backgroundImage = 'url(' + imageDir + imgList[imageIndex]+ ')';
        imgContainer.style.backgroundPosition = '100% center';  // Start the background image off-screen to the right
        imgContainer.style.transition = 'background-position 1s ease-out';
    } else {
        console.error("Could not find element with class 'sliding'");
    }

    setInterval(slideImages, 4000)

    function slideImages() {
        imageIndex = (imageIndex + 1) % imgList.length
        imgContainer.style.backgroundImage = 'url(' + imageDir + imgList[imageIndex]+ ')';
        imgContainer.style.backgroundPosition = '100% center';

        // Trigger a reflow to ensure the transition works after changing the background image
        imgContainer.offsetHeight;  // Trigger a reflow

        // After a brief delay (to allow for the reflow), animate the image to the center
        setTimeout(() => {
            imgContainer.style.backgroundPosition = '0% center';
        }, 10);
    }

});

//Prefect Speech
console.log
 window.addEventListener('DOMContentLoaded', event => {


    //Swapping images on the footer
    const imgContainer = document.querySelector("#handover")    
    const imgSliding = document.querySelector(".sele")
    const imageDir = "/static/asset/images/handover/";
    const imgList = ['hnd-over.jpg', 'induction.jpg', 'sspeech.jpg','sttaff_studentt.jpg'];
    let imageIndex = 0;
    if (imgSliding) {
        imgSliding.src = imageDir + imgList[imageIndex];
    } else {
        console.error("Could not find element with class 'sliding'");
    }
    imgContainer.addEventListener('click', slideImages)


    function slideImages() {
        imageIndex = (imageIndex + 1) % imgList.length
        imgSliding.src = imageDir + imgList[imageIndex]
        console.log("Image index: " + imgSliding.src)
    }

});

 // HIDE AND SHOW ALL STAFF PROFILE FORM

  $(document).ready(function(){
    $('#profile-btn').click(() =>{
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

   // ADDING MORE STAFF QUALIFICATION FORM
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


    //LOADING PROFILE IMAGE AT PROFILE FORM IN USER DASHBOARD
  
    document.getElementById('pickImageBtn').addEventListener('click', function() {
        document.getElementById('fileInput').click();
    });

    document.getElementById('fileInput').addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = document.getElementById('imageDisplay');
                img.src = e.target.result;
                img.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });

    $(document).ready(() => {
        const $pro_form = $("#profile-form");
        var $save_upt = $('#save_upt');
        const $contain_name = $('#first_name');
    
        if ($contain_name.text().trim() !== '') {
            $save_upt.text("Update");
          // $pro_form.method = 'put'
        }
    });
    //LOADING PROFILE IMAGE AT PROFILE FORM IN USER DASHBOARD

    $(document).ready(() => {
        $('#password').click(() =>{
            alert("hello")
        })
    })


    function submitForm(method) {
        const form = document.getElementById('profile-form');
    
        fetch(actionUrl, fetchOptions)
            .then(response => {
                // Handle the response
                return response.json()// Assuming the server responds with JSON
            })
            .then(data => {
                console.log(data); // Handle the data received
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }