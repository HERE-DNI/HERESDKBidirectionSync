---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolors"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMultiColors.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class</li>
<li class="self-crumb">setMultiColors abstract method</li>
</ol>
<div class="self-name">setMultiColors</div>
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
<div class="main-content" data-above-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setMultiColors abstract method</h1></div>
<section class="multi-line-signature">
bool
setMultiColors(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>double&gt; colorStops, </li>
<li>List&lt;<wbr/>int&gt; colorIndices, </li>
<li>List&lt;<wbr/>Color&gt; colors</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets lists of colors and multiple color segment stops for the polyline to be colored in.</p>
<p>When this representation is already set on any <code>MapPolyline</code>, values will be applied on that <code>MapPolyline</code> right away.
If this representation is not set on any <code>MapPolyline</code>, values will be applied once representation is set on a <code>MapPolyline</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>colorStops</code> List containing color stop values indicating a change of color on a polyline.
Color stops must be in the range of [0.0, 1.0].
Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
Color stop list must be of the same size as color indices list.
Maximum size is 100 color stops.
An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
</li>
<li>
<p><code>colorIndices</code> List of color indices (from the color list) corresponding to the color stops.
Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
Color indices list must be of the same size as color stop list.
Maximum size is 100 color indices.</p>
</li>
<li>
<p><code>colors</code> List of colors.
Maximum size is 16 colors.
An empty list is not allowed.</p>
</li>
</ul>
<p>Returns <code>bool</code>. Value indicating whether parameters are valid and can be applied.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setMultiColors(List&lt;double&gt; colorStops, List&lt;int&gt; colorIndices, List&lt;ui.Color&gt; colors);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class</li>
<li class="self-crumb">setMultiColors abstract method</li>
</ol>
<h5>MapPolylineSolidMultiColorRepresentation class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
