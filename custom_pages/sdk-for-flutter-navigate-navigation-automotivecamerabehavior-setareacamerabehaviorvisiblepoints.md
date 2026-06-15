---
title: "setAreaCameraBehaviorVisiblePoints abstract method"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setAreaCameraBehaviorVisiblePoints.html -->


<div>
<h1>setAreaCameraBehaviorVisiblePoints abstract method</h1></div>

void
setAreaCameraBehaviorVisiblePoints(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>&gt; points, </li>
<li>bool includeCurrentPosition</li>
</ol>)

      

    

<p>Configures the Area camera to frame the specified points.</p>
<p>The camera calculates the optimal zoom level and center position to display
all provided coordinates within the viewport. Use this for showing a single
point of interest or multiple points such as safety cameras.</p>
<p>This function does not change <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a>. To display the configured
area view, set <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a> to <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.area</a>.</p>
<p>Calling this function overrides any previously set geographic bounding box
configured via <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox">AutomotiveCameraBehavior.setAreaCameraBehaviorGeobox</a>.</p>
<ul>
<li>
<p><code>points</code> The list of geographic coordinates to display.</p>
</li>
<li>
<p><code>includeCurrentPosition</code> When true, the current vehicle position is
included in the visible area calculation, ensuring the vehicle remains
visible alongside the provided points.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setAreaCameraBehaviorVisiblePoints(List&lt;GeoCoordinates&gt; points, bool includeCurrentPosition);</code></pre>

 



</div>
`
}</HTMLBlock>
