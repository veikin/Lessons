// for (let i =0; i < 5; i++) {
//     setTimeout(function () {
//         console.log(i)
//     }, 2000)
// }

// var HEX = '#FFAABB'
//
// document.querySelector('h1').style.color = HEX

// function getAge(year) {
//     const current = new Date().getFullYear()
//     return current - year
// }
//
// const calculateAge = (year) => {
//     const current = new Date().getFullYear()
//     return current - year
// }
//
// const getAge = year => {
//     const current = new Date().getFullYear()
//     return current - year
// }

// const getAge = year => new Date().getFullYear() - year
//
// const logAge = year => console.log(new Date().getFullYear() - year)
// logAge(1956)
//
// console.log(getAge(1946))

// const person = {
//     age: 30,
//     firstName: 'Andrei',
//     logNameWithTimeout: function () {
//         window.setTimeout(function () {
//             console.log(this.firstName)
//         }.bind(this), 1000)
//     }
// }

// const createPost = (title, text = 'Default text', date = new Date().toLocaleDateString()) => {
//     return {
//         title: title,
//         text: text,
//         date: date
//     }
// }
//
// const post = createPost('Test')
// console.log(post)

// const createCar = (name, model) => {
//     return {name, model}
// }
//
// const ford = createCar('Ford', 'Focus')
//
// console.log(ford)

const form = document.querySelector('form')

form.addEventListener('submit', event => {
    event.preventDefault()

    const title = form.title.value
    const text = form.text.value
    const description = form.description.value

    saveForm({title, text, description})
})

// Spread
// function saveForm(data) {
//
//     const formData = {
//         date: new Date().toLocaleDateString(),
//         ...data
//     }
//
//     console.log('Form data:', formData)
// }

// Rest
function saveForm(...args) {
    const [title, text, description] = args

    const formData = {
        date: new Date().toLocaleDateString(),
        title, text, description
    }

    console.log('Form data:', formData)
}