const $divContainerForm = document.getElementById("form-mailMark");
const $btnShowForm = document.getElementById("btn-show-form");
const $submitMailMark = document.getElementById("submitMailMark")

$btnShowForm.addEventListener('click', () => {
    $divContainerForm.style.display = 'block';
})

// $submitMailMark.addEventListener('click', (e) => {
//     e.preventDefault();
//     let usersMail = [];
//     document.querySelectorAll('.table tbody tr').forEach((e) => {
//         let fila = {
//             id: e.querySelector(".id").innerText,
//             name: e.querySelector(".name").innerText,
//             email: e.querySelector(".email").innerText,
//             confirmed: e.querySelector(".confirmed").checked
//         }
//         usersMail.push(fila)
//     })
//     fetch('http://127.0.0.1:5000/admin/users/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         mode: 'cors',
//         body: usersMail
//     })
//     .then(function(response) {
//         if (response.ok) {
//             return response.text();
//         } else {
//             throw "Error en la llamada Ajax";
//         }
//     })
//     .then(function(texto) {
//         console.log("texto")
//         console.log(texto)
//     })
//     .catch(function(err) {
//         console.log("err")
//         console.log(err)
//     })
//     // " {{ current_app.config['ENVIRON'] }} "= usersMail
// })