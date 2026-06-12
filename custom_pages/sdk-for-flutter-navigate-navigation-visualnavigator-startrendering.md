---
title: "startRendering abstract method"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-startrendering"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startRendering.html -->


<div>
<h1>startRendering abstract method</h1></div>

void
startRendering(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a> mapView</li>
</ol>)

      

    

<p>Starts visual navigation rendering.</p>
<p>A preconfigured current location marker is shown as soon as a location is received.
The marker is chosen according to the transport mode specified in the route. If no route is
present, the marker is chosen based on the <a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">NavigatorInterface.trackingTransportSpecification</a> property.
Calling startRendering() changes the <a href="/sdk-for-flutter-navigate-mapview-mapcamera-principalpoint">MapCamera.principalPoint</a> property so that the current
position indicator is equal to the value from <a href="/sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">CameraBehavior.normalizedPrincipalPoint</a>,
in which by default places the principal point slightly at the bottom of the mapview. It is
restored to its original value when stopRendering() is called.
<strong>Note:</strong> When rendering is started again for a new map view instance, rendering
is automatically stopped on the previous map view instance. Also note that
the <a href="/sdk-for-flutter-navigate-mapview-mapviewbase-framerate">MapViewBase.frameRate</a> can be lowered to reduce CPU usage, to adjust for tradeoffs
between rendering smoothness versus battery consumption.</p>
<ul>
<li><code>mapView</code> The map view on which visual navigation will take place.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startRendering(MapViewBase mapView);</code></pre>

 



</div>
`
}</HTMLBlock>
