const comment_form= document.querySelector('#comment-form');
const comment_button=document.querySelector('#comment-btn');
const cancel_button=document.querySelector('.cancel-btn');

comment_button.addEventListener('click',displayForm);
cancel_button.addEventListener('click',removeForm);





function displayForm(){
    comment_form.style.display="block";
}

function removeForm(){
    if (comment_form.style.display=="block"){
        comment_form.style.display="none";
    }
}