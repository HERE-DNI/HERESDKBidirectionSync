---
title: "engineSizeInCubicCentimeters property"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-enginesizeincubiccentimeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- engineSizeInCubicCentimeters.html -->


<div>
<h1>engineSizeInCubicCentimeters property</h1></div>

        
        int?
        engineSizeInCubicCentimeters
<div class="features">getter/setter pair</div>


<p>Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535.
Default value is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the
road.</p>
<p><strong>Notes</strong></p>
<ul>
<li>For now, this option is only relevant in Japan and will be ignored for other countries. Currently,
map data for this option is only available for Japan.</li>
<li>Supported only in <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.scooter</a> (Alpha) transport mode.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? engineSizeInCubicCentimeters;</code></pre>

 



</div>
`
}</HTMLBlock>
