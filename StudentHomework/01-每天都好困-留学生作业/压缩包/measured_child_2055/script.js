const $ = (s, c=document) => c.querySelector(s);
const $$ = (s, c=document) => [...c.querySelectorAll(s)];

function goTo(id){
  const el = document.getElementById(id);
  if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
}

$$('[data-target]').forEach(btn => btn.addEventListener('click', () => goTo(btn.dataset.target)));

$('#scanCard').addEventListener('click', () => {
  $('#identityCard').classList.remove('hidden');
  $('#scanCard').textContent = 'Identity Confirmed';
  $('#scanCard').disabled = true;
});

$$('.credit-card').forEach(btn => btn.addEventListener('click', () => {
  $$('.credit-card').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  $('#creditDetail').textContent = btn.dataset.detail;
}));

$$('.score-row').forEach(btn => btn.addEventListener('click', () => {
  $('#scoreNote').textContent = btn.dataset.note;
}));

$$('#moodChoices button').forEach(btn => btn.addEventListener('click', () => {
  $$('#moodChoices button').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  const mood = btn.dataset.value;
  const impacts = {
    Calm:'Stable condition recorded. No score adjustment.',
    Tired:'Fatigue recorded. Attention forecast reduced by 3%.',
    Anxious:'Risk marker added. Scholarship stability may be reviewed.',
    Angry:'Emotional warning recorded. Human teacher notified.'
  };
  $('#moodResult').textContent = `SYSTEM: ${impacts[mood]}`;
}));

let focusTimer;
$('#focusTest').addEventListener('click', () => {
  const btn = $('#focusTest');
  btn.disabled = true;
  let n = 5;
  $('#focusResult').textContent = `Keep this page active: ${n}`;
  focusTimer = setInterval(() => {
    n--;
    if(n > 0) $('#focusResult').textContent = `Keep this page active: ${n}`;
    else {
      clearInterval(focusTimer);
      const score = Math.floor(70 + Math.random()*25);
      $('#focusResult').textContent = `Focus test complete. Attention sample: ${score}/100. Hesitation data stored.`;
      btn.disabled = false;
      btn.textContent = 'Repeat Focus Test';
    }
  },1000);
});

$$('#activityChoices button').forEach(btn => btn.addEventListener('click', () => {
  $$('#activityChoices button').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
  const v = btn.dataset.value;
  const out = {
    'Community Service':'+8 Community Credits. Scholarship probability rises to 84%.',
    'Care for Brother':'+3 provisional Care Credits. Verification pending.',
    'Animation':'No official credits. Creativity portfolio updated privately.'
  };
  $('#activityResult').textContent = `SELECTED: ${v}. ${out[v]}`;
}));

$('#openMessages').addEventListener('click', () => goTo('messages'));

$$('.message-tab').forEach(tab => tab.addEventListener('click', () => {
  $$('.message-tab').forEach(t => t.classList.remove('active'));
  $$('.message-content').forEach(m => m.classList.remove('active'));
  tab.classList.add('active');
  $('#' + tab.dataset.message).classList.add('active');
}));

const endings = {
  accept:{
    title:'Ending One — Accept the System',
    system:'PATHWAY ACCEPTED. RISK REDUCED. FUTURE SECURED.',
    text:'Lina accepts the Health Data Management pathway. Her scholarship is confirmed and her risk level falls. The system removes her animation portfolio from the main profile because it is not relevant to her approved future.',
    quote:'“I know this is the safest choice. I just do not know if it is mine.”'
  },
  review:{
    title:'Ending Two — Request Human Review',
    system:'HUMAN REVIEW REQUESTED. ESTIMATED WAIT: 14 MONTHS. OPPORTUNITY STATUS: LIMITED.',
    text:'Lina asks for a human review. Her scholarship remains uncertain while a teacher and government officer examine her case. She may submit her animation portfolio, but the process is slow.',
    quote:'“Maybe a person will understand what the numbers missed. I hope I can wait that long.”'
  },
  unmeasured:{
    title:'Ending Three — Become Unmeasured',
    system:'PROFILE INCOMPLETE. FUTURE PREDICTION UNAVAILABLE. EDUCATIONAL ACCESS MAY BE RESTRICTED.',
    text:'Lina deletes part of her personal data and joins the Right to Be Unmeasured movement. She gains more privacy, but loses access to some scholarships, AI tutoring services and official career predictions.',
    quote:'“For the first time, the system cannot tell me who I should become. That freedom is frightening, but it is still freedom.”'
  }
};

$$('.ending-choice').forEach(btn => btn.addEventListener('click', () => {
  const e = endings[btn.dataset.ending];
  $('#endingOutput').innerHTML = `<h3>${e.title}</h3><div class="system-lines">${e.system}</div><p>${e.text}</p><blockquote>${e.quote}</blockquote><button class="primary-btn" id="continueReflection">Continue to Reflection</button>`;
  $('#endingOutput').classList.remove('hidden');
  $('#continueReflection').addEventListener('click', () => goTo('reflection'));
}));

let seconds = 300;
setInterval(() => {
  if(seconds > 0) seconds--;
  const m = String(Math.floor(seconds/60)).padStart(2,'0');
  const s = String(seconds%60).padStart(2,'0');
  $('#countdown').textContent = `${m}:${s}`;
},1000);

const audio = $('#ambientAudio');
let audioOn = false;
$('#audioToggle').addEventListener('click', async () => {
  try{
    if(!audioOn){ await audio.play(); audioOn = true; $('#audioToggle').textContent='🔇'; }
    else{ audio.pause(); audioOn = false; $('#audioToggle').textContent='🔊'; }
  }catch(e){ console.warn(e); }
});

$('#privacyToggle').addEventListener('click', () => {
  document.body.classList.toggle('privacy-active');
  $('#privacyToggle').textContent = document.body.classList.contains('privacy-active') ? 'Exit Privacy Mode' : 'Privacy Mode';
});

$('#restart').addEventListener('click', () => location.reload());
