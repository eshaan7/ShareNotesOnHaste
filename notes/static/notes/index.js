document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('.submit').disabled = true;
    document.querySelector('#new-note').onkeyup = () => {
        if (document.querySelector('#new-note').value.length > 0 ) 
            document.querySelector('.submit').disabled = false;
        else
            document.querySelector('.submit').disabled = true;
    };
    document.querySelector('form').onsubmit = () => {
        document.querySelector('.submit').disabled = true;
    };
});

function editNote(btn) {
    divEl = btn.parentElement.parentElement;
    divEl.innerHTML = "";
    //divEl.className = "input-form";
    var form = document.createElement('form');
    form.setAttribute("method", "post");
    form.setAttribute("action", "{% url 'index' %}");
    form.innerHTML = '{% csrf_token %}<textarea id="new-note" name="note" draggable="false" placeholder="Enter Note..."></textarea><button class="btn btn-dark" class="submitbtn">Edit note</button>';
    divEl.appendChild(form);
}