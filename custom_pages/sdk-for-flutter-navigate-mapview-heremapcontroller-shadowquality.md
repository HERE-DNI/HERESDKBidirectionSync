---
title: "shadowQuality property"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-shadowquality"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- shadowQuality.html -->


<div>
<h1>shadowQuality property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a>
shadowQuality


<p>The current shadow quality.
Default shadow quality is <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality.medium</a>.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static ShadowQuality get shadowQuality =&gt; $prototype.shadowQuality;</code></pre>

</section>
<section id="setter">

void
shadowQuality=(<a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality</a> shadowQuality)


<p>Sets the desired shadow quality for all instances of HereMap to <code>shadowQuality</code>.
The quality controls the size of the shadow maps and the cascade count.
Default shadow quality is <a href="sdk-for-flutter-navigate-mapview-shadowquality">ShadowQuality.medium</a>.
HereMaps can request to render shadows by feature.
Enabling shadows has a performance impact and should be considered only for devices with
sufficient performance.
Note: This feature is in beta state and thus there can be bugs and unexpected behavior.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void set shadowQuality(ShadowQuality shadowQuality) {
  $prototype.shadowQuality = shadowQuality;
}</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
