---
title: "MapCameraUpdateFactory class abstract"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraUpdateFactory-class.html -->


<div>
<h1>MapCameraUpdateFactory class abstract</h1></div>

<p>Factory for creating MapCameraUpdate to change map's camera.</p>
<p>For some factory methods you can apply an additional padding in pixels by setting a
<code>viewRectangle</code> parameter based on the current size of the map view:</p>
<pre class="language-dart"><code>var leftPaddingInPixels = 5;
var rightPaddingInPixels = 5;
var topPaddingInPixels = 5;
var bottomPaddingInPixels = 5;
var horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
var verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

var origin = Point2D(leftPaddingInPixels, topPaddingInPixels);
var sizeInPixels = Size2D(_hereMapController.viewportSize.width - horizontalPaddingInPixels, _hereMapController.viewportSize.height - verticalPaddingInPixels);
var paddedViewRectangle = Rectangle2D(origin, sizeInPixels);
</code></pre>
<p>The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
also the top-left corner of the map's viewport.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-mapcameraupdatefactory">MapCameraUpdateFactory</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate">compositeUpdate</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea">lookAtArea</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle">lookAtAreaWithGeoOrientationAndViewRectangle</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithviewrectangle">lookAtAreaWithViewRectangle</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoint">lookAtPoint</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoints">lookAtPoints</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithgeoorientationandmeasure">lookAtPointWithGeoOrientationAndMeasure</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithmeasure">lookAtPointWithMeasure</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithorientation">lookAtPointWithOrientation</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookattargetandpoints">lookAtTargetAndPoints</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint">lookToMatchGeoPointToViewPoint</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpointwithorientationmapmeasure">lookToMatchGeoPointToViewPointWithOrientationMapMeasure</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-orbitby">orbitBy</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-panby">panBy</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-rotateby">rotateBy</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint">setNormalizedPrincipalPoint</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setprincipalpoint">setPrincipalPoint</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setverticalfieldofview">setVerticalFieldOfView</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomby">zoomBy</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomto">zoomTo</a></li></ul>

 



</div>
`
}</HTMLBlock>
