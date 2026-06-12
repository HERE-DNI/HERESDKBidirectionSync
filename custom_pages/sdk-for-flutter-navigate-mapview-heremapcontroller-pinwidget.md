---
title: "pinWidget abstract method"
slug: "sdk-for-flutter-navigate-mapview-heremapcontroller-pinwidget"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- pinWidget.html -->


<div>
<h1>pinWidget abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a>?
pinWidget(<ol class="parameter-list"> <li>Widget widget, </li>
<li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, {</li>
<li><a href="/sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a>? anchor, </li>
</ol>})

      

    

<p>Pins a <code>Widget</code> to the MapView and returns a proxy object that can be used to
control the pinning.</p>
<p>The altitude component of the coordinates, if set, is interpreted as above sea level.
When not set, the coordinates are interpreted as at ground level.</p>
<p><code>widget</code> Widget to pin</p>
<p><code>coordinates</code> GeoCoordinates to pin the widget at</p>
<p><code>anchor</code> The anchor point for the widget which specifies the position offset relative to the widget's coordinates.</p>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-widgetpin-class">WidgetPin</a> a pin proxy object</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WidgetPin? pinWidget(Widget widget, GeoCoordinates coordinates, {Anchor2D? anchor});</code></pre>

 



</div>
`
}</HTMLBlock>
