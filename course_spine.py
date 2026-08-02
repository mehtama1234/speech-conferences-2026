COURSE_TITLE = "Speech And Signal Processing From First Principles"
COURSE_SUBTITLE = (
    "A plain-language course spine for ICASSP 2026 now, with Interspeech to join "
    "when its open proceedings publish."
)

INTRO = [
    "A sound is movement in air. A microphone turns that movement into numbers. Speech and signal processing are about making sense of those numbers.",
    "ICASSP is broader than speech. It covers audio, images, radar, medical signals, wireless signals, graphs, sensors, and many other streams of measurements. Speech is one important slice of a larger signal-processing world.",
    "This course page is honest about the current data. The public ICASSP map is title-only, so it can explain topics and counts, but it should not pretend to know each paper's full method until abstracts or full texts are open.",
]

SECTIONS = [
    {
        "kicker": "Start",
        "title": "The Whole Field Starts With A Measured Signal",
        "summary": "A signal is a changing measurement: sound pressure, light, motion, radio energy, brain activity, or any stream of numbers over time or space.",
        "body": [
            "A microphone measures air pressure over time. A camera measures light over a grid. A radar measures reflected radio energy. A medical device measures electrical or physical activity. These are all signals because they are measurements that vary.",
            "The first problem is that useful information is mixed with noise, delay, missing data, and interference. The signal you want is rarely alone. A voice may be mixed with traffic, music, room echo, another speaker, or the microphone's own limits.",
            "Signal processing asks how to recover, compress, compare, separate, transform, and interpret those measurements without losing the parts that matter.",
        ],
        "applications": [
            "Speech recognition turns a voice signal into words.",
            "Medical sensing turns body measurements into warning signs or diagnoses.",
            "Wireless systems turn radio signals into messages between devices.",
        ],
    },
    {
        "kicker": "Sound",
        "title": "Speech Is Sound With Human Structure",
        "summary": "Speech carries words, speaker identity, emotion, timing, accent, health cues, and social context.",
        "body": [
            "Speech is not just text in the air. The same sentence can be whispered, shouted, rushed, calm, tired, angry, accented, sung, or slurred. A listener hears words, but also who is speaking and how they are speaking.",
            "A speech system may need to recognize words, identify a speaker, separate two voices, remove background noise, detect emotion, preserve tone in translation, or notice health changes in voice.",
            "This is why the speech slice of ICASSP has many subtopics. Automatic speech recognition is the steady core, but enhancement, speaker checks, synthesis, audio-visual speech, speech language models, health, and low-resource languages all solve different parts of the same sound-to-meaning problem.",
        ],
        "applications": [
            "Assistants and captioning need word recognition under noise and accents.",
            "Call centers need speaker turns, intent, emotion, and quality monitoring.",
            "Clinical tools can use speech changes as clues for disease or recovery.",
        ],
    },
    {
        "kicker": "Time",
        "title": "Time Is Part Of The Meaning",
        "summary": "Order, rhythm, pauses, overlap, and delay change what the signal means.",
        "body": [
            "A written word can sit still on a page. A spoken word unfolds over time. The order of sounds matters. The length of a pause matters. The rise and fall of pitch matters. A streaming system must decide before the future has arrived.",
            "This makes speech different from many static tasks. The system must remember what came before, update as new sound arrives, and sometimes revise an earlier guess.",
            "Timing also matters in products. A caption that appears five seconds late may be accurate but not useful. A hearing aid, meeting assistant, or translation system has to work while the person is still speaking.",
        ],
        "applications": [
            "Streaming speech recognition must balance speed with accuracy.",
            "Speaker diarization must track who spoke when, including overlap.",
            "Real-time translation must preserve enough timing that conversation still feels natural.",
        ],
    },
    {
        "kicker": "Topology",
        "title": "Topology Means Which Pieces Of A Signal Are Connected",
        "summary": "In speech and signals, topology is the shape of connections across time, speakers, sources, rooms, words, languages, and sensors.",
        "body": [
            "In plain words, topology asks what is connected to what. Do two sound frames belong to the same word? Do two voice segments belong to the same speaker? Are two microphones hearing the same source from different places? Does a phrase loop back as a repeated chorus?",
            "A conversation has topology. Turns connect to speakers. Interruptions overlap. A reply connects to an earlier question. A meeting has threads that split and later rejoin.",
            "A room has topology too. Sound travels from mouth to walls to microphone. Echoes create extra paths. Several microphones form a shape that can help locate where a voice came from.",
            "Language has topology. Sounds connect into syllables, syllables into words, words into grammar, related languages into families, and code-switching into paths between languages.",
        ],
        "applications": [
            "Diarization uses topology to connect voice segments that belong to the same person.",
            "Source separation uses topology to untangle which time-frequency pieces belong to which sound.",
            "Audio-visual speech uses topology to connect lip motion with the matching sound.",
            "Low-resource speech uses topology between related languages to share evidence where data is scarce.",
        ],
    },
    {
        "kicker": "Transform",
        "title": "A New View Can Make The Signal Easier To Read",
        "summary": "Many methods change the view of a signal so hidden structure becomes easier to separate.",
        "body": [
            "A waveform shows pressure over time. A spectrogram shows which frequencies are present at each moment. Both describe the same sound, but each makes different patterns easier to see.",
            "This is a central signal-processing move: transform the data into a view where the desired pattern is clearer. Noise may occupy different frequencies than speech. A musical instrument may have a repeated frequency shape. A radar reflection may have a pattern that appears only after the right transform.",
            "Modern models learn many such views automatically, but the reason is the same: find a representation where useful structure is easier to use.",
        ],
        "applications": [
            "Speech enhancement uses frequency structure to reduce noise.",
            "Music separation uses patterns that differ between vocals, drums, and instruments.",
            "Biomedical signal analysis uses transformed views to find rhythms and events.",
        ],
    },
    {
        "kicker": "Learning",
        "title": "Learning Reuses Patterns From Many Examples",
        "summary": "Models learn what speech, music, noise, speakers, rooms, and languages tend to look like.",
        "body": [
            "A hand-written rule cannot cover every speaker, room, microphone, language, and background sound. Learning gives the system a way to improve from examples.",
            "Self-supervised learning uses large amounts of unlabeled audio to learn useful structure before any specific task is taught. This matters because labeled speech data is expensive, and many languages or clinical cases have little data.",
            "Generative models learn to create or restore signals. They can synthesize speech, remove noise, fill missing audio, convert voices, or separate sources when the target sound is mixed with others.",
        ],
        "applications": [
            "Low-resource languages need learning methods that reuse related data.",
            "Voice conversion and synthesis need models that preserve content while changing voice or style.",
            "Audio repair needs models that infer missing or damaged parts of a signal.",
        ],
    },
    {
        "kicker": "Trust",
        "title": "Speech Systems Need Proof Against Mistakes And Misuse",
        "summary": "Speech is personal, easy to fake, and often used in high-stakes settings.",
        "body": [
            "A speech system can fail by hearing the wrong words, mixing two speakers, missing a quiet voice, leaking private information, or accepting a fake voice as real.",
            "Anti-spoofing and deepfake detection matter because voice is increasingly used as identity, evidence, and interface. A synthetic voice can sound convincing even when it is not the person.",
            "Privacy matters because speech contains more than words. It may reveal identity, location, health, emotion, age, background, and relationships.",
        ],
        "applications": [
            "Banking and security systems need to distinguish real speakers from fake or replayed voices.",
            "Meeting tools need clear consent, retention, and access rules for recordings.",
            "Clinical speech tools need careful validation before informing care.",
        ],
    },
    {
        "kicker": "Evaluation",
        "title": "The Right Score Depends On The Job",
        "summary": "A system can be accurate by one score and still bad for a person using it.",
        "body": [
            "Word error rate matters for transcription, but it does not measure everything. A system may get most words right but fail on names, quiet speakers, accents, or urgent phrases.",
            "For enhancement, the question may be whether speech becomes easier to understand. For synthesis, whether it sounds natural and preserves identity. For diarization, whether speaker turns are correctly grouped.",
            "Good evaluation starts by naming the use. A podcast editor, doctor, hearing aid user, emergency dispatcher, and language learner need different evidence.",
        ],
        "applications": [
            "Captioning needs low delay and fair performance across speakers.",
            "Search in audio archives needs retrieval quality, not only transcript accuracy.",
            "Speech health tools need patient-level evidence, not only clean lab scores.",
        ],
    },
    {
        "kicker": "Fields",
        "title": "Why Signal Processing Matters Across Fields",
        "summary": "Any field with messy measurements needs signal processing.",
        "body": [
            "Robotics needs signal processing for microphones, cameras, touch sensors, lidar, radar, and motor feedback. AI hardware needs it because efficient models depend on compact, useful representations. Search needs it because audio and video archives must be indexed and retrieved.",
            "Topology connects speech to other fields. In computer vision, it appears as connected regions and object shapes. In robotics, it appears as reachable paths and contact. In networks, it appears as which devices can reach each other. In speech, it appears as connected sounds, speakers, rooms, and language paths.",
            "ICASSP matters because it teaches the wider lesson: before a system can reason, it must measure; before it can measure well, it must understand the signal.",
        ],
        "applications": [
            "Medicine uses signals from speech, brain activity, images, and wearable sensors.",
            "Climate and remote sensing use signal processing to read large noisy measurements.",
            "Music and media tools use signal processing to separate, generate, repair, and search sound.",
            "Communications uses signal processing so devices can share information through noisy channels.",
        ],
    },
]

READING_PATH = [
    ("index.html", "ICASSP title map"),
    ("../index.html", "Root copy"),
]
