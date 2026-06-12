---
title: "measureDependentWidth property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- measureDependentWidth.html -->


<div>
<h1>measureDependentWidth property</h1></div>
<section id="getter">

Map&lt;<a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, double&gt;
measureDependentWidth


<p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.
It is a dictionary that has keys that are <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s and values
that are width in pixels at this <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s.
This route and maneuver arrows width is multiplied by a pixel_scale <a href="/sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">MapViewBase.pixelScale</a>
before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
<a href="/sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one.
The function defined by a dictionary is linearly interpolated between each successive pair of data points.
For keys below the lowest <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used.
For keys above the highest <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used.
Only <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of <code>sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</code> type are supported.
<a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of other unsupported types will be ignored.
<code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
value of this single entry for all <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s.
Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
If route and maneuver arrows were not configured with this property,
then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
Gets the <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> dependent polyline and maneuver arrow width in pixels.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;MapMeasure, double&gt; get measureDependentWidth;</code></pre>

</section>
<section id="setter">

void
measureDependentWidth=(Map&lt;<a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, double&gt; value)


<p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.
It is a dictionary that has keys that are <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s and values
that are width in pixels at this <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s.
This route and maneuver arrows width is multiplied by a pixel_scale <a href="/sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale">MapViewBase.pixelScale</a>
before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
<a href="/sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor">VisualNavigator.maneuverArrowWidthFactor</a>; which by default equals one.
The function defined by a dictionary is linearly interpolated between each successive pair of data points.
For keys below the lowest <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used.
For keys above the highest <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>, its corresponding value width is used.
Only <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of <code>sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</code> type are supported.
<a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> of other unsupported types will be ignored.
<code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
value of this single entry for all <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>s.
Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
If route and maneuver arrows were not configured with this property,
then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
Sets the <a href="/sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> dependent route and maneuver arrows width in pixels.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set measureDependentWidth(Map&lt;MapMeasure, double&gt; value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
