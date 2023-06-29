const rallax = window.rallax

// Check user's motion preference
const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)')
const prefersReducedMotion = mediaQuery.matches

if (!prefersReducedMotion) {
  for (const image of document.getElementsByClassName('motion-safe:rallax')) {
    rallax(image)
  }
}
