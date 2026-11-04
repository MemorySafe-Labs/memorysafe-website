/* Illustrative sequence only. No model execution, scores, tracking or network calls. */
(() => {
  const root = document.querySelector('[data-cl-explainer]');
  if (!root) return;
  const panels = [...root.querySelectorAll('[data-cl-panel]')];
  const steps = [...root.querySelectorAll('[data-cl-step]')];
  const control = root.querySelector('[data-cl-play]');
  const story = root.querySelector('.cl-story');
  const diagram = root.querySelector('.cl-diagram');
  const layer = root.querySelector('.cl-motion-layer');
  const samples = [...root.querySelectorAll('.cl-sample')];
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  let step = 0, playing = !motion.matches, visible = false, timer = null, finished = false;
  let renderedStep = -1, motionTimer = null, motionActive = false;
  const flights = new Set();
  const shuffles = new Set();
  const duration = 6500;
  function clearTimer() { clearTimeout(timer); timer = null; }
  function clearFlights() {
    clearTimeout(motionTimer); motionTimer = null;
    flights.forEach(({ animation, node }) => { animation.cancel(); node.remove(); });
    flights.clear();
  }
  function point(element) {
    const frame = diagram.getBoundingClientRect(), box = element.getBoundingClientRect();
    return { x: box.left + box.width / 2 - frame.left, y: box.top + box.height / 2 - frame.top };
  }
  function fly(text, from, to, delay = 0, kind = '') {
    if (!layer || typeof layer.animate !== 'function') return;
    const node = document.createElement('span');
    node.className = 'cl-flying-card' + (kind ? ' cl-flight-' + kind : '');
    node.textContent = text; layer.append(node);
    const tag = kind === 'signal', w = tag ? 38 : 28, h = tag ? 22 : 34;
    const mobile = matchMedia('(max-width: 600px)').matches;
    const middle = { x: (from.x + to.x) / 2, y: (from.y + to.y) / 2 };
    if (mobile) middle.x = Math.min(diagram.clientWidth - w / 2, middle.x + 28);
    else middle.y -= 28;
    const transform = (p, rotate, scale) => `translate(${p.x - w / 2}px, ${p.y - h / 2}px) rotate(${rotate}deg) scale(${scale})`;
    const animation = node.animate([
      { transform: transform(from, -9, .9), opacity: 0, offset: 0 },
      { opacity: 1, offset: .13 },
      { transform: transform(middle, 4, 1.08), opacity: 1, offset: .52 },
      { opacity: 1, offset: .84 },
      { transform: transform(to, 0, .85), opacity: 0, offset: 1 },
    ], { duration: 1550, delay, easing: 'cubic-bezier(.3,0,.2,1)', fill: 'both' });
    const item = { animation, node }; flights.add(item);
    animation.onfinish = () => { node.remove(); flights.delete(item); };
  }
  function launchScene() {
    const incoming = root.querySelector('.cl-stream-pieces i');
    const buffer = root.querySelector('.cl-slots');
    const model = root.querySelector('.cl-model-mark');
    const fragile = root.querySelector('.cl-fragile');
    const rare = root.querySelector('.cl-rare');
    const replacement = root.querySelector('.cl-replaceable');
    if (step === 0) {
      const frame = diagram.getBoundingClientRect(), box = buffer.getBoundingClientRect();
      const destination = matchMedia('(max-width: 600px)').matches ?
        { x: point(buffer).x, y: box.top - frame.top - 10 } :
        { x: box.left - frame.left - 8, y: point(buffer).y };
      fly('G', point(incoming), destination);
      fly('H', point(root.querySelector('.cl-stream-pieces i:nth-child(2)')), destination, 900);
    } else if (step === 1) {
      fly('MVI', point(model), point(fragile), 100, 'signal');
    } else if (step === 2) {
      const origin = point(replacement);
      fly('F', origin, { x: origin.x + 35, y: origin.y + 30 }, 0, 'outgoing');
      fly('G', point(incoming), origin, 600);
    } else {
      fly('A', point(fragile), point(model));
      fly('B', point(rare), point(model), 650);
      fly('J', point(root.querySelector('.cl-stream-pieces i:nth-child(3)')), point(model), 1350);
      fly('MVI', point(model), point(fragile), 2200, 'signal');
    }
  }
  function queueMotion() {
    clearTimeout(motionTimer); motionTimer = null;
    if (!motionActive || step === 2) return;
    motionTimer = setTimeout(() => { if (motionActive) { launchScene(); queueMotion(); } }, step === 3 ? 4200 : 2900);
  }
  function syncMotion(changed) {
    if (changed) clearFlights();
    const active = playing && visible && !document.hidden && !motion.matches;
    const wasActive = motionActive;
    motionActive = active;
    if (!active) {
      clearTimeout(motionTimer); motionTimer = null;
      flights.forEach(({ animation }) => animation.pause());
      if (!visible || document.hidden || motion.matches) {
        shuffles.forEach(animation => animation.cancel()); shuffles.clear();
      }
    } else if (changed || !wasActive) {
      flights.forEach(({ animation }) => animation.play());
      if (!flights.size) launchScene();
      queueMotion();
    }
  }
  function shuffle(previous) {
    if (motion.matches || !visible || typeof diagram.animate !== 'function') return;
    shuffles.forEach(animation => animation.cancel()); shuffles.clear();
    samples.forEach((sample, i) => {
      const current = sample.getBoundingClientRect();
      const dx = previous[i].left - current.left, dy = previous[i].top - current.top;
      if (Math.abs(dx) + Math.abs(dy) < 2) return;
      const animation = sample.animate([
        { transform: `translate(${dx}px, ${dy}px) scale(.96)` },
        { transform: 'translate(0, 0) scale(1)' },
      ], { duration: 1000, easing: 'cubic-bezier(.2,.7,.2,1)' });
      shuffles.add(animation); animation.onfinish = () => shuffles.delete(animation);
    });
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
    const previous = changed && renderedStep !== -1 ? samples.map(sample => sample.getBoundingClientRect()) : null;
    root.dataset.step = String(step);
    root.dataset.playing = String(playing && visible && !document.hidden);
    story.setAttribute('aria-live', playing ? 'off' : 'polite');
    panels.forEach((panel, i) => { panel.hidden = i !== step; });
    root.querySelectorAll('[data-cl-buffer-note]').forEach(node => {
      node.hidden = Number(node.dataset.clBufferNote) !== step;
    });
    root.querySelectorAll('[data-cl-model-note]').forEach(node => {
      node.hidden = Number(node.dataset.clModelNote) !== step;
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
    if (previous) shuffle(previous);
    syncMotion(changed);
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
    step = i; playing = false; finished = i === panels.length - 1; render();
  }));
  document.addEventListener('visibilitychange', render);
  window.addEventListener('resize', () => { clearFlights(); motionActive = false; render(); });
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
