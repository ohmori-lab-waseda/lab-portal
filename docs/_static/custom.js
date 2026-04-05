document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a.reference.external").forEach(function (a) {
    a.setAttribute("target", "_blank");
    a.setAttribute("rel", "noopener noreferrer");
  });
});
