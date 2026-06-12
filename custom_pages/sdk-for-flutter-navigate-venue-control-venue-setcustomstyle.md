---
title: "setCustomStyle abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venue-setcustomstyle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomStyle.html -->


<div>
<h1>setCustomStyle abstract method</h1></div>

void
setCustomStyle(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-venue-data-venuegeometry-class">VenueGeometry</a>&gt; geometries, </li>
<li><a href="/sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class">VenueGeometryStyle</a>? style, </li>
<li><a href="/sdk-for-flutter-navigate-venue-style-venuelabelstyle-class">VenueLabelStyle</a>? labelStyle</li>
</ol>)

      

    

<p>Sets a custom style for geometries and related labels.</p>
<ul>
<li>
<p><code>geometries</code> The list of geometries to apply the new style.</p>
</li>
<li>
<p><code>style</code> The style for geometries, or <code>null</code> to reset the style to default.</p>
</li>
<li>
<p><code>labelStyle</code> The style for geometry labels, or <code>null</code> to reset the label style to default.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setCustomStyle(List&lt;VenueGeometry&gt; geometries, VenueGeometryStyle? style, VenueLabelStyle? labelStyle);</code></pre>

 



</div>
`
}</HTMLBlock>
