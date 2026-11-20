/* Illustrative sequence only. No model execution, scores, tracking or network calls.
   Every step is a plain state (data-step plus .is-off); the flying cards only decorate
   the move from one state to the next, so the picture is right without them. */
(() => {
  const root = document.querySelector('[data-cl-explainer]');
  if (!root) return;
  const panels = [...root.querySelectorAll('[data-cl-panel]')];
  const steps = [...root.querySelectorAll('[data-cl-step]')];
  const control = root.querySelector('[data-cl-play]');
  const story = root.querySelector('.cl-story');
  const diagram = root.querySelector('.cl-diagram');
  const layer = root.querySelector('.cl-motion-layer');
  const staged = [...root.querySelectorAll('[data-cl-from], [data-cl-until]')];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const last = panels.length - 1;
  /* Reduced motion: open on the finished picture, where protected and replaced are both visible. */
  let step = motion.matches ? last : 0, playing = !motion.matches, finished = motion.matches;
  let visible = false, timer = null, renderedStep = -1;
  const flights = new Set();
  const duration = 6000;
  function clearTimer() { clearTimeout(timer); timer = null; }
  function clearFlights() {
    flights.forEach(({ animation, node }) => { animation.cancel(); node.remove(); });
    flights.clear();
  }
  function point(element) {
    const frame = diagram.getBoundingClientRect(), box = element.getBoundingClientRect();
    return { x: box.left + box.width / 2 - frame.left, y: box.top + box.height / 2 - frame.top };
  }
  function fly(text, from, to, delay, kind) {
    const node = document.createElement('span');
    node.className = 'cl-flying-card' + (kind ? ' cl-flight-' + kind : '');
    node.textContent = text; layer.append(node);
    const w = 30, h = 38;
    const stacked = matchMedia('(max-width: 600px)').matches;
    const middle = { x: (from.x + to.x) / 2, y: (from.y + to.y) / 2 };
    if (stacked) middle.x = Math.min(diagram.clientWidth - w / 2, middle.x + 26);
    else middle.y -= 30;
    const transform = (p, rotate, scale) => `translate(${p.x - w / 2}px, ${p.y - h / 2}px) rotate(${rotate}deg) scale(${scale})`;
    const animation = node.animate([
      { transform: transform(from, 0, 1.15), opacity: 0, offset: 0 },
      { opacity: 1, offset: .12 },
      { transform: transform(middle, kind ? 9 : -5, 1.1), opacity: 1, offset: .5 },
      { opacity: 1, offset: .86 },
      { transform: transform(to, 0, 1), opacity: 0, offset: 1 },
    ], { duration: 1500, delay, easing: 'cubic-bezier(.3,0,.2,1)', fill: 'both' });
    const item = { animation, node }; flights.add(item);
    animation.onfinish = () => { node.remove(); flights.delete(item); };
  }
  /* Measured before the state changes: who leaves which place, and who takes it. */
  function plan(next) {
    const place = root.querySelector(`[data-cl-swap="${next}"]`);
    const arriving = root.querySelector(`.cl-queue [data-cl-until="${next}"]`);
    const resting = root.querySelector(`.cl-tray [data-cl-from="${next}"]`);
    if (!place || !arriving || !resting || !layer || typeof layer.animate !== 'function') return [];
    const leaving = place.querySelector('[data-cl-until]'), entering = place.querySelector('[data-cl-from]');
    return [
      [leaving.dataset.clLetter, point(place), point(resting), 0, 'outgoing'],
      [entering.dataset.clLetter, point(arriving), point(place), 450, ''],
    ];
  }
  function schedule() {
    clearTimer();
    if (!playing || !visible || document.hidden) return;
    timer = setTimeout(() => {
      step = (step + 1) % panels.length; finished = false; render();
    }, duration);
  }
  function render() {
    const changed = renderedStep !== step;
    const live = visible && !document.hidden && !motion.matches;
    const moves = changed && live && renderedStep === step - 1 ? plan(step) : [];
    if (changed || !live) clearFlights();
    if (changed) root.dataset.flight = String(moves.length > 0);
    root.dataset.step = String(step);
    root.dataset.playing = String(playing && visible && !document.hidden);
    story.setAttribute('aria-live', playing ? 'off' : 'polite');
    panels.forEach((panel, i) => { panel.hidden = i !== step; });
    staged.forEach(node => {
      const from = Number(node.dataset.clFrom || 0), until = Number(node.dataset.clUntil || 99);
      node.classList.toggle('is-off', step < from || step >= until);
    });
    root.querySelectorAll('[data-cl-buffer-note]').forEach(node => {
      node.hidden = Number(node.dataset.clBufferNote) !== step;
    });
    root.querySelectorAll('[data-cl-audit-from]').forEach(node => {
      node.classList.toggle('is-revealed', Number(node.dataset.clAuditFrom) <= step);
    });
    steps.forEach((button, i) => {
      if (i === step) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    control.querySelector('[data-cl-play-label]').textContent = playing ? control.dataset.pause :
      (finished ? control.dataset.replay : control.dataset.play);
    control.querySelector('[data-cl-play-icon]').textContent = playing ? 'Ⅱ' : '▶';
    moves.forEach(move => fly(...move));
    renderedStep = step;
    schedule();
  }
  control.hidden = false;
  control.addEventListener('click', () => {
    if (finished) { step = 0; finished = false; playing = true; }
    else playing = !playing;
    render();
  });
  steps.forEach((button, i) => button.addEventListener('click', () => {
    step = i; playing = false; finished = i === last; render();
  }));
  document.addEventListener('visibilitychange', render);
  window.addEventListener('resize', () => { clearFlights(); render(); });
  motion.addEventListener('change', event => { if (event.matches) { playing = false; render(); } });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting && entries[0].intersectionRatio >= .35;
      render();
    }, { threshold: .35 });
    observer.observe(diagram);
  } else visible = true;
  render();
})();
