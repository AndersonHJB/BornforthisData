/*
  LEARNSCORE 2055 — interaction controller
  The page stores choices only in memory. Nothing is transmitted or retained.
*/

'use strict';

const select = (selector, context = document) => context.querySelector(selector);
const selectAll = (selector, context = document) => [...context.querySelectorAll(selector)];

const state = {
  soundOn: false,
  accessed: false,
  mood: null,
  activity: null,
  ending: null,
  openedMessages: new Set(['teacher'])
};

const ambientAudio = select('#ambient-audio');
const orientationVideo = select('#orientation-video');
const audioToggle = select('#audio-toggle');
const privacyToggle = select('#privacy-toggle');
const toast = select('#toast');
let audioContext;
let toastTimer;
let resumeAmbientAfterVideo = false;

ambientAudio.volume = 0.22;

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('is-visible');
  window.clearTimeout(toastTimer);
  toastTimer = window.setTimeout(() => toast.classList.remove('is-visible'), 2600);
}

/* Short procedural tones reinforce system feedback without carrying unique information. */
function playTone(type = 'confirm') {
  if (!state.soundOn) return;

  const AudioContextClass = window.AudioContext || window.webkitAudioContext;
  if (!AudioContextClass) return;
  audioContext ||= new AudioContextClass();

  const patterns = {
    confirm: [440, 660],
    data: [320],
    risk: [180, 135],
    message: [560, 720],
    decision: [260, 390, 520]
  };
  const frequencies = patterns[type] || patterns.confirm;
  const now = audioContext.currentTime;

  frequencies.forEach((frequency, index) => {
    const oscillator = audioContext.createOscillator();
    const gain = audioContext.createGain();
    const start = now + index * 0.09;
    oscillator.type = type === 'risk' ? 'sawtooth' : 'sine';
    oscillator.frequency.value = frequency;
    gain.gain.setValueAtTime(0.0001, start);
    gain.gain.exponentialRampToValueAtTime(0.045, start + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.0001, start + 0.16);
    oscillator.connect(gain).connect(audioContext.destination);
    oscillator.start(start);
    oscillator.stop(start + 0.18);
  });
}

async function setSound(enabled) {
  state.soundOn = enabled;
  audioToggle.setAttribute('aria-pressed', String(enabled));
  audioToggle.lastChild.textContent = enabled ? ' Sound on' : ' Sound off';

  if (enabled) {
    try {
      await ambientAudio.play();
      playTone('confirm');
    } catch (error) {
      state.soundOn = false;
      audioToggle.setAttribute('aria-pressed', 'false');
      audioToggle.lastChild.textContent = ' Sound off';
      showToast('Your browser blocked audio. Press Sound on once more.');
    }
  } else {
    ambientAudio.pause();
  }
}

audioToggle.addEventListener('click', () => setSound(!state.soundOn));

privacyToggle.addEventListener('click', () => {
  const isPrivate = document.body.classList.toggle('privacy-active');
  privacyToggle.setAttribute('aria-pressed', String(isPrivate));
  privacyToggle.textContent = isPrivate ? 'Exit privacy mode' : 'Privacy mode';
  showToast(isPrivate ? 'Protected records obscured.' : 'Protected records restored.');
});

/* Pause the ambient bed while the embedded film is using its own audio track. */
orientationVideo.addEventListener('play', () => {
  resumeAmbientAfterVideo = state.soundOn && !ambientAudio.paused;
  if (resumeAmbientAfterVideo) ambientAudio.pause();
});

function resumeAmbient() {
  if (resumeAmbientAfterVideo && state.soundOn) ambientAudio.play().catch(() => {});
  resumeAmbientAfterVideo = false;
}

orientationVideo.addEventListener('pause', resumeAmbient);
orientationVideo.addEventListener('ended', resumeAmbient);

/* Access-card reveal: the first authored interaction in the narrative. */
const scanCard = select('#scan-card');
const accessResult = select('#access-result');
const openCase = select('#open-case');

scanCard.addEventListener('click', () => {
  if (state.accessed) return;
  scanCard.disabled = true;
  scanCard.classList.add('is-scanning');
  scanCard.lastChild.textContent = ' Reading identity…';
  accessResult.textContent = 'SCANNING // Matching permanent learner record…';
  playTone('data');

  window.setTimeout(() => {
    state.accessed = true;
    scanCard.classList.remove('is-scanning');
    scanCard.lastChild.textContent = ' Identity confirmed';
    accessResult.textContent = 'MATCH FOUND // Lina Chen // Development Path Review Pending';
    accessResult.classList.add('is-confirmed');
    openCase.classList.remove('is-hidden');
    openCase.focus();
    playTone('confirm');
  }, 1050);
});

openCase.addEventListener('click', () => select('#promise').scrollIntoView({ behavior: 'smooth' }));

/* Explain how the official system translates behaviour into a score. */
const measureOutput = select('#measure-output');
selectAll('[data-measure]').forEach((button) => {
  button.addEventListener('click', () => {
    selectAll('[data-measure]').forEach((item) => item.classList.remove('is-selected'));
    button.classList.add('is-selected');
    measureOutput.textContent = `SYSTEM RULE // ${button.dataset.measure}`;
    playTone('data');
  });
});

/* Each visible score can be audited for the assumption behind it. */
selectAll('[data-score-note]').forEach((button) => {
  button.addEventListener('click', () => {
    select('#score-note').textContent = `EVIDENCE NOTE // ${button.dataset.scoreNote}`;
    playTone('data');
  });
});

const moodImpacts = {
  Calm: 'Stable state recorded. No score adjustment.',
  Fatigued: 'Attention reduced by 3%. Break extended by five minutes.',
  Anxious: 'Risk marker added. Scholarship stability may be affected.',
  Angry: 'Red flag added. Teacher and guardian notified.',
  Skipped: 'Non-compliance recorded. Predictive confidence reduced.'
};

const attentionScore = select('#attention-score');
const emotionScore = select('#emotion-score');
const attentionBar = select('#attention-bar');
const emotionBar = select('#emotion-bar');
const moodResult = select('#mood-result');

selectAll('#mood-choices button').forEach((button) => {
  button.addEventListener('click', () => {
    selectAll('#mood-choices button').forEach((item) => item.classList.remove('is-selected'));
    button.classList.add('is-selected');
    state.mood = button.dataset.mood;

    const newAttention = Number(button.dataset.attention);
    const newEmotion = Number(button.dataset.emotion);
    attentionScore.textContent = String(newAttention);
    emotionScore.textContent = String(newEmotion);
    attentionBar.style.setProperty('--score', `${newAttention}%`);
    emotionBar.style.setProperty('--score', `${newEmotion}%`);
    moodResult.textContent = `SYSTEM RECORDED // ${moodImpacts[state.mood]}`;
    moodResult.classList.toggle('is-risk', !['Calm', 'Fatigued'].includes(state.mood));
    select('#receipt-mood').textContent = state.mood;
    playTone(['Anxious', 'Angry', 'Skipped'].includes(state.mood) ? 'risk' : 'data');
  });
});

const activityImpacts = {
  'Community maintenance': '+8 Community and +2 Teamwork. Scholarship ranking rises.',
  'Care for younger brother': '+3 provisional Care. Adult verification remains pending.',
  'Animation portfolio': '0 official credits. A private, unverified portfolio is created.'
};

selectAll('#activity-choices button').forEach((button) => {
  button.addEventListener('click', () => {
    selectAll('#activity-choices button').forEach((item) => item.classList.remove('is-selected'));
    button.classList.add('is-selected');
    state.activity = button.dataset.activity;
    select('#activity-result').textContent = `ACTIVITY ALLOCATED // ${activityImpacts[state.activity]}`;
    select('#receipt-activity').textContent = state.activity;
    playTone(state.activity === 'Animation portfolio' ? 'risk' : 'confirm');
  });
});

/* Tabbed testimony preserves keyboard navigation and tracks what the reviewer opened. */
const messageTabs = selectAll('.message-tab');

function openMessage(tab) {
  messageTabs.forEach((item) => {
    const active = item === tab;
    item.classList.toggle('is-active', active);
    item.setAttribute('aria-selected', String(active));
    item.tabIndex = active ? 0 : -1;
  });

  selectAll('.message-panel').forEach((panel) => {
    const active = panel.id === `message-${tab.dataset.message}`;
    panel.hidden = !active;
    panel.classList.toggle('is-active', active);
  });

  state.openedMessages.add(tab.dataset.message);
  const count = state.openedMessages.size;
  select('#evidence-count').textContent = `${count} / 4 opened`;
  select('#evidence-fill').style.width = `${count * 25}%`;
  select('#receipt-evidence').textContent = `${count} of 4`;
  playTone('message');
  if (count === 4) showToast('Contested record complete. Four incompatible truths retained.');
}

messageTabs.forEach((tab, index) => {
  tab.addEventListener('click', () => openMessage(tab));
  tab.addEventListener('keydown', (event) => {
    if (!['ArrowDown', 'ArrowRight', 'ArrowUp', 'ArrowLeft'].includes(event.key)) return;
    event.preventDefault();
    const direction = ['ArrowDown', 'ArrowRight'].includes(event.key) ? 1 : -1;
    const nextIndex = (index + direction + messageTabs.length) % messageTabs.length;
    messageTabs[nextIndex].focus();
    openMessage(messageTabs[nextIndex]);
  });
});

const endings = {
  accept: {
    label: 'Recommendation accepted',
    system: 'PATHWAY ACCEPTED // SCHOLARSHIP CONFIRMED // RISK MARKER CLEARED',
    title: 'The safest future',
    text: 'Lina enters Health Data Management. Her animations move to a non-relevant archive because they do not support her approved path.',
    quote: '“I know this is the safest choice. I just do not know whether it is mine.”'
  },
  review: {
    label: 'Human review requested',
    system: 'APPEAL SUBMITTED // ESTIMATED WAIT 14 MONTHS // OPPORTUNITY STATUS RESTRICTED',
    title: 'A future placed on hold',
    text: 'Ms Ward’s statement and Lina’s portfolio enter a government queue. Her scholarship remains uncertain while a person reviews what the scores excluded.',
    quote: '“Maybe a person can understand what the numbers missed. I hope my future can wait.”'
  },
  unmeasured: {
    label: 'Optional data withdrawn',
    system: 'PROFILE INCOMPLETE // PUBLIC SERVICES SUSPENDED // FUTURE CANNOT BE GUARANTEED',
    title: 'The right to be unpredictable',
    text: 'Lina disconnects optional personal data and joins the Right to Be Unmeasured. Existing records remain, but tutoring, placement and scholarship access are suspended.',
    quote: '“For the first time, the system cannot tell me who I should become. The freedom is frightening, but it is still freedom.”'
  }
};

const endingOutput = select('#ending-output');

function contextualConsequence() {
  const mood = state.mood
    ? `You classified Lina as ${state.mood.toLowerCase()}.`
    : 'You left Lina’s emotional state unclassified.';
  const activity = state.activity
    ? `You allocated ${state.activity.toLowerCase()}.`
    : 'You did not allocate an after-school activity.';
  return `${mood} ${activity} Both actions remain in the review history.`;
}

selectAll('#ending-choices button').forEach((button) => {
  button.addEventListener('click', () => {
    selectAll('#ending-choices button').forEach((item) => item.classList.remove('is-selected'));
    button.classList.add('is-selected');
    state.ending = button.dataset.ending;
    const ending = endings[state.ending];

    endingOutput.innerHTML = `
      <div class="system-line">${ending.system}</div>
      <h3>${ending.title}</h3>
      <p>${ending.text}</p>
      <p>${contextualConsequence()}</p>
      <blockquote>${ending.quote}</blockquote>
      <button class="secondary-button" id="continue-reflection" type="button">Close case and view reviewer audit</button>
    `;
    endingOutput.classList.remove('is-hidden');
    select('#receipt-ending').textContent = ending.label;
    select('#continue-reflection').addEventListener('click', () => {
      select('#reflection').scrollIntoView({ behavior: 'smooth' });
    });
    playTone(state.ending === 'accept' ? 'confirm' : state.ending === 'review' ? 'decision' : 'risk');
    window.setTimeout(() => endingOutput.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 80);
  });
});

/* The five-minute review clock begins only when the final decision comes into view. */
let countdownStarted = false;
let countdownSeconds = 300;
let countdownTimer;

function startCountdown() {
  if (countdownStarted) return;
  countdownStarted = true;
  countdownTimer = window.setInterval(() => {
    countdownSeconds = Math.max(0, countdownSeconds - 1);
    const minutes = String(Math.floor(countdownSeconds / 60)).padStart(2, '0');
    const seconds = String(countdownSeconds % 60).padStart(2, '0');
    select('#countdown').textContent = `${minutes}:${seconds}`;
    if (countdownSeconds === 0) {
      window.clearInterval(countdownTimer);
      showToast('Decision window held open for accessibility. No option has been removed.');
    }
  }, 1000);
}

const decisionObserver = new IntersectionObserver((entries) => {
  if (entries.some((entry) => entry.isIntersecting)) startCountdown();
}, { threshold: 0.25 });
decisionObserver.observe(select('#decision'));

/* Full-size artefact viewer for the student's original hand-drawn materials. */
const artifactDialog = select('#artifact-dialog');
const artifactDialogImage = select('#artifact-dialog-image');

selectAll('[data-image]').forEach((button) => {
  button.addEventListener('click', () => {
    artifactDialogImage.src = button.dataset.image;
    artifactDialogImage.alt = button.dataset.alt;
    select('#artifact-dialog-title').textContent = button.dataset.alt;
    artifactDialog.showModal();
  });
});

select('#close-artifact').addEventListener('click', () => artifactDialog.close());
artifactDialog.addEventListener('click', (event) => {
  if (event.target === artifactDialog) artifactDialog.close();
});

/* Scroll progress, active navigation and gentle reveals. */
function updateReadingProgress() {
  const scrollable = document.documentElement.scrollHeight - window.innerHeight;
  const progress = scrollable > 0 ? (window.scrollY / scrollable) * 100 : 0;
  select('#reading-progress').style.width = `${Math.min(100, Math.max(0, progress))}%`;
}

window.addEventListener('scroll', updateReadingProgress, { passive: true });
updateReadingProgress();

const revealObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.classList.add('is-visible');
    observer.unobserve(entry.target);
  });
}, { rootMargin: '0px 0px -9% 0px', threshold: 0.08 });

selectAll('.reveal').forEach((element) => revealObserver.observe(element));

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    selectAll('[data-nav]').forEach((link) => {
      link.classList.toggle('is-current', link.dataset.nav === entry.target.id);
    });
  });
}, { rootMargin: '-35% 0px -55% 0px', threshold: 0 });

selectAll('[data-section]').forEach((section) => sectionObserver.observe(section));

select('#restart-case').addEventListener('click', () => {
  ambientAudio.pause();
  window.location.reload();
});

