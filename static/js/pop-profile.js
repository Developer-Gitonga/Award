let exit3 = document.getElementById('exit3');
let open3 = document.getElementById('open3');
let openmobile3 = document.getElementById('openmobile3');
let element3 = document.getElementById('element3');

element3.style.display = 'none';

exit3.addEventListener('click', function() {
    element3.style.display = 'none';
});

open3.addEventListener('click', function() {
    element3.style.display = 'flex';
});
openmobile3.addEventListener('click', function() {
    element3.style.display = 'flex';
});