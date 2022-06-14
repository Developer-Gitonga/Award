let exit = document.getElementById('exit');
let open = document.getElementById('open');
let openmobile = document.getElementById('openmobile');
let element = document.getElementById('element');

exit.addEventListener('click', function() {
    element.style.display = 'none';
});

open.addEventListener('click', function() {
    element.style.display = 'flex';
});
openmobile.addEventListener('click', function() {
    element.style.display = 'flex';
});
