---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolorgradientlength"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMultiColorGradientLength.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class</li>
<li class="self-crumb">setMultiColorGradientLength abstract method</li>
</ol>
<div class="self-name">setMultiColorGradientLength</div>
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
<h1>setMultiColorGradientLength abstract method</h1></div>
<section class="multi-line-signature">
bool
setMultiColorGradientLength(<wbr/><ol class="parameter-list single-line"> <li>double length</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the multiple color segment gradient length.</p>
<p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
gradient of specific length which is part of the color segment being blended.</p>
<p>Start of the segment is blended with a color from the previous segment.
Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
smallest segment's size to other segment size ratio.</p>
<p>Length of '0.0' is the default value which means blending will not be applied.
Valid value range is [0.0, 1.0]. Out of range values are not supported.
When this representation is already set on any <code>MapPolyline</code>, value will be applied on that <code>MapPolyline</code> right away.
If this representation is not set on any <code>MapPolyline</code>, value will be applied once representation is set on a <code>MapPolyline</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>length</code> Multiple color segment gradient length. Length of '0.0' is the default value which means blending will not be applied.
Valid value range is [0.0, 1.0]. Out of range values are not supported.</li>
</ul>
<p>Returns <code>bool</code>. Value indicating whether specified value is valid and can be applied.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setMultiColorGradientLength(double length);</code></pre>
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
<li class="self-crumb">setMultiColorGradientLength abstract method</li>
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
