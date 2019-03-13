// var p = document.querySelectorAll('p')
//
// for (var i = 0; i < p.length; i++) {
//     p[i].addEventListener('click', function(event) {
//         event.target.style.color = 'lightblue'
//     })
// }

document.getElementById('wrapper').addEventListener('click', function(event) {
    console.log(event.target)
})