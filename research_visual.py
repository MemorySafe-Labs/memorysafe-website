"""Illustrative research explainer, separate from product and benchmark results.

Mechanism sources: memorysafe_v14/buffer_v14.py, _recompute_protect,
update_risk_from_losses, quota-aware retention and stratified weighted replay.
Copy checked against CLAIMS_LOCK.md. No measured outcomes or score values.
"""
from html import escape


STORY = {
    'en': {
        'eyebrow': 'MVI · PROTECTSCORE · REPLAY',
        'title': 'What gets another chance?',
        'film': 'Inside a learning memory',
        'play': 'Play animation', 'pause': 'Pause animation', 'replay': 'Replay animation',
        'steps_label': 'Explore the research mechanism',
        'steps': [
            ('The limit', 'THE CONSTRAINT', 'New data. The same memory budget.',
             'As a model keeps learning, new examples arrive. Only a limited selection of earlier examples can stay in its replay buffer.'),
            ('MVI', 'MEMORY VULNERABILITY INDEX', 'Notice what may be fragile.',
             'MVI tracks a smoothed signal from each example’s training loss. It is a signal of vulnerability that helps identify examples needing another look.'),
            ('ProtectScore', 'RETENTION + REPLAY PRIORITY', 'Give the selection a reason.',
             'ProtectScore combines MVI with configured value, rarity, criticality and task-age signals. It guides retention and replay; separate quotas set minimum retention for selected groups.'),
            ('The impact', 'THE INTENDED EFFECT', 'Change what gets practiced.',
             'Within the same memory limit, selected earlier examples return to training alongside new data. Their replay losses refresh MVI, feeding the next decision.'),
        ],
        'incoming': 'New examples', 'budget': 'Fixed memory budget', 'model': 'Learning model',
        'earlier': 'Earlier', 'rare': 'Rare', 'recent': 'Recent', 'new': 'New',
        'floor': 'Separate retention floor', 'mvi_flag': 'MVI',
        'buffer_notes': ['Earlier knowledge, limited space', 'Vulnerability becomes visible',
                         'Priority + retention constraints', 'Selected examples get another look'],
        'model_notes': ['Learning continues', 'Learning continues', 'Learning continues', 'New data + replay'],
        'feedback': 'Replay loss refreshes MVI',
        'audit_title': 'The audit trail',
        'audit_label': 'EXAMPLE ENTRIES',
        'audit_rows': [
            ('0', 'ADMIT', 'A stays', 'A free slot was available.', 'free_capacity'),
            ('2', 'REJECT', 'H stays out', 'Its ProtectScore is below the eligible resident’s.', 'protect_below_victim'),
            ('2', 'EVICT', 'F → G', 'G outranks F within their group. B’s group retains its floor.', 'lowest_protect_in_group'),
        ],
        'audit_note': 'Run records can include the rule, scores, training step and buffer state, so the selection can be inspected.',
        'caption': 'Illustrative training examples. A visual explanation of the research method.',
        'diagram_label': 'New examples enter a bounded replay buffer. MVI informs ProtectScore. Retention constraints and scores guide which examples return to model training.',
    },
    'pt': {
        'eyebrow': 'MVI · PROTECTSCORE · REPLAY',
        'title': 'O que merece outra chance?',
        'film': 'Por dentro da memória que aprende',
        'play': 'Reproduzir animação', 'pause': 'Pausar animação', 'replay': 'Repetir animação',
        'steps_label': 'Explore o mecanismo da pesquisa',
        'steps': [
            ('O limite', 'A RESTRIÇÃO', 'Novos dados. O mesmo limite de memória.',
             'Enquanto o modelo continua aprendendo, novos exemplos chegam. Só uma seleção limitada de exemplos anteriores pode ficar no buffer de replay.'),
            ('MVI', 'ÍNDICE DE VULNERABILIDADE DA MEMÓRIA', 'Perceber o que pode estar frágil.',
             'O MVI acompanha um sinal suavizado da perda de treinamento de cada exemplo. Esse sinal de vulnerabilidade ajuda a identificar exemplos que merecem ser revisitados.'),
            ('ProtectScore', 'PRIORIDADE DE RETENÇÃO + REPLAY', 'Dar um motivo à seleção.',
             'O ProtectScore combina MVI com sinais configurados de valor, raridade, criticidade e idade da tarefa. Ele orienta retenção e replay; cotas separadas definem mínimos de retenção para grupos selecionados.'),
            ('O impacto', 'O EFEITO PRETENDIDO', 'Mudar o que recebe prática.',
             'Com o mesmo limite de memória, exemplos anteriores selecionados voltam ao treinamento junto de novos dados. As perdas no replay atualizam o MVI e alimentam a próxima decisão.'),
        ],
        'incoming': 'Novos exemplos', 'budget': 'Limite fixo de memória', 'model': 'Modelo em aprendizado',
        'earlier': 'Anterior', 'rare': 'Raro', 'recent': 'Recente', 'new': 'Novo',
        'floor': 'Piso de retenção separado', 'mvi_flag': 'MVI',
        'buffer_notes': ['Conhecimento anterior, espaço limitado', 'A vulnerabilidade fica visível',
                         'Prioridade + regras de retenção', 'Exemplos selecionados são revisitados'],
        'model_notes': ['O aprendizado continua', 'O aprendizado continua', 'O aprendizado continua', 'Novos dados + replay'],
        'feedback': 'A perda no replay atualiza o MVI',
        'audit_title': 'A trilha de auditoria',
        'audit_label': 'REGISTROS ILUSTRATIVOS',
        'audit_rows': [
            ('0', 'ADMIT', 'A fica', 'Havia uma vaga disponível.', 'free_capacity'),
            ('2', 'REJECT', 'H fica de fora', 'Seu ProtectScore é inferior ao do candidato elegível à substituição.', 'protect_below_victim'),
            ('2', 'EVICT', 'F → G', 'G supera F dentro do mesmo grupo. O piso do grupo de B é preservado.', 'lowest_protect_in_group'),
        ],
        'audit_note': 'Os registros podem incluir regra, pontuações, etapa de treinamento e estado do buffer, permitindo examinar a seleção.',
        'caption': 'Exemplos de treinamento ilustrativos. Uma explicação visual do método de pesquisa.',
        'diagram_label': 'Novos exemplos chegam a um buffer de replay limitado. O MVI informa o ProtectScore. Regras de retenção e pontuações orientam quais exemplos voltam ao treinamento do modelo.',
    },
}


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
    model_notes = ''.join(f'<span data-cl-model-note="{i}" {"hidden" if i else ""}>{e(t)}</span>'
                          for i, t in enumerate(c['model_notes']))
    audit_rows = ''.join(f'<li data-cl-audit-from="{at}" data-reason="{e(code)}"><span class="cl-audit-action">{e(action)}</span>'
                         f'<strong>{e(subject)}</strong><span class="cl-audit-reason">{e(reason)}'
                         '</span></li>'
                         for at, action, subject, reason, code in c['audit_rows'])
    samples = []
    for letter, label, kind in [('A', c['earlier'], 'fragile'), ('B', c['rare'], 'rare'),
                                ('C', c['recent'], 'ordinary'), ('D', c['earlier'], 'ordinary'),
                                ('E', c['recent'], 'ordinary'), ('F', c['recent'], 'replaceable')]:
        extra = f'<span class="cl-mvi-marker">{e(c["mvi_flag"])}</span>' if kind == 'fragile' else ''
        if kind == 'replaceable':
            extra = f'<span class="cl-replacement"><span class="cl-sample-glyph">G</span><span class="cl-sample-label">{e(c["new"])}</span></span>'
        samples.append(f'<div class="cl-sample cl-{kind}"><span class="cl-sample-glyph" aria-hidden="true">{letter}</span>'
                       f'<span class="cl-sample-label">{e(label)}</span>{extra}</div>')
    return f'''<section class="cl-explainer" data-cl-explainer data-step="0" data-playing="false" aria-labelledby="cl-title">
<div class="cl-heading"><div class="eyebrow">{e(c['eyebrow'])}</div><h2 id="cl-title">{e(c['title'])}</h2></div>
<figure class="cl-film">
<div class="cl-film-top"><span class="mono">{e(c['film'])}</span><button type="button" class="cl-play" data-cl-play data-play="{e(c['play'])}" data-pause="{e(c['pause'])}" data-replay="{e(c['replay'])}" hidden><span data-cl-play-icon aria-hidden="true">▶</span> <span data-cl-play-label>{e(c['play'])}</span></button></div>
<ol class="cl-steps" aria-label="{e(c['steps_label'])}">{steps}</ol>
<div class="cl-story" id="cl-story" aria-live="polite">{panels}</div>
<div class="cl-diagram" role="img" aria-label="{e(c['diagram_label'])}">
<div class="cl-motion-layer" aria-hidden="true"></div>
<div class="cl-stream"><span class="cl-node-label">{e(c['incoming'])}</span><div class="cl-stream-pieces" aria-hidden="true"><i>G</i><i>H</i><i>J</i></div></div>
<div class="cl-connector cl-incoming" aria-hidden="true"><i></i></div>
<div class="cl-buffer"><span class="cl-node-label">{e(c['budget'])}</span><div class="cl-slots">{''.join(samples)}</div><span class="cl-floor">⌑ {e(c['floor'])}</span><div class="cl-buffer-note">{buffer_notes}</div></div>
<div class="cl-connector cl-replay" aria-hidden="true"><i></i><i></i></div>
<div class="cl-model"><span class="cl-node-label">{e(c['model'])}</span><div class="cl-model-mark" aria-hidden="true">{''.join('<i></i>' for _ in range(9))}</div><div class="cl-model-note">{model_notes}</div></div>
</div>
<div class="cl-feedback"><span aria-hidden="true">↶</span> {e(c['feedback'])}</div>
<section class="cl-audit" aria-labelledby="cl-audit-title"><div class="cl-audit-heading"><h3 id="cl-audit-title">{e(c['audit_title'])}</h3><span class="mono">{e(c['audit_label'])}</span></div><ol>{audit_rows}</ol><p>{e(c['audit_note'])}</p></section>
<figcaption>{e(c['caption'])}</figcaption>
</figure>
<noscript><ol class="cl-static">{''.join(f'<li><strong>{e(s[0])}.</strong> {e(s[3])}</li>' for s in c['steps'])}</ol></noscript>
</section>'''
