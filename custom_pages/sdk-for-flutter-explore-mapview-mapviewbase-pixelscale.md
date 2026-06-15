---
title: "pixelScale property"
slug: "sdk-for-flutter-explore-mapview-mapviewbase-pixelscale"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pixelScale.html -->


<div>
<h1>pixelScale property</h1></div>
<section id="getter">

double
pixelScale


<p>The pixel scale factor used by this <code>MapView</code>.</p>
<p>Pixel scale is 0.0 if the map view is not initialized.</p>
<p>In cases where the <code>MapView</code> moves in between screens (e.g. from main screen to a CarPlay screen),
/ the most up-to-date pixel scale value can be obtained after a render target gets attached to the view.
/ To get notified when a render target gets attached to the <code>MapView</code>, see <a href="sdk-for-flutter-explore-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a>.
It is used to support screen resolution and size independence.
This value is a derivative of the device's screen pixel density and is a direct analog of</p>
<p>devicePixelRatio from FlutterView, ViewConfiguration or MediaQueryData.
It can be used to translate between physical pixels and</p>
<p>logical pixels
according to the formula:</p>
<p>logicalPixels = pixels / pixelScale.
Gets the pixel scale factor used by this <code>MapView</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double get pixelScale;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
