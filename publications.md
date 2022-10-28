---
layout: default
title: "Publications"
order: 2
---

# Publications #

<script src="https://bibbase.org/show?bib=https://raw.githubusercontent.com/bethard/bethard.github.io/main/assets/bethard.bib&jsonp=1&fullnames=1"></script>
<script>
// hack bibbase toggles to work with Bootstrap 5
bibbaseHeaderElem = document.getElementById("bibbase_header");
for (dropdownToggleElem of bibbaseHeaderElem.getElementsByClassName("dropdown-toggle")) {
    dropdownToggleElem.setAttribute("data-bs-toggle", "dropdown")
}
for (menuElem of bibbaseHeaderElem.getElementsByClassName("dropdown-menu")) {
    for (aElem of menuElem.getElementsByTagName("a")) {
        aElem.classList.add("dropdown-item");
    }
}
for (dropdownElem of bibbaseHeaderElem.getElementsByClassName("dropdown")) {
    dropdownElem.classList.add("pe-3");
}
</script>
