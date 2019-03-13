// var p = document.querySelectorAll('p')
//
// for (var i = 0; i < p.length; i++) {
//     p[i].addEventListener('click', function(event) {
//         event.target.style.color = 'lightblue'
//     })
// }

document.getElementById('wrapper').addEventListener('click', function(event) {
    var tagName = event.target.tagName.toLowerCase()

    if (tagName === 'p') {
        event.target.style.color = 'blue'
    }

    if (event.target.classList.contains('color')) {
        event.target.style.color = 'orange'
    }
})

document.querySelector('#alert').addEventListener('click', function () {
    alert('Успех!')
})

document.querySelector('#confirm').addEventListener('click', function () {
    var decision = confirm('Вы уверены,?')

    if (decision) {
        alert('Успех!')
    }
})

document.querySelector('button').addEventListener('click', function(event) {
    var value = document.querySelector('input').value

    localStorage.setItem('headerText', value)

})