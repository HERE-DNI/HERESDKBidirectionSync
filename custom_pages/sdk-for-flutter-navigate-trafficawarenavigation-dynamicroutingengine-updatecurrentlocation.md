---
title: "updateCurrentLocation abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateCurrentLocation.html -->


<div>
<h1>updateCurrentLocation abstract method</h1></div>

void
updateCurrentLocation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a> mapMatchedLocation, </li>
<li>int sectionIndex</li>
</ol>)

      

    

<p>Updates the current location.</p>
<p>This location will be used as new starting point when the next
<a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval">DynamicRoutingEngineOptions.pollInterval</a> is reached and a new route is requested.
If an immediate route update is needed, consider to use the RoutingEngine instead.
All subsequently calculated routes used for the ETA calculation will start from this location.
The location needs to lie on the route or a <code>RoutingError</code> will be issued.</p>
<ul>
<li>
<p><code>mapMatchedLocation</code> The last known location.
It is recommended to use a <a href="sdk-for-flutter-navigate-navigation-navigablelocation-mapmatchedlocation">NavigableLocation.mapMatchedLocation</a>
as the driver is expected to be on a road.</p>
</li>
<li>
<p><code>sectionIndex</code> The current section from <a class="deprecated" href="sdk-for-flutter-navigate-navigation-routeprogress-sectionindex">RouteProgress.sectionIndex</a>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void updateCurrentLocation(MapMatchedLocation mapMatchedLocation, int sectionIndex);</code></pre>

 



</div>
`
}</HTMLBlock>
