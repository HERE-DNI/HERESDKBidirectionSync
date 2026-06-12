---
title: "lastKnownLocation property"
slug: "sdk-for-flutter-navigate-location-locationengine-lastknownlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastKnownLocation.html -->


<div>
<h1>lastKnownLocation property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-core-location-class">Location</a>?
lastKnownLocation
<div class="features">override</div>


<p>The last known location obtained by the engine.
<a href="/sdk-for-flutter-navigate-core-location-class">Location</a> is returned synchronously. <a href="/sdk-for-flutter-navigate-core-location-class">Location</a> object has a timestamp attribute,
which reflects when data was obtained. If location was never obtained - null is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Location? get lastKnownLocation =&gt; _location.lastKnownLocation;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
