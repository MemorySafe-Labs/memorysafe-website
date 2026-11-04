"""Build the Claudete concept (logo v7 design language). Separate, unpublished. No network or deployment."""
from pathlib import Path
from html import escape
from hashlib import sha256
import re
from research_visual import render_research_visual

ROOT=Path(__file__).resolve().parent
PUBLIC=ROOT/'public'
OLD=ROOT.parent/'netlify-publish-2026-10-12/public'

TEAM=[
    ('Ankit Mishra, MBA','ankit-mishra','https://www.linkedin.com/in/ankitmishra3/','Strategic Advisor','Assessor estratégico'),
    ('Grégoire Gervais-Vachon','gregoire-gervais-vachon','https://www.linkedin.com/in/gregoire-gervais-vachon-511942ba/','Advisor, GTM','Assessor de estratégia comercial'),
    ('Larissa Centeno','larissa-centeno','https://www.linkedin.com/in/larissa-centeno-a5b38842/','Advisor, operations & finance','Assessora de operações e finanças'),
    ('Grégoire Dubé','gregoire-dube','https://www.linkedin.com/in/gr%C3%A9goire-dub%C3%A9-b90056173/','Advisor, project controls & delivery','Assessor de controle e entrega de projetos'),
    ('Alexandre Rosenfeld','alexandre-rosenfeld','https://www.linkedin.com/in/a-rosenfeld/','Technical Advisor','Assessor técnico'),
]

ICONS={
'refresh':'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 1 1-2.64-6.36"></path><path d="M21 3v6h-6"></path></svg>',
'scatter':'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="5.5" cy="6" r="2.5"></circle><circle cx="18.5" cy="5" r="2.5"></circle><circle cx="12" cy="18" r="2.5"></circle><path d="M7.5 7.5l3 8"></path><path d="M17 7l-3.5 8.5"></path></svg>',
'lock':'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="11" width="16" height="9" rx="2"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3"></path></svg>',
'capture':'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h12v18l-6-4.5L6 21z"></path></svg>',
'store':'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><ellipse cx="12" cy="5" rx="8" ry="3"></ellipse><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"></path><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"></path></svg>',
'recall':'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="M16.5 16.5L21 21"></path></svg>',
'shield':'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"></path></svg>',
'key':'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="7.5" cy="15.5" r="3.5"></circle><path d="M10.5 12.5L21 2"></path><path d="M16 7l3 3"></path></svg>',
'eyeoff':'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 3l18 18"></path><path d="M10.6 5.1A9.8 9.8 0 0 1 12 5c5 0 9 4 10 7-.4 1.2-1.2 2.5-2.4 3.6M6.2 6.2C4 7.7 2.6 9.9 2 12c1 3 5 7 10 7 1.5 0 2.9-.3 4.2-.9"></path></svg>',
'scale':'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18"></path><path d="M5 7h14"></path><path d="M5 7l-2.5 6a3.5 3.5 0 0 0 7 0L7 7"></path><path d="M19 7l-2.5 6a3.5 3.5 0 0 0 7 0L21 7"></path></svg>',
}

COPY={
'en':{
'lang':'en-CA','prefix':'/','other':'/pt-br/','other_label':'PT','skip':'Skip to content',
'nav':['The problem','How it works','Pricing','Research','Value','About'],
'cta':'Download the free beta','cta_short':'Download',
'value':{'eyebrow':'MEMORYSAFE LABS / PLANNING SIMULATOR','title':'What could MemorySafe change for you?',
'intro':'Two small planning models — one for people using assistants, one for teams training models. Your numbers, simple arithmetic, no promises.',
'film':'Benefit simulator · your assumptions','tab1':'Assistants','tab2':'Model teams',
'p1_lead':'How much time does re-explaining cost a team? The middle scenario assumes half of it can be avoided.',
'p1_fields':[['people','People using AI assistants','10','1'],['minutes','Minutes each person spends re-explaining / week','20','1'],['rate','Value of one work hour (CAD)','50','1']],
'p1_outs':[['lost','Repetition / year'],['returned','Time returned / year'],['value','Illustrative value / year']],
'p1_formula':'people × minutes × 52 weeks → hours; half avoided in the middle scenario.',
'p2_lead':'What does a smaller replay buffer save in compute? The what-if assumes a buffer 30% smaller — 500 samples become about 350.',
'p2_fields':[['runs','Replay or update runs / day','200','1'],['mins','Minutes for one replay run','12','1'],['cost','Compute cost per hour (CAD)','2.50','0.1']],
'p2_outs':[['avoided','Runtime avoided / year'],['gross','Illustrative gross value / year']],
'p2_formula':'runs × minutes × 365 days × 30%, priced at your compute rate. This models runtime only — never model quality.',
'hours':'hrs',
'caption':'A planning model with your assumptions — the simulator from memorysafe.ca with fewer knobs. Actual results depend on workflow, setup and answer quality.'},
'hero_eyebrow':'One memory for all your AI assistants',
'hero_title':'Stop re-explaining yourself to your AI.',
'hero_intro':'MemorySafe is one memory your AI assistants share. Claude, Codex, Cursor and the rest read and save the same facts, so you never explain yourself twice. Free on your computer, in a single file nothing uploads; or hosted, so it follows you everywhere.',
'hero_primary':'Download the free beta','hero_secondary':'See how it works',
'hero_sub':'No account. No email signup.','hero_code':'Open source on GitHub','privacy_code':'Read the code on GitHub','source_code':'Source code on GitHub','github_label':'MemorySafe on GitHub','linkedin_label':'MemorySafe Labs on LinkedIn',
'demo':{'without':'Monday, without MemorySafe','with':'Monday, with MemorySafe','chip':'3 memories recalled','you':'You','assistant':'Assistant',
'u1':'Quick context again, since you won’t remember: I’m Carla, the deadline is Nov 14, we deploy with Docker, and we use Vue — please stop suggesting React.',
'a1':'Thanks for the context! Could you also remind me what we worked on last time?',
'u2':'Pick up where we left off.',
'a2':'On it — Nov 14 deadline, Vue front end, Docker deploy. We stopped at the login bug on Friday.',
'step1':'Without','step2':'With','pause':'Pause example','play':'Play example',
'label':'One memory, two Mondays','steps_label':'Explore the example',
'note':'Illustrative conversation · no data is saved.'},
'compatible':'FREE LOCAL PLUGIN FOR',
'ch_problem':'01 — THE PROBLEM','problem_title':'AI has a memory problem. Three of them.',
'problems':[['refresh','Groundhog Day','Every chat starts at zero. You re-type your tools, your rules, your deadlines — every session, in every app.'],['scatter','Scattered memory','Claude knows some of it, Codex another slice, Cursor nothing. Your context is fragmented across vendors that don’t talk to each other.'],['lock','Memory you don’t own','Vendor memory lives on their servers, on their terms. You can’t open it, back it up, or take it with you.']],
'ch_how':'02 — HOW IT WORKS','how_title':'One file. Three verbs.',
'how_lead':'Deliberately boring infrastructure: capture facts, keep them in a file you own, recall them when they matter.',
'verbs':[['capture','1 · Capture','As you work, MemorySafe saves concise, durable facts — decisions, preferences, deadlines. Automatically if you turn that on, or only when you say “remember this.”'],['store','2 · Store','Everything lands in one database file on your computer. Open it, back it up, review it in the local dashboard.'],['recall','3 · Recall','Your assistant searches memory before it answers, and only the facts it needs enter the conversation. Memories are never pruned for being old.']],
'how_strip':'<strong>You stay in charge of the verbs.</strong> Protect what must not change. Remove a memory from recall. Review conflicts when facts collide — nothing is silently overwritten.',
'ch_learn':'03 — IT KEEPS LEARNING YOU','learn_title':'Not just remembered. Learned.',
'learn_lead':'Models are frozen the day they ship. Your memory is the part that keeps learning — every decision and preference you confirm compounds.',
'learn_steps':[['WEEK 1','Knows the basics.','Your name, your tools, your rules of engagement. No more introductions.'],['MONTH 2','Knows your decisions.','What you chose, what you set aside, and why — settled questions stay settled.'],['MONTH 6','Knows how you work.','Your standards, your edge cases. Answers start from your context, not from zero.']],
'learn_strip':'<strong>And the learning is portable.</strong> Because it lives in a file you own, it survives model upgrades, new tools, even a change of assistant.',
'ch_editions':'03 — THE EDITIONS','edition_title':'Your memory. Your kind of setup.',
'edition_lead':'Start on your computer today, or let your memory follow you: Hosted is available now, free during the beta.',
'local_status':'FREE LOCAL BETA · AVAILABLE NOW','local_title':'On your computer. In your hands.',
'local_body':'A shared place for your supported desktop assistants to save and recall useful context.',
'local_points':['Claude Desktop, Claude Code, and Codex','Review memories, protect facts, inspect history','Your memory database stays on your computer'],
'local_cta':'Download the free beta','local_fine':'Free. Open source (Apache 2.0), forever.<br>Advanced features live in Hosted.',
'hosted_status':'HOSTED · AVAILABLE NOW · FREE DURING BETA','hosted_title':'Your memory follows you.',
'hosted_body':'One shared memory across supported AI apps and devices — Claude, Codex, Cursor and more — kept current wherever you work.',
'hosted_points':['One shared address your apps connect to','Laptop, phone, desktop','Hosted in Canada'],'hosted_cta':'Create your free account',
'hosted_fine':'Free while we keep improving it.<br>Can’t get in yet? <a href="mailto:contact@memorysafe.ca?subject=MemorySafe%20Hosted%20early%20access">Email us for early access</a>.',
'band_note':'The local plugin keeps your memory on one computer. Hosted is where every assistant you use meets one memory, on every device.',
'research_label':'A DIFFERENT SCALE.<br>THE SAME QUESTION.',
'research_title':'What deserves to stay?',
'research_body':'The question behind the product, asked at training scale: we study how AI models select past training examples to revisit when storage is limited. A separate research track, same enduring question.',
'research_cta':'Inside the research',
'ch_privacy':'04 — PRIVACY','privacy_title':'Private by architecture, not by promise.',
'privacy_lead':'Most privacy pages ask you to trust a policy. Ours asks you to look at a file path.',
'tiles':[['shield','Nothing uploaded by MemorySafe','Your memory database stays on your computer. No account, no sync, no MemorySafe server behind the free plugin.'],['key','You hold the keys','Protect locks a memory against change. Forget removes it from recall. The local dashboard shows what’s saved and what changed.'],['eyeoff','No sensitive capture','Secrets, credentials, payment and government IDs, health data: never captured, in any mode.'],['scale','Honest limits','A connected AI service still processes the context you choose to share, and forgetting removes a memory from recall — not from history or backups. We say both plainly.']],
'founder_eyebrow':'A HUMAN QUESTION, FIRST','founder_heading':'Better memory.<br>Less starting over.',
'founder_name':'Carla Centeno · Founder & CEO',
'founder_description':'MemorySafe Labs takes inspiration from human memory and turns it into questions we can build and test. Useful context should have continuity. And the person behind it should have control.',
'contact':'Say hello','team_heading':'Team & advisors','supported_heading':'Supported by',
'faq_eyebrow':'BEFORE YOU ASK','faq_heading':'A few things, made clear.',
'faqs':[
['Does the free version work across my devices?','The free plugin keeps its database on the computer where you install it. It can be shared by supported assistants on that computer. Cross-device memory is what the hosted edition does; it is available now, free during the beta.'],
['What does “local” actually mean?','The memory database stays on your computer. A connected AI service can still process the context you choose to share under its own terms. Local storage doesn’t mean the AI service itself runs locally.'],
['Can I change my mind about a memory?','Use the local dashboard to review saved memories, inspect changes, manage protection, and remove memories from recall. Removing a memory from recall does not completely erase history or backups.'],
['Are the advanced memory features available yet?','We’re testing tools to prioritize memories automatically: what to keep, revisit, or set aside. They’re being built into the hosted edition and aren’t included in the free local plugin.'],
],
'footer_eyebrow':'LESS STARTING OVER. MORE GETTING SOMEWHERE.','footer_title':'Pick up where you left off.',
'privacy':'Privacy','github':'GitHub','copyright':'MemorySafe Labs Inc. · 2026',
'download_title':'Make room for memory.',
'download_intro':'Choose your assistant. Install the free local beta. No signup, no dramatic onboarding.',
'download_eyebrow':'FREE LOCAL BETA','desktop_download':'Download for Claude Desktop','desktop_steps':'In Claude Desktop: Settings → Extensions → Advanced settings → Install Extension… Select the downloaded file. On Windows, don’t double-click the file.',
'terminal_intro':'With your assistant’s command-line tool installed, run:','copy':'Copy commands',
'after_title':'Then, pick up the thread.','after_body':'Restart your assistant. First-time setup may take a few minutes. Open the local dashboard to review your setup and connect supported assistants on this computer.',
'dashboard':'Open local dashboard','test_body':'Try asking your assistant to remember a harmless preference. Open a new chat and ask it to recall that preference.',
'guide':'Prefer pictures? View the visual guide',
'download_legal':'Free, open source under the Apache License 2.0. Advanced memory features of the hosted edition are not included. Your database stays on this computer; connected AI services may process selected context. Forget removes a memory from recall, not completely from history or backups.',
'notes':'Release notes','product_privacy':'Product privacy','terms':'Beta terms',
'upd_label':'Optional','upd_title':'Want release updates?','upd_body':'Leave an email and we’ll write only when a new release ships — nothing else. The download never requires it.','upd_cta':'Notify me',
'thanks_title':'You’re on the list.','thanks_body':'We’ll email you when a new release ships — and that’s all. The beta itself stays signup-free.','thanks_back':'Back to download',
'research_eyebrow':'MEMORYSAFE LABS / CONTINUAL-LEARNING RESEARCH',
'research_page_title':'Learning continues. What stays?',
'research_page_intro':'A model cannot revisit everything it has ever seen. We study how to choose what it returns to.',
'research_note':'This is research into model training. It is separate from the free local assistant plugin and the hosted edition. No performance results are presented on this page.',
'research_contact':'Talk about your research question',
'cases_label':'RESEARCH SETTING · POSSIBLE APPLICATIONS','cases_title':'Where forgetting has consequences.',
'cases_lead':'Our continual-learning evaluation uses medical images. Financial models, edge devices, and robotics are possible applications to explore with partners.',
'cases':[['use-medical-ai','Medical AI','Rare clinical cases can be overwritten as models absorb new data.','Prioritize vulnerable, clinically important samples.'],['use-fraud-detection','Model-risk & retraining','Changing data can make previously reliable financial models drift.','Preserve important evidence across retraining cycles.'],['use-edge-ai','Edge AI','Strict storage and compute limits make every retained sample matter.','Allocate bounded memory intentionally.'],['use-robotics','Robotics','New environments can interfere with previously learned skills.','Protect fragile capabilities during adaptation.']],
},
'pt':{
'lang':'pt-BR','prefix':'/pt-br/','other':'/','other_label':'EN','skip':'Ir para o conteúdo',
'nav':['O problema','Como funciona','Preços','Pesquisa','Valor','Sobre'],
'cta':'Baixar o beta gratuito','cta_short':'Baixar',
'value':{'eyebrow':'MEMORYSAFE LABS / SIMULADOR DE PLANEJAMENTO','title':'O que o MemorySafe pode mudar para você?',
'intro':'Dois pequenos modelos de planejamento — um para quem usa assistentes, outro para equipes que treinam modelos. Seus números, aritmética simples, sem promessas.',
'film':'Simulador de benefício · suas premissas','tab1':'Assistentes','tab2':'Equipes de modelo',
'p1_lead':'Quanto tempo custa se explicar de novo? O cenário intermediário assume que metade pode ser evitada.',
'p1_fields':[['people','Pessoas usando assistentes de IA','10','1'],['minutes','Minutos que cada pessoa gasta se explicando / semana','20','1'],['rate','Valor de uma hora de trabalho (CAD)','50','1']],
'p1_outs':[['lost','Repetição / ano'],['returned','Tempo devolvido / ano'],['value','Valor ilustrativo / ano']],
'p1_formula':'pessoas × minutos × 52 semanas → horas; metade evitada no cenário intermediário.',
'p2_lead':'O que um buffer de replay menor economiza em computação? O cenário assume um buffer 30% menor — 500 exemplos viram cerca de 350.',
'p2_fields':[['runs','Execuções de replay ou atualização / dia','200','1'],['mins','Minutos de uma execução de replay','12','1'],['cost','Custo de computação por hora (CAD)','2.50','0.1']],
'p2_outs':[['avoided','Tempo de execução evitado / ano'],['gross','Valor bruto ilustrativo / ano']],
'p2_formula':'execuções × minutos × 365 dias × 30%, ao seu custo de computação. Modela apenas tempo de execução — nunca a qualidade do modelo.',
'hours':'h',
'caption':'Um modelo de planejamento com as suas premissas — o simulador do memorysafe.ca com menos controles. Resultados reais dependem de fluxo de trabalho, configuração e qualidade das respostas.'},
'hero_eyebrow':'Uma memória para todos os seus assistentes de IA',
'hero_title':'Chega de se explicar de novo para a sua IA.',
'hero_intro':'O MemorySafe é uma memória que seus assistentes de IA compartilham. Claude, Codex, Cursor e os outros leem e salvam os mesmos fatos, e você nunca mais se explica duas vezes. Gratuito no seu computador, em um único arquivo que nada envia; ou hospedado, para acompanhar você em todo lugar.',
'hero_primary':'Baixar o beta gratuito','hero_secondary':'Veja como funciona',
'hero_sub':'Sem conta. Sem cadastro.','hero_code':'Código aberto no GitHub','privacy_code':'Leia o código no GitHub','source_code':'Código-fonte no GitHub','github_label':'MemorySafe no GitHub','linkedin_label':'MemorySafe Labs no LinkedIn',
'demo':{'without':'Segunda, sem MemorySafe','with':'Segunda, com MemorySafe','chip':'3 memórias recuperadas','you':'Você','assistant':'Assistente',
'u1':'Contexto de novo, já que você não vai lembrar: sou a Carla, o prazo é 14/nov, usamos Docker e o front é Vue — pare de sugerir React.',
'a1':'Obrigado pelo contexto! Pode me lembrar também no que trabalhamos da última vez?',
'u2':'Continue de onde paramos.',
'a2':'Certo — prazo 14/nov, front em Vue, deploy com Docker. Paramos no bug do login na sexta.',
'step1':'Sem','step2':'Com','pause':'Pausar exemplo','play':'Reproduzir exemplo',
'label':'Uma memória, duas segundas-feiras','steps_label':'Explore o exemplo',
'note':'Conversa ilustrativa · nenhum dado é salvo.'},
'compatible':'PLUGIN LOCAL GRATUITO PARA',
'ch_problem':'01 — O PROBLEMA','problem_title':'A IA tem um problema de memória. Três, na verdade.',
'problems':[['refresh','Dia da marmota','Toda conversa começa do zero. Você redigita suas ferramentas, suas regras, seus prazos — em cada sessão, em cada app.'],['scatter','Memória espalhada','O Claude sabe uma parte, o Codex outra, o Cursor nada. Seu contexto está fragmentado entre empresas que não conversam entre si.'],['lock','Memória que não é sua','A memória dos provedores vive nos servidores deles, nas regras deles. Você não pode abri-la, copiá-la nem levá-la com você.']],
'ch_how':'02 — COMO FUNCIONA','how_title':'Um arquivo. Três verbos.',
'how_lead':'Infraestrutura deliberadamente simples: capturar fatos, guardá-los em um arquivo que é seu, recuperá-los quando importam.',
'verbs':[['capture','1 · Capturar','Enquanto você trabalha, o MemorySafe salva fatos concisos e duráveis — decisões, preferências, prazos. Automaticamente, se você ativar, ou só quando você disser “lembre disso”.'],['store','2 · Guardar','Tudo fica em um único arquivo de banco de dados no seu computador. Abra, faça backup, revise no painel local.'],['recall','3 · Recuperar','Seu assistente consulta a memória antes de responder, e só os fatos necessários entram na conversa. Memórias nunca são descartadas por serem antigas.']],
'how_strip':'<strong>Os verbos continuam seus.</strong> Proteja o que não pode mudar. Remova uma memória da recuperação. Revise conflitos quando fatos se contradizem — nada é sobrescrito em silêncio.',
'ch_learn':'03 — ELA CONTINUA APRENDENDO VOCÊ','learn_title':'Não só lembrada. Aprendida.',
'learn_lead':'Modelos ficam congelados no dia em que são lançados. Sua memória é a parte que continua aprendendo — cada decisão e preferência que você confirma se acumula.',
'learn_steps':[['SEMANA 1','Sabe o básico.','Seu nome, suas ferramentas, suas regras. Sem apresentações de novo.'],['MÊS 2','Conhece suas decisões.','O que você escolheu, o que deixou de lado e por quê — o que foi decidido continua decidido.'],['MÊS 6','Sabe como você trabalha.','Seus padrões, seus casos particulares. As respostas partem do seu contexto, não do zero.']],
'learn_strip':'<strong>E o aprendizado é portátil.</strong> Como vive em um arquivo que é seu, sobrevive a novas versões de modelo, novas ferramentas e até a uma troca de assistente.',
'ch_editions':'03 — AS VERSÕES','edition_title':'Sua memória. Do seu jeito.',
'edition_lead':'Comece hoje no seu computador, ou deixe sua memória acompanhar você: o Hosted já está disponível, gratuito durante o beta.',
'local_status':'BETA LOCAL GRATUITO · DISPONÍVEL AGORA','local_title':'No seu computador. Nas suas mãos.',
'local_body':'Um espaço compartilhado para seus assistentes desktop compatíveis salvarem e recuperarem contexto útil.',
'local_points':['Claude Desktop, Claude Code e Codex','Revise memórias, proteja fatos, consulte o histórico','Seu banco de memórias fica no seu computador'],
'local_cta':'Baixar o beta gratuito','local_fine':'Gratuito. Código aberto (Apache 2.0), para sempre.<br>Os recursos avançados ficam no Hosted.',
'hosted_status':'HOSTED · DISPONÍVEL AGORA · GRATUITO NO BETA','hosted_title':'Sua memória acompanha você.',
'hosted_body':'Uma memória compartilhada entre apps de IA e dispositivos compatíveis — Claude, Codex, Cursor e outros — que mantém seu contexto atualizado onde você estiver.',
'hosted_points':['Um endereço compartilhado ao qual seus apps se conectam','Notebook, celular, desktop','Hospedado no Canadá'],'hosted_cta':'Criar sua conta gratuita',
'hosted_fine':'Gratuito enquanto o aperfeiçoamos.<br>Ainda não conseguiu entrar? <a href="mailto:contact@memorysafe.ca?subject=MemorySafe%20Hosted%20early%20access">Peça acesso por e-mail</a>.',
'band_note':'O plugin local guarda sua memória em um computador. O Hosted é onde todos os seus assistentes encontram uma só memória, em todos os dispositivos.',
'research_label':'OUTRA ESCALA.<br>A MESMA PERGUNTA.',
'research_title':'O que merece ficar?',
'research_body':'A pergunta por trás do produto, feita na escala do treinamento: estudamos como modelos de IA selecionam exemplos anteriores para revisitar quando o armazenamento é limitado. Uma linha de pesquisa separada, a mesma pergunta de sempre.',
'research_cta':'Por dentro da pesquisa',
'ch_privacy':'04 — PRIVACIDADE','privacy_title':'Privada por arquitetura, não por promessa.',
'privacy_lead':'A maioria das páginas de privacidade pede confiança em uma política. A nossa pede que você olhe o caminho de um arquivo.',
'tiles':[['shield','Nada enviado pelo MemorySafe','Seu banco de memórias fica no seu computador. Sem conta, sem sincronização, sem servidor do MemorySafe no plugin gratuito.'],['key','As chaves são suas','Proteger trava uma memória contra mudanças. Esquecer a remove da recuperação. O painel local mostra o que foi salvo e o que mudou.'],['eyeoff','Sem captura sensível','Senhas, credenciais, documentos, dados de pagamento e de saúde: nunca capturados, em nenhum modo.'],['scale','Limites ditos com clareza','Um serviço de IA conectado ainda processa o contexto que você escolhe compartilhar, e esquecer remove uma memória da recuperação — não do histórico ou dos backups. Dizemos as duas coisas com todas as letras.']],
'founder_eyebrow':'UMA PERGUNTA HUMANA, PRIMEIRO','founder_heading':'Memória melhor.<br>Menos recomeços.',
'founder_name':'Carla Centeno · Fundadora e CEO',
'founder_description':'A MemorySafe Labs se inspira na memória humana e transforma essa inspiração em perguntas que podemos construir e testar. Contexto útil merece continuidade. E quem está por trás dele merece controle.',
'contact':'Vamos conversar','team_heading':'Equipe e assessores','supported_heading':'Apoiado por',
'faq_eyebrow':'ANTES QUE VOCÊ PERGUNTE','faq_heading':'Algumas coisas, bem claras.',
'faqs':[
['A versão gratuita funciona entre dispositivos?','O plugin gratuito mantém o banco de dados no computador em que é instalado. Assistentes compatíveis nesse computador podem compartilhá-lo. A memória entre dispositivos é o que a versão hospedada faz; ela já está disponível, gratuita durante o beta.'],
['O que “local” significa?','O banco de memórias fica no seu computador. Um serviço de IA conectado ainda pode processar o contexto que você compartilha, conforme os próprios termos. Armazenamento local não significa que o serviço de IA roda localmente.'],
['Posso mudar de ideia sobre uma memória?','No painel local, você pode revisar memórias, consultar mudanças, gerenciar a proteção e remover memórias da recuperação. Isso não apaga completamente o histórico ou os backups.'],
['Os recursos avançados de memória já estão disponíveis?','Estamos testando ferramentas para priorizar memórias automaticamente: o que guardar, revisitar ou deixar de lado. Elas estão sendo construídas na versão hospedada e não fazem parte do plugin local gratuito.'],
],
'footer_eyebrow':'MENOS RECOMEÇAR. MAIS IR ADIANTE.','footer_title':'Continue de onde parou.',
'privacy':'Privacidade','github':'GitHub','copyright':'MemorySafe Labs Inc. · 2026',
'download_title':'Abra espaço para a memória.',
'download_intro':'Escolha seu assistente. Instale o beta local gratuito. Sem cadastro, sem complicar.',
'download_eyebrow':'BETA LOCAL GRATUITO','desktop_download':'Baixar para Claude Desktop','desktop_steps':'No Claude Desktop: Settings → Extensions → Advanced settings → Install Extension… Selecione o arquivo baixado. No Windows, não dê duplo clique no arquivo.',
'terminal_intro':'Com a ferramenta de linha de comando do seu assistente instalada, execute:','copy':'Copiar comandos',
'after_title':'Depois, retome a conversa.','after_body':'Reinicie seu assistente. A primeira configuração pode levar alguns minutos. Abra o painel local para revisar a instalação e conectar assistentes compatíveis neste computador.',
'dashboard':'Abrir painel local','test_body':'Experimente pedir ao assistente para lembrar uma preferência simples. Abra outro chat e peça que ele recupere essa preferência.',
'guide':'Prefere imagens? Veja o guia visual',
'download_legal':'Gratuito, de código aberto sob a Apache License 2.0. Os recursos avançados da versão hospedada não estão incluídos. O banco de dados fica neste computador; serviços de IA conectados podem processar contexto selecionado. Esquecer remove uma memória da recuperação, mas não apaga completamente o histórico ou os backups.',
'notes':'Notas da versão','product_privacy':'Privacidade do produto','terms':'Termos do beta',
'upd_label':'Opcional','upd_title':'Quer saber das novas versões?','upd_body':'Deixe um e-mail e escrevemos só quando sair uma nova versão — nada além disso. O download nunca exige cadastro.','upd_cta':'Avisar-me',
'thanks_title':'Você está na lista.','thanks_body':'Vamos escrever quando sair uma nova versão — e só. O beta continua sem cadastro.','thanks_back':'Voltar ao download',
'research_eyebrow':'MEMORYSAFE LABS / PESQUISA EM APRENDIZADO CONTÍNUO',
'research_page_title':'O aprendizado continua. O que fica?',
'research_page_intro':'Um modelo não consegue revisitar tudo o que já viu. Estudamos como escolher aquilo a que ele deve retornar.',
'research_note':'Esta é uma pesquisa sobre treinamento de modelos. Ela é separada do plugin local gratuito e da versão hospedada. Esta página não apresenta resultados de desempenho.',
'research_contact':'Converse sobre sua pergunta de pesquisa',
'cases_label':'CENÁRIO DE PESQUISA · APLICAÇÕES POSSÍVEIS','cases_title':'Onde esquecer tem consequências.',
'cases_lead':'Nossa avaliação de aprendizado contínuo usa imagens médicas. Modelos financeiros, dispositivos de borda e robótica são aplicações possíveis a explorar com parceiros.',
'cases':[['use-medical-ai','IA médica','Casos clínicos raros podem ser sobrescritos à medida que o modelo absorve novos dados.','Priorizar exemplos vulneráveis e clinicamente importantes.'],['use-fraud-detection','Risco de modelo e retreinamento','Mudanças nos dados podem fazer modelos financeiros antes confiáveis derivarem.','Preservar evidências importantes entre ciclos de retreinamento.'],['use-edge-ai','IA de borda','Limites rígidos de armazenamento e computação tornam cada exemplo retido importante.','Alocar memória limitada com intenção.'],['use-robotics','Robótica','Ambientes novos podem interferir em habilidades já aprendidas.','Proteger capacidades frágeis durante a adaptação.']],
}}

# Stripe Payment Links, one per offer. Empty until they are created in the Stripe
# Dashboard; an empty one renders a disabled button and the build says so, so nothing
# with a dead payment button is deployed by accident.
# TEST MODE links (Stripe sandbox, 30 Oct 2026). Replace with the live links before deploying.
# LIVE Stripe payment links (account acct_1UWIFK6tTEE8b1kM, created 3 Nov 2026). Hosted Personal is free
# during the beta, so its links are empty here; the US$10/mo and US$100/yr test links stay in the sandbox.
STRIPE={'personal_month':'',
        'personal_year':'',
        'team':'https://buy.stripe.com/9B69AM6fu9ffdRx1VNbZe00',
        'pilot':'https://buy.stripe.com/7sY8wIavKcrr00H57ZbZe01'}
CONTACT='mailto:contact@memorysafe.ca'
# Hosted is free with no end date while it is improved (Carla, 30 Oct 2026). Buttons go to the service itself (Carla, 3 Nov);
# the email stays as the fallback in the fine print while sign-up is still opening up.
HOSTED='https://memory.memorysafe.ca/'
# Straight to the create-account form (Hosted 0.7.7); the landing page offers sign-in for people who already have one.
HOSTED_SIGNUP='https://memory.memorysafe.ca/account/start?signup=1&next=/account&lang='  # + en or pt-BR: Cognito's forms open in the page's language
HOSTED_TEAM_SIGNUP='https://memory.memorysafe.ca/account/start?signup=1&next=%2Forgs%2Fnew%3Fplan%3Dteam&lang='  # Team: create the account, then the organization, then pay from its page (Hosted 0.7.9)
def signup_lang(prefix): return 'en' if prefix=='/' else 'pt-BR'
BETA=CONTACT+'?subject=MemorySafe%20Hosted%20early%20access'
# All prices in US dollars (Carla, 3 Nov 2026). The audit tiers are the 14 Oct proposal's C$7,500 / C$22,000 /
# C$3,500 a month converted at about 0.72 and rounded: US$5,500 / US$16,000 / US$2,500.
PRICING={
'en':{'eyebrow':'PRICING','title':'Free on your computer. Free everywhere you work, for now.',
'intro':'The local plugin and Hosted are free. Companies start with a free fragility test.',
'for_you':'FOR YOU','for_companies':'FOR COMPANIES','pending':'Payment link coming soon',
'cards':[
 {'status':'FREE · AVAILABLE NOW','name':'Local plugin','price':'Free','per':'','includes':'What’s included','body':'One memory for Claude Desktop, Claude Code and Codex on one computer.',
  'points':['Kept in one file on your computer','Review, protect and forget what it keeps','Open source, Apache 2.0'],
  'buttons':[('Download','download','')],'fine':''},
 {'status':'HOSTED · FREE','name':'Hosted Personal','price':'Free','per':'','featured':True,'includes':'Everything in Local, plus','body':'Your memory follows you: Claude, Codex, Cursor and more, on laptop, phone and desktop.',
  'points':['Unlimited connected apps','Up to 25,000 memories','Export and erase with a receipt','Hosted in Canada'],
  'buttons':[('Create your free account','hosted','')],'fine':'Free while we keep improving it. If paid plans start, at US$10 a month, you hear first. Can’t get in yet? <a href="'+BETA+'">Email us for early access</a>.'},
 {'status':'COMPANIES · EARLY ACCESS','name':'Team','price':'US$29','per':'/ person / month','includes':'Everything in Hosted Personal, plus','body':'One memory your whole team reads and saves to, set up with you by our founders.',
  'points':['One memory the whole team reads and saves to','People join by invitation, on every assistant they use','Onboarding with our founders, and a direct line to them','Flat monthly pricing by company size, on request'],
  'buttons':[('Get Team','team','')],'fine':'Create your free account, then pay for Team from your organization’s page. Stripe handles the payment.'},
 {'status':'COMPANIES · STARTS FREE','name':'Audits & pilots','price':'Free','per':'to start','includes':'What’s included','body':'We first test your agent or model for free and show you where it forgets what matters. Then we propose the next step.',
  'points':['Free fragility test: one agent or model, a short readout','Memory Audit: an independent report with a test pack you can rerun, from US$5,500','Continual Learning pilot: MemorySafe running on one of your training streams for 3 months, US$7,500'],
  'buttons':[('Book a free fragility test','test','')],'fine':'Medical and regulated work is quoted separately.'}],
'note':'All prices in US dollars. Payments are handled by Stripe; MemorySafe never sees your card number. Questions: <a href="'+CONTACT+'">contact@memorysafe.ca</a>'},
'pt':{'eyebrow':'PREÇOS','title':'Grátis no seu computador. Grátis onde você trabalha, por enquanto.',
'intro':'O plugin local e o Hosted são gratuitos. Empresas começam com um teste de fragilidade gratuito.',
'for_you':'PARA VOCÊ','for_companies':'PARA EMPRESAS','pending':'Link de pagamento em breve',
'cards':[
 {'status':'GRÁTIS · DISPONÍVEL AGORA','name':'Plugin local','price':'Grátis','per':'','includes':'O que está incluído','body':'Uma memória para Claude Desktop, Claude Code e Codex em um computador.',
  'points':['Guardada em um único arquivo no seu computador','Revise, proteja e esqueça o que ela guarda','Código aberto, Apache 2.0'],
  'buttons':[('Baixar','download','')],'fine':''},
 {'status':'HOSTED · GRÁTIS','name':'Hosted Pessoal','price':'Grátis','per':'','featured':True,'includes':'Tudo do Local, mais','body':'Sua memória acompanha você: Claude, Codex, Cursor e outros, no notebook, no celular e no desktop.',
  'points':['Apps conectados sem limite','Até 25.000 memórias','Exporte e apague com recibo','Hospedado no Canadá'],
  'buttons':[('Criar sua conta gratuita','hosted','')],'fine':'Grátis enquanto o aperfeiçoamos. Se planos pagos começarem, a US$10 por mês, você fica sabendo antes. Ainda não conseguiu entrar? <a href="'+BETA+'">Peça acesso por e-mail</a>.'},
 {'status':'EMPRESAS · LANÇAMENTO','name':'Team','price':'US$29','per':'/ pessoa / mês','includes':'Tudo do Hosted Pessoal, mais','body':'Uma memória que toda a equipe lê e alimenta, configurada com você pelos nossos fundadores.',
  'points':['Uma memória que toda a equipe lê e alimenta','Cada pessoa entra por convite, em todos os assistentes que usa','Onboarding com os fundadores, e uma linha direta com eles','Preço mensal fixo por tamanho de empresa, sob consulta'],
  'buttons':[('Assinar o Team','team','')],'fine':'Crie sua conta gratuita e pague o Team na página da sua organização. O Stripe processa o pagamento.'},
 {'status':'EMPRESAS · COMEÇA GRÁTIS','name':'Auditorias e pilotos','price':'Grátis','per':'para começar','includes':'O que está incluído','body':'Primeiro testamos seu agente ou modelo de graça e mostramos onde ele esquece o que importa. Depois propomos o próximo passo.',
  'points':['Teste de fragilidade gratuito: um agente ou modelo, um resumo curto','Auditoria de Memória: relatório independente com pacote de testes que você pode repetir, a partir de US$5.500','Piloto de Aprendizado Contínuo: o MemorySafe rodando em um dos seus fluxos de treinamento por 3 meses, US$7.500'],
  'buttons':[('Agendar o teste gratuito','test','')],'fine':'Trabalhos médicos e regulados têm orçamento à parte.'}],
'note':'Todos os preços em dólares americanos. Os pagamentos são processados pelo Stripe; o MemorySafe nunca vê o número do seu cartão. Dúvidas: <a href="'+CONTACT+'">contact@memorysafe.ca</a>'}}

GITHUB='https://github.com/MemorySafe-Labs/memorysafe-plugin'
LINKEDIN='https://www.linkedin.com/company/memorysafe-labs'
LINKEDIN_ICON='<svg class="gh-icon li-icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/></svg>'
GITHUB_ICON='<svg class="gh-icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"/></svg>'

def mark():
    return '<span class="brand-mark" aria-hidden="true">'+'<i></i>'*16+'</span><span class="brand-name">MemorySafe<small>Labs</small></span>'

def header(c,page=''):
    p=c['prefix'];other=c['other']+page
    links=[p+'#problem',p+'#how',p+'pricing/',p+'research/',p+'value/',p+'#about']
    nav=''.join(f'<a href="{href}">{text}</a>' for href,text in zip(links,c['nav']))
    langs=f'<a href="{p+page}" aria-current="page">{"PT" if p!="/" else "EN"}</a><span aria-hidden="true">/</span><a href="{other}">{c["other_label"]}</a>'
    return f'''<a class="skip" href="#main">{c['skip']}</a><div class="masthead"><div class="wrap"><div class="nav"><a class="brand" href="{p}" aria-label="MemorySafe Labs">{mark()}</a><nav class="nav-links" aria-label="{'Main navigation' if p=='/' else 'Navegação principal'}">{nav}</nav><div class="nav-actions"><nav class="language" aria-label="Language">{langs}</nav><a class="nav-github" href="{GITHUB}" aria-label="{c['github_label']}">{GITHUB_ICON}<span class="nav-github-label">GitHub</span></a><a class="nav-github nav-linkedin" href="{LINKEDIN}" aria-label="{c['linkedin_label']}">{LINKEDIN_ICON}</a><a class="button small" href="{p}download/"><span class="nav-cta-long">{c['cta']}</span><span class="nav-cta-short">{c['cta_short']}</span></a></div></div></div></div>'''

def footer(c):
    p=c['prefix']
    return f'''<footer class="footer on-dark"><div class="wrap"><div class="footer-top"><div><div class="eyebrow">{c['footer_eyebrow']}</div><h2>{c['footer_title']}</h2></div><a class="button light" href="{p}download/">{c['cta']}</a></div><div class="footer-meta"><a class="brand" href="{p}" aria-label="MemorySafe Labs">{mark()}</a><span class="footer-copy">{c['copyright']}</span><nav class="footer-links"><a href="{p}privacy/">{c['privacy']}</a><a href="{GITHUB}">{c['github']} ↗</a><a href="{LINKEDIN}">LinkedIn ↗</a><a href="mailto:contact@memorysafe.ca">{c['contact']} ↗</a></nav></div></div></footer>'''

# Link previews (Open Graph + Twitter), as deployed on 29 Oct 2026; the image is public/assets/og-image.png (1800x945).
OG_DESC={'/':'Governed memory for AI, from neuroscience. Free local plugin gives Claude, Cursor and your other agents one shared memory on your computer.',
         '/pt-br/':'Memória governada para IA, inspirada na neurociência. Plugin local e gratuito: uma memória compartilhada entre Claude, Cursor e seus agentes.'}
def og(c,title,page=''):
    url='https://memorysafe.ca'+c['prefix']+page
    t=f'{title} — MemorySafe Labs'; d=OG_DESC[c['prefix']]; img='https://memorysafe.ca/assets/og-image.png'
    return (f'<meta property="og:type" content="website"><meta property="og:site_name" content="MemorySafe Labs"><meta property="og:url" content="{url}">'
            f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:image" content="{img}">'
            f'<meta property="og:image:width" content="1800"><meta property="og:image:height" content="945"><meta name="twitter:card" content="summary_large_image">'
            f'<meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{img}">')
def shell(c,title,body,page=''):
    style='/style.css?v='+sha256((PUBLIC/'style.css').read_bytes()).hexdigest()[:12]
    script='/site.js?v='+sha256((PUBLIC/'site.js').read_bytes()).hexdigest()[:12]
    research_assets=''
    if page=='research/':
        ra_css='/research-animation.css?v='+sha256((PUBLIC/'research-animation.css').read_bytes()).hexdigest()[:12]
        ra_js='/research-animation.js?v='+sha256((PUBLIC/'research-animation.js').read_bytes()).hexdigest()[:12]
        research_assets=f'<link rel="stylesheet" href="{ra_css}"><script src="{ra_js}" defer></script>'
    return f'''<!doctype html><html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — MemorySafe Labs</title><meta name="description" content="{'Memory for the things worth remembering. Free, open-source local plugin; hosted memory free during the beta.' if c['prefix']=='/' else 'Memória para o que vale a pena lembrar. Plugin local gratuito e de código aberto; memória hospedada gratuita durante o beta.'}">{og(c,title,page)}<meta name="theme-color" content="#ffffff"><link rel="icon" href="/assets/mark.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"><link rel="stylesheet" href="{style}">{research_assets}<script src="{script}" defer></script></head><body>{header(c,page)}<main id="main">{body}</main>{footer(c)}</body></html>'''

def updates_form(c):
    p=c['prefix']
    return f"""<form name="release-updates" method="POST" action="{p}download/thanks/" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="release-updates"><input type="hidden" name="lang" value="{'en' if p=='/' else 'pt'}"><p class="hp" hidden><label>Leave this empty<input name="bot-field"></label></p><div class="updates-row"><label class="sr-only" for="upd-email-{'h' if p=='/' else 'hp'}">Email</label><input type="email" name="email" required placeholder="you@example.com"><button class="button" type="submit">{c['upd_cta']}</button></div></form>"""

def hero_demo(c):
    pt=c['lang'].startswith('pt')
    d=({'title':'Conte uma vez. Continue em outro assistente.','save':'Conte','store':'Guarde','recall':'Recupere','pause':'Pausar','play':'Reproduzir','you':'Você','first':'UMA CONVERSA NO CLAUDE DESKTOP','second':'UMA NOVA CONVERSA NO CODEX','u1':'Lembre: nosso lançamento mudou para sexta-feira.','a1':'Salvo no MemorySafe.','fact':'Lançamento → mudou para sexta-feira','shared':'Uma memória compartilhada','source':'Disponível para seus assistentes conectados','u2':'O que devo terminar primeiro?','a2':'O lançamento é na sexta, então comece pela página de cadastro.','chip':'Recuperado do MemorySafe','end':'Outro assistente. O mesmo contexto.','note':'Exemplo ilustrativo · Claude Desktop e Codex conectados ao mesmo MemorySafe local. Nenhum dado é salvo.'} if pt else {'title':'Tell one assistant. Continue with another.','save':'Tell','store':'Keep','recall':'Recall','pause':'Pause','play':'Play','you':'You','first':'A CONVERSATION IN CLAUDE DESKTOP','second':'A NEW CONVERSATION IN CODEX','u1':'Remember: our launch moved to Friday.','a1':'Saved to MemorySafe.','fact':'Launch → moved to Friday','shared':'One shared memory','source':'Available to your connected assistants','u2':'What should I finish first?','a2':'The launch is Friday, so start with the signup page.','chip':'Retrieved from MemorySafe','end':'Different assistant. Same context.','note':'Illustrative example · Claude Desktop and Codex connected to the same local MemorySafe. No data is saved.'})
    steps=''.join(f'<li><button type="button" class="demo-step" data-demo-step="{i}" aria-pressed="{str(i==3).lower()}"><span class="demo-step-number">0{i}</span>{d[k]}</button></li>' for i,k in enumerate(['save','store','recall'],1))
    return f'''<figure class="hero-demo handoff-demo" data-memory-demo data-stage="3" aria-label="{d['title']}">
<div class="ms-film-top"><span class="mono">CLAUDE → MEMORYSAFE → CODEX</span><button type="button" class="demo-play" data-demo-play data-pause="{d['pause']}" data-play="{d['play']}" aria-label="{d['pause']}" aria-pressed="false" hidden><span data-demo-icon aria-hidden="true">Ⅱ</span> <span data-demo-label>{d['pause']}</span></button></div>
<h2 class="handoff-title">{d['title']}</h2><ol class="ms-steps" aria-label="{d['title']}">{steps}</ol>
<div class="chat-card agent-claude" data-demo-card="1"><div class="agent-heading"><img class="agent-badge app-logo" src="/assets/claude-app.png" width="36" height="36" alt=""><div><strong>Claude Desktop</strong><span class="agent-context">{d['first']}</span></div></div><p class="msg user shown" data-demo-msg="u1"><span class="sr-only">{d['you']}: </span>{d['u1']}</p><p class="saved-line shown" data-demo-msg="a1">✓ {d['a1']}</p></div>
<div class="memory-bridge" data-demo-card="2"><span class="flow-line flow-in" aria-hidden="true"><i></i></span><div class="shared-memory"><div class="memory-brand"><img src="/assets/mark.svg" width="22" height="22" alt=""><strong>MemorySafe</strong><span>{d['shared']}</span></div><p class="memory-fact shown" data-demo-msg="fact">{d['fact']}</p><span class="memory-source">{d['source']}</span></div><span class="flow-line flow-out" aria-hidden="true"><i></i></span></div>
<div class="chat-card agent-codex" data-demo-card="3"><div class="agent-heading"><img class="agent-badge app-logo" src="/assets/codex-app.png" width="36" height="36" alt=""><div><strong>Codex</strong><span class="agent-context">{d['second']}</span></div></div><p class="msg user shown" data-demo-msg="u2"><span class="sr-only">{d['you']}: </span>{d['u2']}</p><span class="recall-chip shown" data-demo-msg="chip">↳ {d['chip']}</span><p class="msg ai shown" data-demo-msg="a2">{d['a2']}</p></div>
<p class="handoff-end">{d['end']}</p><figcaption class="demo-note">{d['note']}</figcaption></figure>'''

# Programs that support MemorySafe Labs: shown under the team as one row of solid-black marks (CSS filter), no tiles.
# Files in public/assets/programs/ come from each program's own site or brand kit (see ../partner-logo-sources.md).
# (name, href, file or None for a typed wordmark, caption or None)
# Order = date each program accepted us (MemorySafe-Docs/funding/tracker_data.py): NVIDIA 11 Feb 2026, AWS 1 May,
# Google 23 Jun, Desjardins 14 Sep, Claude 6 Oct, Mila and Dobson both confirmed 12 Oct, NEXT AI 21 Oct.
PROGRAMS=[('NVIDIA Inception','https://www.nvidia.com/en-us/startups/','nvidia-inception.png',None),
          ('AWS Activate','https://aws.amazon.com/activate/',None,'Activate'),
          ('Google for Startups','https://startup.google.com/','google-for-startups.png',None),
          ('Startup en Résidence · Desjardins','https://www.startup-residence.ca/','startup-en-residence.png',None),
          ('Claude for Startups','https://claude.com/programs/startups','claude.svg','for Startups'),
          ('Mila Venture Sprint','https://mila.quebec/','mila.png','Venture Sprint'),
          ('McGill Dobson Centre for Entrepreneurship','https://www.mcgill.ca/dobson/','mcgill-dobson.png',None),
          ('NEXT AI','https://www.nextcanada.com/next-ai/','next.png','AI')]
def programs(c):
    items=''
    for name,href,f,cap in PROGRAMS:
        slug=(f or 'aws').split('.')[0]
        mark=f'<img src="/assets/programs/{f}" alt="" width="1" height="1" loading="lazy">' if f else '<span class="program-aws" aria-hidden="true">aws</span>'
        if slug=='startup-en-residence': mark+='<img src="/assets/programs/desjardins.png" alt="" width="1" height="1" loading="lazy">'
        caption=f'<span class="program-caption">{escape(cap)}</span>' if cap else ''
        items+=f'<li><a class="program program-{slug}" href="{href}" target="_blank" rel="noopener" aria-label="{escape(name)}">{mark}{caption}</a></li>'
    # One moving line under the hero (Carla, 3 Nov 2026): the list scrolls left and repeats; the
    # second copy only fills the loop. Hover pauses it; prefers-reduced-motion shows it still.
    return (f'<div class="programs-line"><span class="mono" id="programs-title">{escape(c["supported_heading"])}</span>'
            f'<div class="marquee"><ul class="program-list track" aria-labelledby="programs-title">{items}</ul>'
            f'<ul class="program-list track" aria-hidden="true">{items}</ul></div></div>')
def homepage(c):
    p=c['prefix']
    problems=''.join(f'<div class="card">{ICONS[i]}<h3>{t}</h3><p>{x}</p></div>' for i,t,x in c['problems'])
    verbs=''.join(f'<div class="verb"><h3>{ICONS[i]}{t}</h3><p>{x}</p></div>' for i,t,x in c['verbs'])
    learns=''.join(f'<div class="verb"><span class="learn-stage">{s}</span><h3>{t}</h3><p>{x}</p></div>' for s,t,x in c['learn_steps'])
    local_pts=''.join(f'<li>{s}</li>' for s in c['local_points'])
    hosted_pts=''.join(f'<li>{s}</li>' for s in c['hosted_points'])
    tiles=''.join(f'<div class="tile">{ICONS[i]}<h3>{t}</h3><p>{x}</p></div>' for i,t,x in c['tiles'])
    faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in c['faqs'])
    team=''.join(f'<li><a class="team-person" href="{url}" target="_blank" rel="noopener"><img src="/assets/{slug}.jpg" alt="" width="54" height="60" loading="lazy"><span><strong>{escape(name)}</strong><span class="team-role">{escape(en_role if p=="/" else pt_role)}</span></span><span class="team-arrow" aria-hidden="true">↗</span></a></li>' for name,slug,url,en_role,pt_role in TEAM)
    body=f'''<section class="wrap" aria-labelledby="hero-title"><div class="hero"><div class="hero-copy"><div class="eyebrow">{c['hero_eyebrow']}</div><h1 id="hero-title">{c['hero_title']}</h1><p class="hero-intro">{c['hero_intro']}</p><div class="hero-actions"><a class="button" href="{p}download/">{c['hero_primary']}</a><a class="button ghost" href="#how">{c['hero_secondary']}</a></div><p class="hero-sub">{c['hero_sub']} <a class="hero-code" href="{GITHUB}">{GITHUB_ICON}{c['hero_code']} <span aria-hidden="true">↗</span></a></p></div>{hero_demo(c)}</div><div class="hero-bottom"><span class="mono">{c['compatible']}</span><div class="compatibility"><span>Claude Desktop</span><span>Claude Code</span><span>Codex</span></div></div>{programs(c)}</section>
<section id="problem" class="section ice" aria-labelledby="problem-title"><div class="wrap"><div class="chapter-number">{c['ch_problem']}</div><div class="section-head"><h2 id="problem-title">{c['problem_title']}</h2></div><div class="card-row">{problems}</div></div></section>
<section id="how" class="section" aria-labelledby="how-title"><div class="wrap"><div class="chapter-number">{c['ch_how']}</div><div class="section-head"><h2 id="how-title">{c['how_title']}</h2><p class="section-lead">{c['how_lead']}</p></div><div class="card-row">{verbs}</div><div class="strip">{c['how_strip']}</div></div></section>
<section id="editions" class="band on-dark" aria-labelledby="edition-title"><div class="wrap"><div class="chapter-number">{c['ch_editions']}</div><div class="section-head"><h2 id="edition-title">{c['edition_title']}</h2><p class="section-lead">{c['edition_lead']}</p></div><div class="card-row"><article class="edition"><div class="edition-status">{c['local_status']}</div><h3>{c['local_title']}</h3><p>{c['local_body']}</p><ul>{local_pts}</ul><a class="button light" href="{p}download/">{c['local_cta']}</a><div class="fine">{c['local_fine']}</div></article><article class="edition"><div class="edition-status">{c['hosted_status']}</div><h3>{c['hosted_title']}</h3><p>{c['hosted_body']}</p><ul>{hosted_pts}</ul><a class="button light" href="{HOSTED_SIGNUP}{signup_lang(c['prefix'])}">{c['hosted_cta']}</a><div class="fine">{c['hosted_fine']}</div></article></div><p class="band-note">{c['band_note']}</p></div></section>
<section id="privacy-s" class="section ice" aria-labelledby="privacy-title"><div class="wrap"><div class="chapter-number">{c['ch_privacy']}</div><div class="section-head"><h2 id="privacy-title">{c['privacy_title']}</h2><p class="section-lead">{c['privacy_lead']}</p><a class="text-link code-link" href="{GITHUB}">{GITHUB_ICON}{c['privacy_code']} <span aria-hidden="true">↗</span></a></div><div class="card-row">{tiles}</div></div></section>
<section id="about" class="section" aria-labelledby="about-title"><div class="wrap"><div class="about"><img class="founder-photo" src="/assets/carla-centeno.jpg" alt="Carla Centeno" width="140" height="150" loading="lazy"><div class="founder-words"><span class="mono">{c['founder_eyebrow']}</span><h2 id="about-title">{c['founder_heading']}</h2><span class="founder-name">{c['founder_name']}</span></div><div class="about-description">{c['founder_description']}<br><a href="mailto:contact@memorysafe.ca">{c['contact']} ↗</a></div></div><div class="team-strip"><h3 class="mono" id="team-title">{escape(c['team_heading'])}</h3><ul class="team-list" aria-labelledby="team-title">{team}</ul></div></div></section>
<section class="section ice" aria-labelledby="faq-title"><div class="wrap faq"><div class="faq-title"><span class="mono">{c['faq_eyebrow']}</span><h2 id="faq-title">{c['faq_heading']}</h2></div><div class="faq-list">{faq}</div></div></section>
<section class="updates-mini"><div class="wrap"><div class="updates-box compact"><div class="compact-words"><span class="mono">{c['upd_label']}</span><h2>{c['upd_title']}</h2></div>{updates_form(c)}</div></div></section>'''
    return shell(c,'Stop re-explaining yourself to your AI' if p=='/' else 'Chega de se explicar de novo para a sua IA',body)

def download(c):
    p=c['prefix'];options=f'''<details class="install-option" open><summary>Claude Desktop</summary><div class="install-body"><a class="button" href="https://github.com/MemorySafe-Labs/memorysafe-plugin/releases/latest/download/memorysafe-claude-desktop.mcpb">{c['desktop_download']}</a><p>{c['desktop_steps']}</p></div></details>'''
    commands={'Codex':'codex plugin marketplace add MemorySafe-Labs/memorysafe-plugin\ncodex plugin add memorysafe@memorysafe','Claude Code':'claude plugin marketplace add MemorySafe-Labs/memorysafe-plugin\nclaude plugin install memorysafe@memorysafe'}
    for i,(name,command) in enumerate(commands.items()):
        options+=f'''<details class="install-option"><summary>{name}</summary><div class="install-body"><p>{c['terminal_intro']}</p><pre><code id="command-{i}">{command}</code></pre><button type="button" class="copy-command" data-copy="command-{i}">{c['copy']}</button><span class="copy-note" role="status"></span></div></details>'''
    body=f'''<div class="wrap"><section class="inner-hero"><div class="eyebrow">{c['download_eyebrow']}</div><h1>{c['download_title']}</h1><p>{c['download_intro']}</p></section><div class="download-layout"><div><div class="download-options">{options}</div><a class="text-link code-link source-link" href="{GITHUB}">{GITHUB_ICON}{c['source_code']} <span aria-hidden="true">↗</span></a><p class="download-legal">{c['download_legal']}</p><div class="updates-box"><span class="mono">{c['upd_label']}</span><h2>{c['upd_title']}</h2><p>{c['upd_body']}</p>{updates_form(c)}</div><nav class="footer-links"><a href="https://github.com/MemorySafe-Labs/memorysafe-plugin/releases/latest">{c['notes']} ↗</a><a href="https://github.com/MemorySafe-Labs/memorysafe-plugin/blob/main/PRIVACY.md">{c['product_privacy']} ↗</a><a href="https://github.com/MemorySafe-Labs/memorysafe-plugin/blob/main/TERMS.md">{c['terms']} ↗</a></nav></div><aside class="download-side"><span class="mono">{'After' if p=='/' else 'Depois'}</span><h2>{c['after_title']}</h2><p>{c['after_body']}</p><a class="text-link" href="http://127.0.0.1:8765/dashboard" target="_blank" rel="noopener">{c['dashboard']} ↗</a><p>{c['test_body']}</p><a class="text-link" href="/assets/memorysafe-install-guide-v0.4.23.png" target="_blank" rel="noopener">{c['guide']} ↗</a></aside></div></div>'''
    return shell(c,c['cta'],body,'download/')

def research(c):
    visual=render_research_visual('en' if c['prefix']=='/' else 'pt')
    cases=''.join(f'<div class="card case-card"><img class="case-img" src="/assets/{img}.png" alt="" width="1536" height="1024" loading="lazy"><h3>{t}</h3><p>{problem}</p><p class="case-action">{action}</p></div>' for img,t,problem,action in c['cases'])
    body=f'''<div class="wrap research-main"><section class="inner-hero"><div class="eyebrow">{c['research_eyebrow']}</div><h1>{c['research_page_title']}</h1><p>{c['research_page_intro']}</p></section>{visual}<section class="research-cases" aria-labelledby="cases-title"><div class="chapter-number">{c['cases_label']}</div><div class="section-head"><h2 id="cases-title">{c['cases_title']}</h2><p class="section-lead">{c['cases_lead']}</p></div><div class="card-row">{cases}</div></section><a class="button" href="mailto:contact@memorysafe.ca">{c['research_contact']}</a><p class="research-note">{c['research_note']}</p></div>'''
    return shell(c,c['nav'][3],body,'research/')

def value(c):
    v=c['value']
    def fields(fs,panel):
        return ''.join(f'<label class="v-field">{label}<input type="number" min="0" step="{step}" value="{default}" data-v="{key}" data-v-panel="{panel}"></label>' for key,label,default,step in fs)
    def outs(os_,panel):
        return ''.join(f'<div class="v-out"><span>{label}</span><strong data-vo="{key}">—</strong></div>' for key,label in os_)
    body=f'''<div class="wrap research-main"><section class="inner-hero"><div class="eyebrow">{v['eyebrow']}</div><h1>{v['title']}</h1><p>{v['intro']}</p></section>
<figure class="ms-film value-film" data-value data-hours="{v['hours']}"><div class="ms-film-top"><span class="mono">{v['film']}</span></div><ol class="ms-steps"><li><button type="button" class="demo-step" data-value-tab="1" aria-pressed="true"><span class="demo-step-number">01</span><span>{v['tab1']}</span></button></li><li><button type="button" class="demo-step" data-value-tab="2" aria-pressed="false"><span class="demo-step-number">02</span><span>{v['tab2']}</span></button></li></ol>
<div class="v-panel" data-value-panel="1"><p class="v-lead">{v['p1_lead']}</p><div class="value-grid">{fields(v['p1_fields'],1)}</div><div class="v-outs">{outs(v['p1_outs'],1)}</div><p class="v-formula">{v['p1_formula']}</p></div>
<div class="v-panel" data-value-panel="2" hidden><p class="v-lead">{v['p2_lead']}</p><div class="value-grid">{fields(v['p2_fields'],2)}</div><div class="v-outs">{outs(v['p2_outs'],2)}</div><p class="v-formula">{v['p2_formula']}</p></div>
<figcaption class="demo-note">{v['caption']}</figcaption></figure></div>'''
    return shell(c,c['nav'][4],body,'value/')

def pricing(c):
    p=c['prefix'];t=PRICING['pt' if p!='/' else 'en']
    def button(label,key,style):
        cls='button'+(' ghost' if style=='ghost' else '')
        if key=='download':
            return f'<a class="{cls}" href="{p}download/">{label}</a>'
        if key=='beta':
            return f'<a class="{cls}" href="{BETA}">{label}</a>'
        if key=='hosted':
            return f'<a class="{cls}" href="{HOSTED_SIGNUP}{signup_lang(p)}">{label}</a>'
        if key=='team':
            return f'<a class="{cls}" href="{HOSTED_TEAM_SIGNUP}{signup_lang(p)}">{label}</a>'
        if key=='test':
            return f'<a class="{cls}" href="{CONTACT}?subject=Fragility%20test">{label}</a>'
        if key=='contact':
            return f'<a class="{cls}" href="{CONTACT}">{label}</a>'
        if STRIPE[key]:
            return f'<a class="{cls}" href="{STRIPE[key]}">{label}</a>'
        return f'<span class="{cls} is-pending" aria-disabled="true" title="{t["pending"]}">{label}</span>'
    cards=[]
    for k in t['cards']:
        pts=''.join(f'<li>{x}</li>' for x in k['points'])
        btns=''.join(button(*b) for b in k['buttons'])
        per=f'<span class="price-per">{k["per"]}</span>' if k['per'] else ''
        fine=f'<p class="price-fine">{k["fine"]}</p>' if k['fine'] else ''
        featured=' featured' if k.get('featured') else ''
        cards.append(f'<article class="price-card{featured}"><div class="mono price-status">{k["status"]}</div><h2>{k["name"]}</h2><div class="price-line"><span class="price-amount">{k["price"]}</span>{per}</div><div class="price-actions">{btns}</div><p>{k["body"]}</p><h3 class="price-includes">{k["includes"]}</h3><ul class="check-list">{pts}</ul>{fine}</article>')
    you=''.join(cards[:2]); companies=''.join(cards[2:])
    body=f'<div class="wrap pricing-main"><section class="inner-hero"><div class="eyebrow">{t["eyebrow"]}</div><h1>{t["title"]}</h1><p>{t["intro"]}</p></section><div class="price-grid four">{you}{companies}</div><p class="price-note">{t["note"]}</p></div>'
    return shell(c,'Pricing' if p=='/' else 'Preços',body,'pricing/')

def thanks(c):
    body=f"""<div class="wrap"><section class="inner-hero"><div class="eyebrow">{c['upd_label']}</div><h1>{c['thanks_title']}</h1><p>{c['thanks_body']}</p><a class="button" href="{c['prefix']}download/">{c['thanks_back']}</a></section></div>"""
    return shell(c,c['thanks_title'],body,'download/thanks/')

def privacy(c):
    source=(OLD/('pt-br/privacy.html' if c['prefix']!='/' else 'privacy.html')).read_text()
    title=re.search(r'<h1>(.*?)</h1>',source,re.S).group(1)
    updated=re.search(r'<p class="updated">(.*?)</p>',source,re.S).group(1)
    content=re.search(r'<article class="content">(.*?)</article>',source,re.S).group(1)
    body=f'<div class="wrap"><section class="inner-hero"><div class="eyebrow">MEMORYSAFE LABS</div><h1>{title}</h1><p>{updated}</p></section><article class="legal-content">{content}</article></div>'
    return shell(c,title,body,'privacy/')

(PUBLIC/'site.js').write_text('''document.addEventListener('click',function(e){var b=e.target.closest('.copy-command');if(!b)return;var code=document.getElementById(b.dataset.copy);if(!code)return;navigator.clipboard.writeText(code.textContent).then(function(){var n=b.parentElement.querySelector('.copy-note');if(n){n.textContent=document.documentElement.lang.indexOf('pt')===0?'Copiado.':'Copied.';setTimeout(function(){n.textContent=''},2500)}})});

/* Hero demo: stepped, looping playback in the manner of the research animation —
   auto-plays while visible, pausable, step-selectable, stops offscreen,
   reduced-motion starts paused on the final frame. Purely illustrative; no data involved. */
(function(){
var demo=document.querySelector('[data-memory-demo]');if(!demo)return;
var ids=['u1','a1','fact','u2','a2','chip'],msgs={};
ids.forEach(function(k){msgs[k]=demo.querySelector('[data-demo-msg="'+k+'"]')});
var cards={1:demo.querySelector('[data-demo-card="1"]'),2:demo.querySelector('[data-demo-card="2"]'),3:demo.querySelector('[data-demo-card="3"]')};
var steps=[].slice.call(demo.querySelectorAll('[data-demo-step]'));
var playBtn=demo.querySelector('[data-demo-play]');
var phases=[{s:1,m:['u1']},{s:2,m:['u1','a1','fact']},{s:3,m:['u1','a1','fact','u2']},{s:3,m:['u1','a1','fact','u2','chip']},{s:3,m:['u1','a1','fact','u2','chip','a2']}];
var hold=[2400,2400,1600,1000,5600];
var i=0,timer=null,userPaused=false,visible=true;
var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function apply(n){i=n;var p=phases[n];demo.dataset.stage=p.s;
ids.forEach(function(k){if(msgs[k])msgs[k].classList.toggle('shown',p.m.indexOf(k)>-1)});
[1,2,3].forEach(function(s){if(cards[s])cards[s].classList.toggle('active',p.s===s)});
steps.forEach(function(b){b.setAttribute('aria-pressed',String(+b.getAttribute('data-demo-step')===p.s))})}
function stop(){if(timer){clearTimeout(timer);timer=null}}
function tick(){timer=setTimeout(function(){apply((i+1)%phases.length);tick()},hold[i])}
function playing(){return !!timer}
function ui(){if(!playBtn)return;var on=playing();demo.classList.toggle('is-playing',on);
var g=playBtn.querySelector('[data-demo-icon]');if(g)g.textContent=on?'\\u2161':'\\u25B6';
var t=playBtn.getAttribute(on?'data-pause':'data-play');
var l=playBtn.querySelector('[data-demo-label]');if(l)l.textContent=t;
playBtn.setAttribute('aria-label',t);
playBtn.setAttribute('aria-pressed',String(!on))}
function maybeRun(){stop();if(!userPaused&&visible&&!document.hidden)tick();ui()}
if(playBtn){playBtn.hidden=false;playBtn.addEventListener('click',function(){userPaused=playing();if(userPaused)stop();else maybeRun();ui()})}
steps.forEach(function(b){b.addEventListener('click',function(){userPaused=true;stop();apply(+b.getAttribute('data-demo-step')===1?0:(+b.getAttribute('data-demo-step')===2?1:4));ui()})});
if('IntersectionObserver' in window){new IntersectionObserver(function(es){visible=es[0].isIntersecting;maybeRun()},{threshold:.25}).observe(demo)}
document.addEventListener('visibilitychange',maybeRun);
if(reduce){userPaused=true;apply(4);ui()}else{apply(0);maybeRun()}
})();

/* Value page: two small planning models. Simple arithmetic on the visitor's own numbers;
   mirrors the memorysafe.ca simulator's middle (50%) and 30% what-if scenarios. */
(function(){
var root=document.querySelector('[data-value]');if(!root)return;
var lang=document.documentElement.lang||'en-CA';
var hoursWord=root.getAttribute('data-hours')||'hrs';
var nf=new Intl.NumberFormat(lang,{maximumFractionDigits:0});
var cf=new Intl.NumberFormat(lang,{style:'currency',currency:'CAD',maximumFractionDigits:0});
function num(key){var el=root.querySelector('[data-v="'+key+'"]');var n=el?parseFloat(el.value):0;return isFinite(n)&&n>0?n:0}
function put(key,text){var el=root.querySelector('[data-vo="'+key+'"]');if(el)el.textContent=text}
function calc(){
var lost=num('people')*num('minutes')*52/60;
put('lost',nf.format(Math.round(lost))+' '+hoursWord);
put('returned',nf.format(Math.round(lost*.5))+' '+hoursWord);
put('value',cf.format(Math.round(lost*.5*num('rate'))));
var avoided=num('runs')*num('mins')*365*.3/60;
put('avoided',nf.format(Math.round(avoided))+' '+hoursWord);
put('gross',cf.format(Math.round(avoided*num('cost'))));
}
root.addEventListener('input',calc);
var tabs=[].slice.call(root.querySelectorAll('[data-value-tab]'));
tabs.forEach(function(b){b.addEventListener('click',function(){
tabs.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
[].slice.call(root.querySelectorAll('[data-value-panel]')).forEach(function(pn){pn.hidden=pn.getAttribute('data-value-panel')!==b.getAttribute('data-value-tab')})})});
calc();
})();
''')

for locale,c in COPY.items():
    root=PUBLIC/('pt-br' if locale=='pt' else '')
    root.mkdir(parents=True,exist_ok=True)
    (root/'index.html').write_text(homepage(c))
    for slug,builder in [('download',download),('download/thanks',thanks),('research',research),('value',value),('pricing',pricing),('privacy',privacy)]:
        (root/slug).mkdir(parents=True,exist_ok=True)
        (root/slug/'index.html').write_text(builder(c))

# Favicon: v7 small-size rule — untilted 3×3, pale third column.
(PUBLIC/'assets/mark.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#0e1420"/>'+''.join(f'<circle cx="{8+x*12}" cy="{8+y*12}" r="4" fill="{["#3b82f6","#93c5fd","#e0f2fe"][x]}"/>' for x in range(3) for y in range(3))+'</svg>')
(PUBLIC/'robots.txt').write_text('User-agent: *\nAllow: /\n')
used={b[1] for lang in PRICING.values() for card in lang['cards'] for b in card['buttons']}
missing=[k for k,v in STRIPE.items() if not v and k in used]
print('Built ten local pages (Claudete concept). No deployment or network access.')
if missing: print('Stripe Payment Links not set yet, buttons disabled:', ', '.join(missing))
test_links=[k for k,v in STRIPE.items() if '/test_' in v]
if test_links: print('Stripe TEST links in use, do not deploy:', ', '.join(test_links))
