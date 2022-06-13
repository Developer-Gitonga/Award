let exit2 = document.getElementById('exit2');
let open2 = document.getElementById('open2');
let openmobile2 = document.getElementById('openmobile2');
let element2 = document.getElementById('element2');

element2.style.display = 'none';

exit2.addEventListener('click', function() {
    element2.style.display = 'none';
});

open2.addEventListener('click', function() {
    element2.style.display = 'flex';
});
openmobile2.addEventListener('click', function() {
    element2.style.display = 'flex';
});