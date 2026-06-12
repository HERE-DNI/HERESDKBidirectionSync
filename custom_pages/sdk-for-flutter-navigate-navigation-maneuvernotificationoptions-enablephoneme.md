---
title: "enablePhoneme property"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablephoneme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enablePhoneme.html -->


<div>
<h1>enablePhoneme property</h1></div>

        
        bool
        enablePhoneme
<div class="features">getter/setter pair</div>


<p>A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names,
road numbers, city names) should be used when generating notifications. Direction information comes usually
in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is
synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability
and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of
direction information sound more natural.
<strong>Note:</strong> For now, this property is functional for road name and road number information only.</p>
<p>Defaults to <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool enablePhoneme;</code></pre>

 



</div>
`
}</HTMLBlock>
