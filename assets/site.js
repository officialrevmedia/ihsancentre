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
  // Success messages shown in place of each form once it has been sent.
  var SUCCESS = {
    'vol-form': ['Thank you for signing up!', 'JazakAllahu khayran for offering your time. We have your details and will be in touch soon about how you can help. High school students: let us know if you need your hours signed off.'],
    'contact-form': ['Message sent', 'Thank you for reaching out. We have received your message and will reply by email as soon as we can.'],
    'newsletter-form': ['You are subscribed', 'Thank you for joining our mailing list. Watch your inbox for news on programs, events and gatherings at the Centre.'],
    'sponsor': ['Thank you for your interest', 'We have received your sponsorship enquiry and will email you the sponsorship package soon. JazakAllahu khayran for supporting the Centre.'],
    'pledge': ['Thank you for your pledge!', 'May Allah reward your generosity. Drop off winter essentials on Sundays, November 1 to December 6, 10 AM to 1 PM, at 487 Shaver Road, Ancaster.'],
    'gn-form': ['You are on the list!', 'Thanks for your RSVP. We will send you upcoming Guys Night dates by email. See you there, brother.'],
    'enquire': ['Enquiry received', 'Thank you for your interest in renting the Centre. We will get back to you about availability and pricing soon.'],
    'fn-form': ['Your family is on the list!', 'Thank you for your interest in Family Night. We will let you know as soon as the first evening is scheduled.'],
    'hifz-form': ['You are on the interest list', 'Thank you for your interest in the Hifz Program. We will share updates with you as the 2027 program takes shape.'],
    'mh-form': ['You are signed up for reminders', 'We will email you before each Markers of Health session. You can unsubscribe at any time.'],
    'join': ['Welcome to the Book Club!', 'You are signed up. Taking you to the next step now so you can join our WhatsApp group...']
  };
  var DEFAULT_SUCCESS = ['Thank you!', 'Your submission has been received. We will be in touch soon.'];

  function showSuccess(form) {
    var msg = SUCCESS[form.id] || DEFAULT_SUCCESS;
    var box = document.createElement('div');
    box.className = 'form form-success';
    box.setAttribute('role', 'status');
    box.setAttribute('tabindex', '-1');
    box.innerHTML = '<div class="fs-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="28" height="28"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>' +
      '<h3></h3><p></p>';
    box.querySelector('h3').textContent = msg[0];
    box.querySelector('p').textContent = msg[1];
    if (form.id !== 'join') {
      var again = document.createElement('button');
      again.type = 'button';
      again.className = 'btn btn-sm btn-outline';
      again.textContent = 'Send another response';
      again.addEventListener('click', function () {
        form.reset();
        var btn = form.querySelector('button[type="submit"]');
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label || btn.textContent; }
        var s = form.querySelector('.form-status'); if (s) s.remove();
        box.parentNode.replaceChild(form, box);
        var first = form.querySelector('input:not([type="hidden"]):not(.hp), select, textarea');
        if (first) first.focus();
      });
      box.appendChild(again);
    }
    form.parentNode.replaceChild(box, form);
    box.focus({ preventScroll: true });
    box.scrollIntoView({ behavior: 'smooth', block: 'center' });
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
      // Shown only if sending really fails. No automatic mail app pop-up: that looked like "nothing happened".
      var fallback = function () {
        status(form, 'Sorry, we could not send your details just now. Please try again in a minute, or ' +
          '<a href="' + mail + '">send them by email instead</a> (your answers are filled in for you) to ' +
          '<a href="mailto:' + TO + '">' + TO + '</a>.');
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.label; }
      };
      if (btn) { btn.dataset.label = btn.textContent; btn.disabled = true; btn.textContent = 'Sending...'; }
      // FormSubmit can take 20 to 30 seconds to reply, so tell people to wait instead of leaving them guessing.
      status(form, 'Sending your details. This can take up to 30 seconds, so please keep this page open.');
      var done = false;
      var slow = setTimeout(function () { if (!done && btn) btn.textContent = 'Still sending...'; }, 12000);
      var timer = setTimeout(function () { if (!done) { done = true; clearTimeout(slow); fallback(); } }, 90000);
      fetch('https://formsubmit.co/ajax/' + TO, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data)
      }).then(function (r) { return r.json(); }).then(function (j) {
        if (done) return; done = true; clearTimeout(timer); clearTimeout(slow);
        if (j && (j.success === true || j.success === 'true')) {
          showSuccess(form);
          // Book Club continues to its welcome page (WhatsApp link) after the message shows.
          if (form.id === 'join') setTimeout(function () { window.location.href = next; }, 2500);
        } else { fallback(); }
      }).catch(function () { if (done) return; done = true; clearTimeout(timer); clearTimeout(slow); fallback(); });
    });
  });
})();
