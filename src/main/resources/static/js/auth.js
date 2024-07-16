function register() {
    let formData = new FormData(document.forms.auth)
    let req = new XMLHttpRequest()
    req.open("POST", "/api/register")

    req.send(formData)
    xhr.onload = () => alert(xhr.response)
}