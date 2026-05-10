const TARGET_LEN = 56;

function formatCite(href, cite) {
  let url;
  try {
    url = new URL(href);
  } catch {
    return;
  }

  const origin = url.origin;
  const pathParts = url.pathname.split('/').filter(Boolean);

  cite.innerHTML = '';
  cite.appendChild(document.createTextNode(origin));

  if (pathParts.length === 0) return;

  const SEP = ' › ';
  const pathStr = pathParts.join(SEP);
  const full = origin + SEP + pathStr;

  let spanText;
  if (full.length <= TARGET_LEN) {
    spanText = SEP + pathStr;
  } else {
    const ellipsis = '...';
    const available = TARGET_LEN - origin.length - SEP.length - ellipsis.length;
    spanText = SEP + pathStr.substring(0, Math.max(0, available)) + ellipsis;
  }

  const span = document.createElement('span');
  span.className = 'ylgVCe ob9lvb';
  span.setAttribute('role', 'text');
  span.textContent = spanText;
  cite.appendChild(span);
}

function processLinks() {
  document.querySelectorAll('a.zReHs').forEach(link => {
    const cite = link.querySelector('cite.tjvcx.GvPZzd.cHaqb');
    if (cite && !cite.dataset.chromeOssProcessed) {
      cite.dataset.chromeOssProcessed = '1';
      formatCite(link.href, cite);
    }
  });
}

processLinks();

new MutationObserver(processLinks).observe(document.documentElement, {
  childList: true,
  subtree: true,
});
