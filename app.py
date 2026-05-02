<script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    if(/^07[0-9]{8}$/.test(v) || /^[0-9]{11}$/.test(v)){
        window.top.location.href = "/?page=employee";
    } else {
        e.innerText = "Enter valid phone number or ID";
    }
}
</script>
