---
title: "onLocationUpdated abstract method"
slug: "sdk-for-flutter-explore-core-locationlistener-onlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLocationUpdated.html -->


<div>
<h1>onLocationUpdated abstract method</h1></div>

void
onLocationUpdated(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-location-class">Location</a> location</li>
</ol>)

      

    

<p>Called each time a new location is available.</p>
<p>In a navigation context while using the <code>Navigator</code> or <code>VisualNavigator</code>,
it's required to set the <code>Location.time</code> parameter for each <code>Location</code>
object so that the HERE SDK can map-match the locations properly.
If the <code>Location.time</code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code>Location</code> object.
Invoked on the main thread.</p>
<ul>
<li><code>location</code> Current location.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onLocationUpdated(Location location);</code></pre>

 



</div>
`
}</HTMLBlock>
