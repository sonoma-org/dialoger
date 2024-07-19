function reg(url, body) {
  const xhr = new XMLHttpRequest()
  xhr.open('POST', url, true)
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      window.location.replace("/login")
    } else { toastr.warning("Такой пользователь уже есть") }
  };
  xhr.send(JSON.stringify(body))
}

function log(url, body) {
  const xhr = new XMLHttpRequest()
  xhr.open('POST', url, true)
  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      window.location.replace("/im")
    } else { toastr.error("Неверный логин или пароль") }
  };
  xhr.send(JSON.stringify(body))
}

function register() {

    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    let repeat_password = document.getElementById("repeat_password").value

    if (password == "" | username == "" | repeat_password == "" | repeat_password, password, username == "") {
      toastr.error("Не все поля заполнены")
    } else if (repeat_password == password) {
      reg('/api/register', {"username": username, "password": password})
    } else {
      toastr.error("Пароли не совпадают")
    }
}

function login() {
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value

    if (password == "" | username == "" | password, username == "") {
      toastr.error("Не все поля заполнены")
    } else { log('/api/login', {"username": username, "password": password}) }
}