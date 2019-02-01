document.addEventListener('DOMContentLoaded', () => {
    
    document.querySelector('#submit').disabled = true;
    document.querySelector('#new-note').onkeyup = () => {
        if (document.querySelector('#new-note').value.length > 0 ) 
            document.querySelector('#submit').disabled = false;
        else
            document.querySelector('#submit').disabled = true;
    };
    document.querySelector('form').onsubmit = () => {
        document.querySelector('#submit').disabled = true;
    };

    //document.querySelector('a').addEventListener("mouseover", () => { document.querySelector('a').innerHTML = "\u{2718}";}); 
});