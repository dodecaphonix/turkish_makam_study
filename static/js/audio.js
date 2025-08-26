    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    let audioBuffer;

    async function loadSound(url) {
        const response = await fetch(url);
        const arrayBuffer = await response.arrayBuffer();
        audioBuffer = await audioContext.decodeAudioData(arrayBuffer);
    }

    function playSound(pitchShiftSemitones, pitchShiftCommas) {
        if (!audioBuffer) return;

        const source = audioContext.createBufferSource();
        source.buffer = audioBuffer;

        // Calculate playback rate for pitch shift
        // TODO: define constants for magic numbers
        const playbackRate = Math.pow(2, pitchShiftSemitones / 12) * Math.pow(2, pitchShiftCommas / 53);
        source.playbackRate.value = playbackRate;

        source.connect(audioContext.destination);
        source.start(0);
    }

    loadSound('/static/audio/oud_note.mp3')

    function click_note(pitchShiftCommas) {
        // Play sound shifted up by 3 semitones to match concert pitch
        playSound(3, pitchShiftCommas);
    }
