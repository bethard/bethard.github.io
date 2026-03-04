---
layout: default
title: "FAQ"
order: 1
---

# Frequently Asked Questions #

<div class="accordion accordion-flush" id="faq">
  {% for question in site.data.faq.questions %}
  <div class="accordion-item">
    <h2 class="accordion-header" id="heading{{ forloop.index }}">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{{ forloop.index }}" aria-expanded="false" aria-controls="collapse{{ forloop.index }}">
        {{ question.q }}
      </button>
    </h2>
    <div id="collapse{{ forloop.index }}" class="accordion-collapse collapse" aria-labelledby="heading{{ forloop.index }}" data-bs-parent="#faq">
      <div class="accordion-body">
        {{ site.data.faq.answers[question.a] | markdownify }}
      </div>
    </div>
  </div>
  {% endfor -%}
</div>
