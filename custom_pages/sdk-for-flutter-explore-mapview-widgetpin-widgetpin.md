---
title: "WidgetPin constructor"
slug: "sdk-for-flutter-explore-mapview-widgetpin-widgetpin"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WidgetPin.html -->


<div>
<h1>WidgetPin constructor</h1></div>

WidgetPin({<ol class="parameter-list"> <li>required Widget child, </li>
<li>required <a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a>? anchor, </li>
<li>dynamic onChange()?, </li>
<li>dynamic onUnpin(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a></li>
</ol>)?, </li>
</ol>})
    

<p>Creates a <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a> displaying child <code>Widget</code> at coordinates location on the map
Don't use this constructor directly. Instead use <a href="sdk-for-flutter-explore-mapview-heremapcontroller-pinwidget">HereMapController.pinWidget</a> to create a <a href="sdk-for-flutter-explore-mapview-widgetpin-class">WidgetPin</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory WidgetPin({
  required Widget child,
  required GeoCoordinates coordinates,
  Anchor2D? anchor,
  Function()? onChange,
  Function(WidgetPin)? onUnpin,
}) =&gt;
    $prototype.make(
      child: child,
      coordinates: coordinates,
      anchor: anchor,
      onChange: onChange,
      onUnpin: onUnpin,
    );</code></pre>

 



</div>
`
}</HTMLBlock>
