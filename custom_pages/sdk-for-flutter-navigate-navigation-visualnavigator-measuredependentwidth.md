---
title: "measureDependentWidth property"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-measuredependentwidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- measureDependentWidth.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">measureDependentWidth property</li>
</ol>
<div class="self-name">measureDependentWidth</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>measureDependentWidth property</h1></div>
<section id="getter">
<section class="multi-line-signature">
Map&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class, double&gt;
measureDependentWidth
</section>
<section class="desc markdown">
<p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.
It is a dictionary that has keys that are /sdk-for-flutter-navigate-mapview-mapmeasure-classs and values
that are width in pixels at this /sdk-for-flutter-navigate-mapview-mapmeasure-classs.
This route and maneuver arrows width is multiplied by a pixel_scale /sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale
before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
/sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor; which by default equals one.
The function defined by a dictionary is linearly interpolated between each successive pair of data points.
For keys below the lowest /sdk-for-flutter-navigate-mapview-mapmeasure-class, its corresponding value width is used.
For keys above the highest /sdk-for-flutter-navigate-mapview-mapmeasure-class, its corresponding value width is used.
Only /sdk-for-flutter-navigate-mapview-mapmeasure-class of <code>sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</code> type are supported.
/sdk-for-flutter-navigate-mapview-mapmeasure-class of other unsupported types will be ignored.
<code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
value of this single entry for all /sdk-for-flutter-navigate-mapview-mapmeasure-classs.
Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
If route and maneuver arrows were not configured with this property,
then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
Gets the /sdk-for-flutter-navigate-mapview-mapmeasure-class dependent polyline and maneuver arrow width in pixels.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Map&lt;MapMeasure, double&gt; get measureDependentWidth;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
measureDependentWidth=(<wbr/>Map&lt;<wbr/>/sdk-for-flutter-navigate-mapview-mapmeasure-class, double&gt; value)
</section>
<section class="desc markdown">
<p>The <code>measureDependentWidth</code> that defines the route and maneuver arrows width.
It is a dictionary that has keys that are /sdk-for-flutter-navigate-mapview-mapmeasure-classs and values
that are width in pixels at this /sdk-for-flutter-navigate-mapview-mapmeasure-classs.
This route and maneuver arrows width is multiplied by a pixel_scale /sdk-for-flutter-navigate-mapview-mapviewbase-pixelscale
before being rendered. The maneuver arrow width is additionally multiplied by a factor configurable with
/sdk-for-flutter-navigate-navigation-visualnavigator-maneuverarrowwidthfactor; which by default equals one.
The function defined by a dictionary is linearly interpolated between each successive pair of data points.
For keys below the lowest /sdk-for-flutter-navigate-mapview-mapmeasure-class, its corresponding value width is used.
For keys above the highest /sdk-for-flutter-navigate-mapview-mapmeasure-class, its corresponding value width is used.
Only /sdk-for-flutter-navigate-mapview-mapmeasure-class of <code>sdk.mapview.MapMeasure.Kind.ZOOM_LEVEL</code> type are supported.
/sdk-for-flutter-navigate-mapview-mapmeasure-class of other unsupported types will be ignored.
<code>measureDependentWidth</code> with a single entry is equivalent to use of the constant width
value of this single entry for all /sdk-for-flutter-navigate-mapview-mapmeasure-classs.
Empty <code>measureDependentWidth</code> is ignored and existing dictionary of width is maintained.
The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.
If route and maneuver arrows were not configured with this property,
then <code>measureDependentWidth</code> contains predefined values chosen to be optimal for different route classes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
Sets the /sdk-for-flutter-navigate-mapview-mapmeasure-class dependent route and maneuver arrows width in pixels.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set measureDependentWidth(Map&lt;MapMeasure, double&gt; value);</code></pre>
</section>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">measureDependentWidth property</li>
</ol>
<h5>VisualNavigator class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
