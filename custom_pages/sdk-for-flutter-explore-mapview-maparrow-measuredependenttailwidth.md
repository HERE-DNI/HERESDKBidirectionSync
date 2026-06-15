---
title: "measureDependentTailWidth property"
slug: "sdk-for-flutter-explore-mapview-maparrow-measuredependenttailwidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- measureDependentTailWidth.html -->


<div>
<h1>measureDependentTailWidth property</h1></div>
<section id="getter">

Map&lt;<a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>, double&gt;
measureDependentTailWidth


<p>The width of the arrow tail in pixels, where the key is a <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> and the value is
a tail width in pixels at this <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>.
Gets the <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependent arrow tail width in pixels.</p>
<p>If tail width was configured without <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependency, then <code>measureDependentTailWidth</code>
contains single entry with measure 0 of type <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> and width value
equal to <code>widthInPixels</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;MapMeasure, double&gt; get measureDependentTailWidth;</code></pre>

</section>
<section id="setter">

void
measureDependentTailWidth=(Map&lt;<a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>, double&gt; value)


<p>The width of the arrow tail in pixels, where the key is a <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> and the value is
a tail width in pixels at this <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a>.
Sets the <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> dependent arrow tail width in pixels.</p>
<p>The width values are linearly interpolated between nearest map entries.
Width values for <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> outside the map entries are kept constant, using the
value of the largest/smallest key.</p>
<p>Only <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> of <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type is supported.
Other <a href="sdk-for-flutter-explore-mapview-mapmeasure-class">MapMeasure</a> types are unsupported and hence, will be ignored.</p>
<p>Map with a single entry is equivalent to use of the <code>widthInPixels</code> value
in the constructor, so a constant width setting, independent of camera.</p>
<p>Empty input is ignored and existing width is maintained.</p>
<p>The width values should be positive. Map entries with width values less than or equal to 0 are ignored.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set measureDependentTailWidth(Map&lt;MapMeasure, double&gt; value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
