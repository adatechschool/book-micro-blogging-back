import { mount } from "svelte";
import "./app.css";
import App from "./pages/App.svelte";
import Profile from "./pages/Profile.svelte";

const getCurrentPage = () => {
  const path = window.location.pathname;

  if (path === "/users") {
    return "users";
  } else if (path === "/profile") {
    return "profile";
  }

  return null;
};

// Montage conditionnel
const currentPage = getCurrentPage();

let app;

if (currentPage === "users") {
  app = mount(App, {
    target: document.getElementById("app"),
  });
} else if (currentPage === "profile") {
  app = mount(Profile, {
    target: document.getElementById("app"),
  });
}

export default app;
