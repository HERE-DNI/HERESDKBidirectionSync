---
title: "PolylineSimplifier class abstract"
slug: "sdk-for-flutter-explore-core-polylinesimplifier-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplifier-class.html -->


<div>
<h1>PolylineSimplifier class abstract</h1></div>

<p>PolylineSimplifier helps to reduce the number of points
in the polyline by removing redundant elements using
Douglas–Peucker algorithm, so that result stays
within <a href="sdk-for-flutter-explore-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a>.</p>
<p>Typical use case is to perform input preparation step
before invoking computationally heavy API. Such API
have an upper limit on the input collection size
and is subject to reduced performance when collection
is huge. Examples of such API are:</p>
<ul>
<li><code>TrafficEngine</code> methods which accept a <code>GeoCorridor</code>;</li>
<li><code>RoutePrefetcher.prefetchGeoCorridor</code>.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-polylinesimplifier">PolylineSimplifier</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-simplify">simplify</a></li><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-core-polylinesimplifier-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
