<script>
    const subtitles = [
        'subway (on a "great" day) speed 🚆 🚉',
        'taking photos of a block bike lane speed 🚕🚓🤳',
        'e-bike delivery 🚴💨 down 2nd ave speed',
        '"walking" 🏃💨 through Times Square speed',
        'the express train from City Hall to Grand Central speed',
        'riding the 14th street 🚌 busway 🚌 speed',
        'riding an e-citibike 🚴 🚴 🚴 during the middle of rush hour',
        'bodega chopped-cheese 🥪 making speed'
    ]

    //select random subtitle
    $: subtitle = subtitles[Math.floor(Math.random() * subtitles.length)];

</script>

<p class="subtitle is-5">
    Locations to coordinates at <strong>{subtitle}</strong>.
</p>