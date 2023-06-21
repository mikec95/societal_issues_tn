// Collapse the navbar after a link is clicked
$(".navbar-nav>li>a").on("click", function () {
  $(".navbar-collapse").collapse("hide");
  $(".navbar-toggler").addClass("collapsed");
});
