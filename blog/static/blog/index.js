const comment_form= document.querySelector('#comment-form');
const comment_button=document.querySelector('#comment-btn');

comment_button.addEventListener('click',displayForm);

function displayForm(){
    comment_form.style.display="block";
}