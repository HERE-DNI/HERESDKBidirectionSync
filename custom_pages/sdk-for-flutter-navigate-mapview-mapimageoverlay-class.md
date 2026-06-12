---
title: "MapImageOverlay class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapimageoverlay-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay-class.html -->


<div>
<h1>MapImageOverlay class abstract</h1></div>

<p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.</p>
<p>The image to be displayed is represented by a <a href="/sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> object.
By default, the overlay is centered on the given view coordinate.</p>
<p>The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate,
the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.</p>
<p>To display the map overlay, it needs to be added to the scene using <a href="/sdk-for-flutter-navigate-mapview-mapscene-addmapimageoverlay">MapScene.addMapImageOverlay</a>.
To stop displaying it, remove it from the scene using <a href="/sdk-for-flutter-navigate-mapview-mapscene-removemapimageoverlay">MapScene.removeMapImageOverlay</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-mapimageoverlay">MapImageOverlay</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-mapimageoverlay-withanchor">MapImageOverlay.withAnchor</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-anchor">anchor</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-draworder">drawOrder</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-image">image</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-viewcoordinates">viewCoordinates</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-mapimageoverlay-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
