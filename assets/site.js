(function () {
  // Mobile menu
  var t = document.getElementById('navToggle'), l = document.getElementById('navLinks');
  if (t && l) t.addEventListener('click', function () {
    var o = l.classList.toggle('open');
    t.setAttribute('aria-expanded', o ? 'true' : 'false');
    t.setAttribute('aria-label', o ? 'Close menu' : 'Open menu');
  });

  // Forms: send through FormSubmit; if that cannot deliver, open a pre-filled email instead.
  var TO = 'info@ihsancentre.org';
  function labelFor(form, el) {
    var lb = el.id && form.querySelector('label[for="' + el.id + '"]');
    return lb ? lb.textContent.replace('*', '').trim() : el.name;
  }
  function mailto(form, subject) {
    var lines = [];
    form.querySelectorAll('input, select, textarea').forEach(function (el) {
      if (!el.name || el.name.charAt(0) === '_' || el.type === 'hidden' || !el.value) return;
      lines.push(labelFor(form, el) + ': ' + el.value);
    });
    return 'mailto:' + TO + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n') + '\n');
  }
  function status(form, html) {
    var s = form.querySelector('.form-status');
    if (!s) { s = document.createElement('div'); s.className = 'form-status'; s.setAttribute('role', 'status'); form.appendChild(s); }
    s.innerHTML = html;
  }
  document.querySelectorAll('form.form').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.reportValidity()) return;
      var hp = form.querySelector('[name="_honey"]');
      if (hp && hp.value) return;
      var subject = (form.querySelector('[name="_subject"]') || {}).value || 'Website message';
      var next = (form.querySelector('[name="_next"]') || {}).value || '/thank-you/';
      var btn = form.querySelector('button[type="submit"]');
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== '_next' && k !== '_honey') data[k] = v; });
      var mail = mailto(form, subject);
      var fallback = function () {
        status(form, 'We have opened an email with your details filled in. Please press <strong>Send</strong> in your email app. ' +
          'If nothing opened, <a href="' + mail + '">tap here</a> or email <a href="mailto:' + TO + '">' + TO + '</a>.');
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
        window.location.href = mail;
      };
      if (btn) { btn.dataset.label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending...'; }
      var done = false;
      var timer = setTimeout(function () { if (!done) { done = true; fallback(); } }, 9000);
      fetch('https://formsubmit.co/ajax/' + TO, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data)
      }).then(function (r) { return r.json(); }).then(function (j) {
        if (done) return; done = true; clearTimeout(timer);
        if (j && (j.success === true || j.success === 'true')) { window.location.href = next; } else { fallback(); }
      }).catch(function () { if (done) return; done = true; clearTimeout(timer); fallback(); });
    });
  });
})();
