---
title: "isAccuracyVisualized property"
slug: "sdk-for-flutter-explore-mapview-locationindicator-isaccuracyvisualized"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isAccuracyVisualized.html -->


<div>
<h1>isAccuracyVisualized property</h1></div>
<section id="getter">

bool
isAccuracyVisualized


<p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
Returns whether <a href="/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> is used to scale the accuracy indicator halo.
Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isAccuracyVisualized;</code></pre>

</section>
<section id="setter">

void
isAccuracyVisualized=(bool value)


<p>Whether the horizontal accuracy is visualized by scaling the accuracy indicator halo.
Sets whether <a href="/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> is used to scale the accuracy indicator halo.
Default is <code>false</code>, in which case the halo has a fixed and zoom level independent size.</p>
<p>When set to <code>true</code>, the radius of the halo corresponds to the value of
<a href="/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> passed to <a href="/sdk-for-flutter-explore-mapview-locationindicator-updatelocation">LocationIndicator.updateLocation</a>
and scales in world coordinates.</p>
<p>For values smaller than 20 meters the halo is hidden.
The radius of the halo is limited to 500 meters and values higher than that or <code>null</code>
will keep the halo at that size.</p>
<p>If the location indicator is set to inactive (which can be checked via <a href="/sdk-for-flutter-explore-mapview-locationindicator-isactive">LocationIndicator.isActive</a> flag),
then the halo is always hidden. The value of this property remains unchanged regardless of the flag's value.
If the location indicator is set to active:</p>
<ul>
<li>Built-in location indicators:
<ul>
<li>The halo is always shown.</li>
<li>If the accuracy visualization is set to <code>true</code>, the size of the halo scales with
<a href="/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, halo displays at a default size.</li>
</ul>
</li>
<li>Custom location indicator:
<ul>
<li>If the accuracy visualization is set to <code>true</code>, halo is shown and the size of the halo scales with
<a href="/sdk-for-flutter-explore-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> in world coordinates.</li>
<li>If the accuracy visualization is set to <code>false</code>, no halo is shown since it might not fit together with the custom 3d model.</li>
</ul>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isAccuracyVisualized(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
