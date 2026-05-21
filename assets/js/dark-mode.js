(function () {
  const storageKey = 'theme'
  const root = document.documentElement
  const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)')

  const renderIcon = (theme) => {
    const icon = document.getElementById('themeIcon')
    if (!icon) return
    icon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill'
  }

  function syncThemeToggleState(theme) {
    const btn = document.getElementById('themeToggle')
    if (!btn) return

    const isDark = theme === 'dark'
    btn.setAttribute('aria-pressed', isDark ? 'true' : 'false');
    btn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
  }

  const applyTheme = (theme, persist) => {
    root.setAttribute('data-bs-theme', theme)
    if (persist) {
      localStorage.setItem(storageKey, theme)
    }
    renderIcon(theme)
    syncThemeToggleState(theme)
  }

  // Apply immediately to prevent FOUC - runs before DOM is ready.
  const storedTheme = localStorage.getItem(storageKey)
  const initialTheme = storedTheme || root.getAttribute('data-bs-theme') || (mediaQuery.matches ? 'dark' : 'light')
  applyTheme(initialTheme, false)

  // Bind interactivity once the DOM is available.
  const init = () => {
    // Re-render icon now that the element exists.
    renderIcon(root.getAttribute('data-bs-theme') || 'light')

    const button = document.getElementById('themeToggle')
    button?.addEventListener('click', () => {
      const next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark'
      applyTheme(next, true)
    })

    mediaQuery.addEventListener('change', (event) => {
      if (localStorage.getItem(storageKey)) return
      applyTheme(event.matches ? 'dark' : 'light', false)
    })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
