---
title: "lastKnownLocation property"
slug: "sdk-for-flutter-navigate-location-locationenginebase-lastknownlocation"
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


<p>The last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.
This property can be obtained without starting the <code>LocationEngine</code>. However, the initial value might be <code>null</code>
if no location has ever been obtained by the <code>LocationEngine</code>.
The time attribute of the <code>Location</code> object indicates when the last location was obtained.
Note: In order to receive continuous location updates, add a <code>LocationListener</code>.
Gets the last known location obtained by the <code>LocationEngine</code>. It is persisted throughout the app's lifecycle.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Location? get lastKnownLocation;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
