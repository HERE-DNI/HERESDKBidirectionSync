---
title: "MapPolylineDashImageRepresentation class abstract"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation-class.html -->


<div>
<h1>MapPolylineDashImageRepresentation class abstract</h1></div>

<p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
from each other.</p>
<p>This dash pattern representation consists only of images rendered at certain
points along the polyline. For rendering them without any distortions, polyline gets sliced into
series of straight segments that are multiple of sum of dash and gap lengths. For this
reason, the new polyline geometry might not align fully with original geometry.</p>
<p>The <a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashimage">MapPolylineDashImageRepresentation.dashImage</a> is stretched according to <code>MapPolylineDashImageRepresentation.dashLength</code>
and <code>MapPolylineDashImageRepresentation.dashWidth</code>, with image's width matched to <code>dashLength</code> and
image's height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
left-hand side between vertices <code>n</code> and <code>n+1</code>.</p>
<p>The spacing between images is specified by <code>MapPolylineDashImageRepresentation.gapLength</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation">MapPolylineDashImageRepresentation</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation-uniform">MapPolylineDashImageRepresentation.uniform</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashimage">dashImage</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashlength">dashLength</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashwidth">dashWidth</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-gaplength">gapLength</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
