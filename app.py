<script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    // يقبل Phone يبدأ بـ 07 وطوله 10
    // أو ID طوله 11
    if(/^07[0-9]{8}$/.test(v) || /^[0-9]{11}$/.test(v)){
        window.top.location.href = "/?page=employee";
    } else {
        e.innerText = "Enter valid phone number or ID";
    }
}
</script>
