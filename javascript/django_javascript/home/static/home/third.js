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

// const form = document.querySelector('form')
//
// form.addEventListener('submit', event => {
//     event.preventDefault()
//
//     const title = form.title.value
//     const text = form.text.value
//     const description = form.description.value
//
//     saveForm({title, text, description})
// })

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
// function saveForm(...args) {
//     const [title, text, description] = args
//
//     const formData = {
//         date: new Date().toLocaleDateString(),
//         title, text, description
//     }
//
//     console.log('Form data:', formData)
// }


// Strings
const createLink = ({path, name}) => `<a target="_blank" href="${path}">${name}</a>`

const ul = document.querySelector('ul')

const google = `<li>${createLink({path: 'https://google.com', name: 'Google'})}</li>`

const habr = `<li>${createLink({path: 'https://habr.com', name: 'Habr'})}</li>`

ul.insertAdjacentHTML('afterbegin', google)
ul.insertAdjacentHTML('afterbegin', habr)



//RootElement <= Box <= Instance
// class RootElement {
//     constructor(tagName = 'div') {
//         this.$el = document.createElement(tagName)
//         this.$el.style.marginBottom = '20px'
//     }
//
//     hide() {
//         this.$el.style.display = 'none'
//     }
// }
//
// class Box extends RootElement {
//     constructor(color, size = 150, tagName) {
//         super(tagName)
//         this.color = color
//         this.size = size
//     }
//
//     create() {
//         this.$el.style.background = this.color
//         this.$el.style.width = this.$el.style.height = '${this.size}px'
//
//         document.querySelector('.wrapper').insertAdjacentElement('afterbegin', this.$el)
//
//         return this
//     }
// }
//
// const redBox = new Box('red', 100, 'div').create()
// const blueBox = new Box('blue').create()