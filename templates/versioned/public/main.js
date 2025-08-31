// Works on GitHub "project" pages (username.github.io/<repo>/...)
export default {
  start: () => {
    const mount = () => {
      const headerNav = document.querySelector('header nav, header .navbar, header');
      if (!headerNav || document.getElementById('bt-version-switcher')) return;

      const parts = window.location.pathname.split('/').filter(Boolean);
      const base = parts.length ? `/${parts[0]}/` : '/'; // "/<repo>/" or "/"
      const currentTop = parts.length > 1 ? parts[1] : ''; // "1.0", "1.1", "latest", ...

      const holder = document.createElement('div');
      holder.id = 'bt-version-switcher';
      holder.style.marginLeft = '0.75rem';

      const select = document.createElement('select');
      select.ariaLabel = 'Documentation version';
      select.className = 'bt-version-select';
      holder.appendChild(select);
      headerNav.appendChild(holder);

      fetch(`${base}versions.json`)
        .then(r => r.ok ? r.json() : null)
        .then(data => {
          if (!data || !Array.isArray(data.versions)) return;
          data.versions.forEach(v => {
            const opt = document.createElement('option');
            opt.value = `${base}${v.path}`;
            opt.textContent = v.label;
            const top = v.path.replace(/\/$/, '');
            if (top === currentTop) opt.selected = true;
            select.appendChild(opt);
          });
          select.addEventListener('change', () => location.href = select.value);
        })
        .catch(()=>{});
    };

    mount();
    window.addEventListener('docfx:nav-ready', mount);
  },
};
