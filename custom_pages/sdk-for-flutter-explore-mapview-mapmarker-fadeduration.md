---
title: "fadeDuration property"
slug: "sdk-for-flutter-explore-mapview-mapmarker-fadeduration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fadeDuration.html -->


<div>
<h1>fadeDuration property</h1></div>
<section id="getter">

Duration
fadeDuration


<p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Duration get fadeDuration;</code></pre>

</section>
<section id="setter">

void
fadeDuration=(Duration value)


<p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p>
<p>Provided value is clamped in range [0.0, 10.0] seconds. Default value is 0 seconds which means the effect is disabled
and marker is added/removed immediately without any animation.
Fade-in effect is also applied when marker leaves and then re-enters screen area.</p>
<p>Change to this property is made asynchronously and is not guaranteed
to take effect on the next rendered frame. In particular, changing fade duration and removing
the marker immediately after may result in the new value being ignored for this removal.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set fadeDuration(Duration value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
