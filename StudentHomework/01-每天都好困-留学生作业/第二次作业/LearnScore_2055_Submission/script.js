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
  resultGenerated: false,
  resultRequested: false,
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
  select('span', audioToggle).textContent = enabled ? 'Sound on' : 'Sound off';
  select('img', audioToggle).src = enabled
    ? 'assets/icons/speaker-simple-high.svg'
    : 'assets/icons/speaker-simple-slash.svg';

  if (enabled) {
    try {
      await ambientAudio.play();
      playTone('confirm');
    } catch (error) {
      state.soundOn = false;
      audioToggle.setAttribute('aria-pressed', 'false');
      select('span', audioToggle).textContent = 'Sound off';
      select('img', audioToggle).src = 'assets/icons/speaker-simple-slash.svg';
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
  select('span', privacyToggle).textContent = isPrivate ? 'Exit privacy mode' : 'Privacy mode';
  select('img', privacyToggle).src = isPrivate
    ? 'assets/icons/eye-slash.svg'
    : 'assets/icons/eye.svg';
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
const accessMessage = select('#access-message');
const scanLabel = select('.scan-label', scanCard);
const cardStatus = select('#card-status');

scanCard.addEventListener('click', () => {
  if (state.accessed) {
    const record = select('#record');
    record.scrollIntoView({ behavior: 'smooth', block: 'start' });
    window.setTimeout(() => select('[data-score-note]', record)?.focus({ preventScroll: true }), 550);
    return;
  }

  scanCard.disabled = true;
  scanCard.setAttribute('aria-busy', 'true');
  scanCard.classList.add('is-scanning');
  scanLabel.textContent = 'Reading identity…';
  accessMessage.textContent = 'Matching the card to the permanent learner record…';
  cardStatus.innerHTML = 'Scanning<br>identity';
  playTone('data');

  window.setTimeout(() => {
    state.accessed = true;
    scanCard.disabled = false;
    scanCard.removeAttribute('aria-busy');
    scanCard.classList.remove('is-scanning');
    scanCard.classList.add('is-confirmed');
    scanLabel.textContent = 'Identity confirmed';
    accessMessage.textContent = 'Match found. Click again to open Lina\u2019s ability record.';
    cardStatus.innerHTML = 'Identity<br>matched';
    accessResult.classList.add('is-confirmed');
    scanCard.focus({ preventScroll: true });
    playTone('confirm');
  }, 1050);
});

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
    handleReviewChange();
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
    handleReviewChange();
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
  handleReviewChange();
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

const reviewerProfiles = {
  accept: {
    code: 'AUDIT RESULT // COMPLIANCE PRIORITISED',
    title: 'Stability-first reviewer',
    summary: 'You protected Lina’s scholarship by accepting the system’s safest forecast.'
  },
  review: {
    code: 'AUDIT RESULT // MODEL CHALLENGED',
    title: 'Context-first reviewer',
    summary: 'You delayed certainty to make space for testimony the score excluded.'
  },
  unmeasured: {
    code: 'AUDIT RESULT // AUTONOMY PRIORITISED',
    title: 'Autonomy-first reviewer',
    summary: 'You valued privacy and uncertainty over guaranteed institutional access.'
  }
};

const moodAudit = {
  Calm: 'treated one calm check-in as reliable evidence',
  Fatigued: 'converted exhaustion into reduced attention',
  Anxious: 'translated anxiety into scholarship risk',
  Angry: 'turned anger into a permanent red flag',
  Skipped: 'recorded refusal as non-compliance'
};

const activityAudit = {
  'Community maintenance': 'rewarded a visible public contribution',
  'Care for younger brother': 'recognised care only after demanding adult proof',
  'Animation portfolio': 'preserved an ambition the official pathway does not credit'
};

const receiptStatus = select('#receipt-status');
const receiptProgress = select('#receipt-progress');
const receiptProgressTrack = select('.receipt-progress');
const generatedResult = select('#generated-result');
const resultCode = select('#result-code');
const resultTitle = select('#result-title');
const resultCopy = select('#result-copy');
const generateResult = select('#generate-result');

function reviewCompletion() {
  const missing = [];
  if (!state.mood) missing.push({ label: 'choose an emotion', target: '#mood-choices button' });
  if (!state.activity) missing.push({ label: 'allocate an activity', target: '#activity-choices button' });
  if (state.openedMessages.size < 4) {
    const unopened = messageTabs.find((tab) => !state.openedMessages.has(tab.dataset.message));
    missing.push({ label: `open ${4 - state.openedMessages.size} more testimony record${state.openedMessages.size === 3 ? '' : 's'}`, target: unopened ? `#${unopened.id}` : '#testimony' });
  }
  if (!state.ending) missing.push({ label: 'choose a pathway', target: '#ending-choices button' });

  return { missing, completed: 4 - missing.length, complete: missing.length === 0 };
}

function setReceiptValue(selector, text, pending) {
  const button = select(selector);
  button.textContent = text;
  button.classList.toggle('is-pending', pending);
}

function updateReviewProgress() {
  const review = reviewCompletion();
  const percentage = review.completed * 25;

  receiptStatus.textContent = `${review.completed} / 4 steps complete`;
  receiptProgress.style.width = `${percentage}%`;
  receiptProgressTrack.setAttribute('aria-valuenow', String(review.completed));
  setReceiptValue('#receipt-mood', state.mood ? `${state.mood} ↗` : 'Choose emotion ↗', !state.mood);
  setReceiptValue('#receipt-activity', state.activity ? `${state.activity} ↗` : 'Allocate activity ↗', !state.activity);
  setReceiptValue('#receipt-evidence', state.openedMessages.size === 4 ? '4 of 4 · complete ↗' : `${state.openedMessages.size} of 4 · open records ↗`, state.openedMessages.size < 4);
  setReceiptValue('#receipt-ending', state.ending ? `${endings[state.ending].label} ↗` : 'Choose pathway ↗', !state.ending);

  select('#reflection-status').textContent = review.complete
    ? 'Case closed // reviewer audit generated'
    : 'Review in progress // reviewer audit';
  generateResult.textContent = review.complete ? 'Reviewer result generated · refresh' : 'Check missing steps';

  const continueButton = select('#continue-reflection');
  if (continueButton) {
    continueButton.textContent = review.complete
      ? 'Close case and view generated audit'
      : 'Complete review and generate audit';
  }

  return review;
}

function showIncompleteResult(review, guide = false) {
  state.resultGenerated = false;
  state.resultRequested = true;
  generatedResult.classList.add('is-incomplete');
  resultCode.textContent = 'RESULT INCOMPLETE';
  resultTitle.textContent = `${review.missing.length} review step${review.missing.length === 1 ? '' : 's'} still required.`;
  resultCopy.textContent = `To generate the audit, ${review.missing.map((item) => item.label).join('; ')}.`;

  if (!guide || review.missing.length === 0) return;
  showToast(`Audit incomplete: ${review.missing[0].label}.`);
  const target = select(review.missing[0].target);
  if (target) {
    window.setTimeout(() => {
      target.scrollIntoView({ behavior: 'smooth', block: 'center' });
      window.setTimeout(() => target.focus?.({ preventScroll: true }), 550);
    }, 180);
  }
}

function renderReviewerResult({ announce = false, guide = false } = {}) {
  const review = updateReviewProgress();
  if (!review.complete) {
    showIncompleteResult(review, guide);
    return false;
  }

  const profile = reviewerProfiles[state.ending];
  generatedResult.classList.remove('is-incomplete');
  resultCode.textContent = profile.code;
  resultTitle.textContent = profile.title;
  resultCopy.textContent = `${profile.summary} Your audit ${moodAudit[state.mood]} and ${activityAudit[state.activity]}.`;
  state.resultGenerated = true;
  state.resultRequested = true;
  if (announce) showToast('Reviewer audit generated from all four steps.');
  return true;
}

function handleReviewChange() {
  const review = updateReviewProgress();
  if (review.complete) {
    renderReviewerResult({ announce: !state.resultGenerated });
  } else if (state.resultGenerated || state.resultRequested) {
    showIncompleteResult(review);
  }
}

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
    handleReviewChange();
    select('#continue-reflection').addEventListener('click', () => {
      if (!renderReviewerResult({ announce: true, guide: true })) return;
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

const receiptFocusTargets = {
  'receipt-mood': '#mood-choices button',
  'receipt-activity': '#activity-choices button',
  'receipt-evidence': '.message-tab',
  'receipt-ending': '#ending-choices button'
};

selectAll('[data-jump]').forEach((button) => {
  button.addEventListener('click', () => {
    const target = select(button.dataset.jump);
    if (!target) return;
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    const focusTarget = select(receiptFocusTargets[button.id]);
    window.setTimeout(() => focusTarget?.focus({ preventScroll: true }), 550);
  });
});

generateResult.addEventListener('click', () => {
  const generated = renderReviewerResult({ announce: true, guide: true });
  if (generated) generatedResult.scrollIntoView({ behavior: 'smooth', block: 'center' });
});

updateReviewProgress();

select('#restart-case').addEventListener('click', () => {
  ambientAudio.pause();
  window.location.reload();
});
