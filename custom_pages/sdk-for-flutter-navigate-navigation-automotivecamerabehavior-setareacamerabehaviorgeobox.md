---
title: "setAreaCameraBehaviorGeobox abstract method"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAreaCameraBehaviorGeobox.html -->


<div>
<h1>setAreaCameraBehaviorGeobox abstract method</h1></div>

void
setAreaCameraBehaviorGeobox(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> geobox</li>
</ol>)

      

    

<p>Configures the Area camera to frame the specified geographic bounding box.</p>
<p>The camera automatically calculates the appropriate zoom level and center
position to ensure the entire area is visible within the viewport.</p>
<p>This function does not change <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a>. To display the configured
area view, set <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a> to <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.area</a>.</p>
<p>Calling this function overrides any previously set visible points configured
via <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints">AutomotiveCameraBehavior.setAreaCameraBehaviorVisiblePoints</a>.</p>
<ul>
<li><code>geobox</code> The geographic bounding box to display.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAreaCameraBehaviorGeobox(GeoBox geobox);</code></pre>

 



</div>
`
}</HTMLBlock>
