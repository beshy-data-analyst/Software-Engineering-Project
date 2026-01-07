const container = document.querySelector(".container");

function showRegister() {
  container.classList.add("active");
}

function showLogin() {
  container.classList.remove("active");
}

window.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const preloader = document.getElementById('preloader');
    preloader.style.opacity = "0";
    preloader.style.top = "-100vh";

    setTimeout(() => {
      preloader.style.display = "none";
    }, 800);
  }, 2000);
});
