import { mount } from "svelte";
import "./app.css";
import App from "./pages/App.svelte";
import Profile from "./pages/Profile.svelte";
import Home from "./pages/Home.svelte";
import Login from "./pages/Login.svelte";

const getCurrentPage = () => {
  const path = window.location.pathname;

  if (path === "/users") {
    return "users";
  } else if (path === "/profile/5/") {
    return "profile";
  } else if (path === "/") {
    return "home";
  } else if (path === "accounts/login/") {
    return "login";
  }

  return null;
};

// Montage conditionnel
const currentPage = getCurrentPage();

let app;

if (currentPage === "home") {
  app = mount(App, {
    target: document.getElementById("app"),
  });
} else if (currentPage === "profile") {
  app = mount(Profile, {
    target: document.getElementById("app"),
  });
} else if (currentPage === "users") {
  app = mount(Home, {
    target: document.getElementById("app"),
  });
} else if (currentPage === "login") {
  app = mount(Login, {
    target: document.getElementById("app"),
  });
}

export default app;
