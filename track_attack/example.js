// function fetchData() {
//     fetch("https://reqres.in/api/users")
//         .then(response => response.json())
//         .then(data => console.log(data.data));
// }

// // function fetchData() {
// //     fetch("https://reqres.in/api/users")
// //         .then(response => { response.json(); })
// //         .then(data => {
// //             const firstUser = data.data[0].email;
// //             console.log(firstUser);

// //         });
// // }

// // function fetchData() {
// //     console.log(fetch("https://reqres.in/api/users"));
// // }

function fetchData() {
    fetch("https://reqres.in/api/users")
        .then(response => response.json())
        .then(data => {
            const firstUser = data.data[0].id;
            console.log(firstUser);
            document.querySelector(".input").textContent = firstUser;
        })
        .catch(error => console.log(error));
}


fetchData();