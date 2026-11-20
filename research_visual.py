"""Illustrative research explainer, separate from product and benchmark results.

One story, told in four steps: the memory is full, every example gets a
ProtectScore, the lowest-scoring one gives up its place while the protected
ones stay, and the same thing happens again.

Mechanism sources: memorysafe_v14/buffer_v14.py, _recompute_protect,
update_risk_from_losses, quota-aware retention and stratified weighted replay.
Wording reuses the sentences already on the live page. No measured outcomes
and no score values: the bars are illustrative lengths, never numbers.
"""
from html import escape


STORY = {
    'en': {
        'eyebrow': 'MVI · PROTECTSCORE · REPLAY',
        'title': 'What gets protected?',
        'film': 'Inside a learning memory',
        'play': 'Play animation', 'pause': 'Pause animation', 'replay': 'Replay animation',
        'steps_label': 'Explore the research mechanism',
        'steps': [
            ('Full memory', 'THE LIMIT', 'Memory is full. A new example arrives.',
             'As a model keeps learning, new examples arrive. Only a limited selection of earlier examples can stay in its replay buffer, so one has to leave.'),
            ('The score', 'PROTECTSCORE', 'Every example gets a score.',
             'ProtectScore combines MVI, a vulnerability signal from each example’s training loss, with configured value, rarity, criticality and task-age signals. Here, the rare example and the fragile one score highest.'),
            ('Protection', 'WHAT PROTECTION MEANS', 'The lowest score leaves. The protected stay.',
             'The new example takes the place of the lowest-scoring one in its group. Examples with a high ProtectScore keep their place, and separate quotas set minimum retention for selected groups.'),
            ('Over time', 'AS LEARNING CONTINUES', 'New examples keep coming. The protected are still here.',
             'Ordinary examples come and go. The protected ones stay in memory and return to training alongside new data, where their replay losses refresh MVI for the next decision.'),
        ],
        'incoming': 'New examples', 'memory': 'Memory: six places, always full', 'out': 'Replaced',
        'rare': 'Rare', 'fragile': 'Fragile', 'common': 'Common', 'new': 'New',
        'protected': 'Protected', 'lowest': 'Lowest',
        'legend_shield': 'Protected: keeps its place', 'legend_bar': 'ProtectScore (illustrative)',
        'buffer_notes': ['To let one in, one must leave.',
                         'The rare example and the fragile one score highest.',
                         'F had the lowest score. A and B did not move.',
                         'E left too. A and B are still here.'],
        'audit_title': 'The audit trail',
        'audit_label': 'EXAMPLE ENTRIES',
        'audit_rows': [
            ('2', 'EVICT', 'F → G', 'G outranks F within their group. B’s group retains its floor.', 'lowest_protect_in_group'),
            ('3', 'EVICT', 'E → H', 'H outranks E within their group. A and B keep their places.', 'lowest_protect_in_group'),
        ],
        'audit_note': 'Run records can include the rule, scores, training step and buffer state, so the selection can be inspected.',
        'caption': 'Illustrative training examples. A visual explanation of the research method.',
        'diagram_label': 'A memory with six places is full. Each example has a ProtectScore. When new examples G and H arrive, the lowest-scoring examples F and E are replaced. The rare example B and the fragile example A are protected and keep their places.',
    },
    'pt': {
        'eyebrow': 'MVI · PROTECTSCORE · REPLAY',
        'title': 'O que fica protegido?',
        'film': 'Por dentro da memória que aprende',
        'play': 'Reproduzir animação', 'pause': 'Pausar animação', 'replay': 'Repetir animação',
        'steps_label': 'Explore o mecanismo da pesquisa',
        'steps': [
            ('Memória cheia', 'O LIMITE', 'A memória está cheia. Chega um novo exemplo.',
             'Enquanto o modelo continua aprendendo, novos exemplos chegam. Só uma seleção limitada de exemplos anteriores pode ficar no buffer de replay; por isso, um precisa sair.'),
            ('A pontuação', 'PROTECTSCORE', 'Cada exemplo recebe uma pontuação.',
             'O ProtectScore combina o MVI, um sinal de vulnerabilidade vindo da perda de treinamento de cada exemplo, com sinais configurados de valor, raridade, criticidade e idade da tarefa. Aqui, o exemplo raro e o frágil têm as pontuações mais altas.'),
            ('A proteção', 'O QUE SIGNIFICA PROTEGER', 'A menor pontuação sai. Os protegidos ficam.',
             'O novo exemplo ocupa o lugar do que tem a menor pontuação em seu grupo. Exemplos com ProtectScore alto mantêm seu lugar, e cotas separadas definem mínimos de retenção para grupos selecionados.'),
            ('Com o tempo', 'ENQUANTO O APRENDIZADO CONTINUA', 'Novos exemplos continuam chegando. Os protegidos seguem aqui.',
             'Exemplos comuns entram e saem. Os protegidos ficam na memória e voltam ao treinamento junto de novos dados, onde as perdas no replay atualizam o MVI para a próxima decisão.'),
        ],
        'incoming': 'Novos exemplos', 'memory': 'Memória: seis lugares, sempre cheia', 'out': 'Substituídos',
        'rare': 'Raro', 'fragile': 'Frágil', 'common': 'Comum', 'new': 'Novo',
        'protected': 'Protegido', 'lowest': 'A menor',
        'legend_shield': 'Protegido: mantém seu lugar', 'legend_bar': 'ProtectScore (ilustrativo)',
        'buffer_notes': ['Para um entrar, outro precisa sair.',
                         'O exemplo raro e o frágil têm as pontuações mais altas.',
                         'F tinha a menor pontuação. A e B não saíram do lugar.',
                         'E também saiu. A e B continuam aqui.'],
        'audit_title': 'A trilha de auditoria',
        'audit_label': 'REGISTROS ILUSTRATIVOS',
        'audit_rows': [
            ('2', 'EVICT', 'F → G', 'G supera F dentro do mesmo grupo. O piso do grupo de B é preservado.', 'lowest_protect_in_group'),
            ('3', 'EVICT', 'E → H', 'H supera E dentro do mesmo grupo. A e B mantêm seus lugares.', 'lowest_protect_in_group'),
        ],
        'audit_note': 'Os registros podem incluir regra, pontuações, etapa de treinamento e estado do buffer, permitindo examinar a seleção.',
        'caption': 'Exemplos de treinamento ilustrativos. Uma explicação visual do método de pesquisa.',
        'diagram_label': 'Uma memória com seis lugares está cheia. Cada exemplo tem um ProtectScore. Quando os novos exemplos G e H chegam, os exemplos F e E, de menor pontuação, são substituídos. O exemplo raro B e o exemplo frágil A estão protegidos e mantêm seus lugares.',
    },
}

SHIELD = ('<svg class="cl-shield" viewBox="0 0 12 14" aria-hidden="true">'
          '<path d="M6 .9 11 2.7v4c0 3-2 5.2-5 6.4-3-1.2-5-3.4-5-6.4v-4z"/></svg>')

# Six places. Each holds one example, or an example and the one that replaces it.
# (letter, label key, kind, illustrative bar length); the swap happens at `swap_at`.
SLOTS = [
    (None, [('C', 'common', '', 55)]),
    (None, [('B', 'rare', 'protected', 92)]),
    (2, [('F', 'common', 'lowest', 16), ('G', 'new', '', 50)]),
    (None, [('A', 'fragile', 'protected', 84)]),
    (3, [('E', 'common', 'next', 30), ('H', 'new', '', 44)]),
    (None, [('D', 'common', '', 48)]),
]


def render_research_visual(locale):
    c = STORY[locale]
    e = escape
    panels = ''.join(
        f'<article class="cl-panel" data-cl-panel="{i}" {"hidden" if i else ""}>'
        f'<span class="cl-kicker mono">{e(kicker)}</span><h3>{e(title)}</h3><p>{e(body)}</p></article>'
        for i, (_, kicker, title, body) in enumerate(c['steps'])
    )
    step_buttons = []
    for i, step in enumerate(c['steps']):
        current = ' aria-current="step"' if i == 0 else ''
        step_buttons.append(f'<li><button type="button" data-cl-step="{i}" aria-controls="cl-story"{current}>'
                            f'<span class="cl-step-number">0{i + 1}</span><span>{e(step[0])}</span>'
                            '<i aria-hidden="true"></i></button></li>')
    steps = ''.join(step_buttons)
    buffer_notes = ''.join(f'<span data-cl-buffer-note="{i}" {"hidden" if i else ""}>{e(t)}</span>'
                           for i, t in enumerate(c['buffer_notes']))
    audit_rows = ''.join(f'<li data-cl-audit-from="{at}" data-reason="{e(code)}"><span class="cl-audit-action">{e(action)}</span>'
                         f'<strong>{e(subject)}</strong><span class="cl-audit-reason">{e(reason)}'
                         '</span></li>'
                         for at, action, subject, reason, code in c['audit_rows'])

    def card(letter, label, kind, score, stage):
        tag = ''
        if kind == 'protected':
            tag = f'<span class="cl-tag">{SHIELD}{e(c["protected"])}</span>'
        elif kind == 'lowest':
            tag = f'<span class="cl-tag">{e(c["lowest"])}</span>'
        cls = 'cl-card' + (f' cl-{kind}' if kind else '') + (' is-off' if 'from' in stage else '')
        return (f'<div class="{cls}" style="--score:{score}%" data-cl-letter="{letter}" {stage}>'
                f'<span class="cl-sample-glyph" aria-hidden="true">{letter}</span>'
                f'<span class="cl-sample-label">{e(c[label])}</span>'
                f'<span class="cl-score" aria-hidden="true"><i></i></span>{tag}</div>')

    slots = []
    for swap_at, residents in SLOTS:
        cards = ''
        for n, (letter, label, kind, score) in enumerate(residents):
            stage = '' if swap_at is None else (f'data-cl-from="{swap_at}"' if n else f'data-cl-until="{swap_at}"')
            cards += card(letter, label, kind, score, stage)
        swap = '' if swap_at is None else f' data-cl-swap="{swap_at}"'
        slots.append(f'<div class="cl-slot"{swap}>{cards}</div>')
    queue = ''.join(f'<i class="cl-chip{" is-off" if "from" in stage else ""}" {stage}>{letter}</i>'
                    for letter, stage in [('G', 'data-cl-until="2"'), ('H', 'data-cl-until="3"'), ('J', ''),
                                          ('K', 'data-cl-from="2"'), ('L', 'data-cl-from="3"')])
    tray = ''.join(f'<span class="cl-rest"><i class="cl-chip is-off" data-cl-from="{at}">{letter}</i></span>'
                   for letter, at in [('F', 2), ('E', 3)])
    return f'''<section class="cl-explainer" data-cl-explainer data-step="0" data-playing="false" data-flight="false" aria-labelledby="cl-title">
<div class="cl-heading"><div class="eyebrow">{e(c['eyebrow'])}</div><h2 id="cl-title">{e(c['title'])}</h2></div>
<figure class="cl-film">
<div class="cl-film-top"><span class="mono">{e(c['film'])}</span><button type="button" class="cl-play" data-cl-play data-play="{e(c['play'])}" data-pause="{e(c['pause'])}" data-replay="{e(c['replay'])}" hidden><span data-cl-play-icon aria-hidden="true">▶</span> <span data-cl-play-label>{e(c['play'])}</span></button></div>
<ol class="cl-steps" aria-label="{e(c['steps_label'])}">{steps}</ol>
<div class="cl-story" id="cl-story" aria-live="polite">{panels}</div>
<div class="cl-diagram" role="img" aria-label="{e(c['diagram_label'])}">
<div class="cl-motion-layer" aria-hidden="true"></div>
<div class="cl-stream"><span class="cl-node-label">{e(c['incoming'])}</span><div class="cl-queue" aria-hidden="true"><div class="cl-queue-track">{queue}</div></div></div>
<div class="cl-connector cl-incoming" aria-hidden="true"><i></i></div>
<div class="cl-buffer"><span class="cl-node-label">{e(c['memory'])}</span><div class="cl-slots">{''.join(slots)}</div><div class="cl-legend"><span>{SHIELD}{e(c['legend_shield'])}</span><span><i class="cl-legend-bar" aria-hidden="true"></i>{e(c['legend_bar'])}</span></div><div class="cl-buffer-note">{buffer_notes}</div></div>
<div class="cl-connector cl-leaving" aria-hidden="true"><i></i></div>
<div class="cl-out"><span class="cl-node-label">{e(c['out'])}</span><div class="cl-tray" aria-hidden="true">{tray}</div></div>
</div>
<section class="cl-audit" aria-labelledby="cl-audit-title"><div class="cl-audit-heading"><h3 id="cl-audit-title">{e(c['audit_title'])}</h3><span class="mono">{e(c['audit_label'])}</span></div><ol>{audit_rows}</ol><p>{e(c['audit_note'])}</p></section>
<figcaption>{e(c['caption'])}</figcaption>
</figure>
<noscript><ol class="cl-static">{''.join(f'<li><strong>{e(s[0])}.</strong> {e(s[3])}</li>' for s in c['steps'])}</ol></noscript>
</section>'''
