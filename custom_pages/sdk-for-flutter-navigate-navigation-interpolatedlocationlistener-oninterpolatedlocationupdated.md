---
title: "onInterpolatedLocationUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-oninterpolatedlocationupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onInterpolatedLocationUpdated.html -->


<div>
<h1>onInterpolatedLocationUpdated abstract method</h1></div>

void
onInterpolatedLocationUpdated(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-location-class">Location</a> location</li>
</ol>)

      

    

<p>Called whenever a new interpolated location is calculated, usually several times per second.</p>
<p>The interpolated locations are only provided between <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and
<a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls and the application is not running in the background.</p>
<ul>
<li><code>location</code> The interpolated location.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onInterpolatedLocationUpdated(Location location);</code></pre>

 



</div>
`
}</HTMLBlock>
