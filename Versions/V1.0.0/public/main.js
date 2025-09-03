// templates/versioned/public/main.js
export default {
  // optional global config for modern theme:
  // defaultTheme: 'system',

  start: () => {
    const mount = () => {
      // Find a stable place in the modern header to mount our switcher.
      // modern template renders a <header> with a nav; we append to its end.
      const headerNav = document.querySelector('header nav, header .navbar, header');
      if (!headerNav) return;

      // Avoid duplicates on navigation updates
      if (document.getElementById('bt-version-switcher')) return;

      const holder = document.createElement('div');
      holder.id = 'bt-version-switcher';
      holder.style.marginLeft = '0.75rem';

      const label = document.createElement('label');
      label.className = 'visually-hidden';
      label.textContent = 'Docs version';

      const select = document.createElement('select');
      select.ariaLabel = 'Documentation version';
      select.className = 'bt-version-select';

      holder.appendChild(label);
      holder.appendChild(select);
      headerNav.appendChild(holder);

      // Load versions.json from site root (gh-pages root)
      fetch(new URL('/versions.json', window.location.origin))
        .then(r => (r.ok ? r.json() : null))
        .then(data => {
          if (!data || !Array.isArray(data.versions)) return;

          // Current top-level folder: "1.0", "1.1", "latest", etc.
          const currentTop = (window.location.pathname.split('/').filter(Boolean)[0] || '');

          data.versions.forEach(v => {
            const opt = document.createElement('option');
            opt.value = '/' + v.path; // e.g. "1.1/"
            opt.textContent = v.label;
            const top = v.path.replace(/\/$/, '');
            if (top === currentTop) opt.selected = true;
            select.appendChild(opt);
          });

          select.addEventListener('change', () => {
            window.location.href = select.value;
          });
        })
        .catch(() => {});
    };

    // Mount immediately and also after client-side nav (modern does soft reloads)
    mount();
    // Re-run on history changes if modern swaps content
    window.addEventListener('docfx:nav-ready', mount);
  },
};
