---
title: "MapMarkerTextStyle.withFont constructor"
slug: "sdk-for-flutter-explore-mapview-mapmarkertextstyle-mapmarkertextstyle-withfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerTextStyle.withFont.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapmarkertextstyle-class</li>
<li class="self-crumb">MapMarkerTextStyle.withFont factory constructor</li>
</ol>
<div class="self-name">MapMarkerTextStyle.withFont</div>
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
<div class="main-content" data-above-sidebar="mapview/MapMarkerTextStyle-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapMarkerTextStyle.withFont constructor</h1></div>
<section class="multi-line-signature">
MapMarkerTextStyle.withFont(<wbr/><ol class="parameter-list"> <li>double textSize, </li>
<li>Color textColor, </li>
<li>double textOutlineSize, </li>
<li>Color textOutlineColor, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmarkertextstyleplacement&gt; placements, </li>
<li>String fontName, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a set of styling options for the text of a /sdk-for-flutter-explore-mapview-mapmarker-class.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<p>List of placements is used to specify allowed placement of text relative to the icon.
When marker overlapping is allowed as set by /sdk-for-flutter-explore-mapview-mapmarker-isoverlapallowed,
only first placement element is considered.
Otherwise the placement value is chosen so that the text does not overlap
with other <code>MapMarker</code> instances.</p>
<p>Placement values are prioritized according
to the order in which they appear in the list. Lists with duplicate entries
as well as empty lists are not supported.</p>
<ul>
<li>
<p><code>textSize</code> The size of the text in pixels.
Only positive values are supported.</p>
</li>
<li>
<p><code>textColor</code> The text color.</p>
</li>
<li>
<p><code>textOutlineSize</code> The size of the text outline in pixels.
Only non-negative values are supported.</p>
</li>
<li>
<p><code>textOutlineColor</code> The color of the text outline.</p>
</li>
<li>
<p><code>placements</code> List of allowed placements of the text relative to the icon of a /sdk-for-flutter-explore-mapview-mapmarker-class.</p>
</li>
<li>
<p><code>fontName</code> Font name, registered with <code>AssetsManager.registerFont</code>.
If empty string is provided, a default font will be used.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-explore-mapview-mapmarkertextstyleinstantiationexception-class. In case of invalid input parameters.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarkerTextStyle.withFont(double textSize, ui.Color textColor, double textOutlineSize, ui.Color textOutlineColor, List&lt;MapMarkerTextStylePlacement&gt; placements, String fontName) =&gt; $prototype.withFont(textSize, textColor, textOutlineSize, textOutlineColor, placements, fontName);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapmarkertextstyle-class</li>
<li class="self-crumb">MapMarkerTextStyle.withFont factory constructor</li>
</ol>
<h5>MapMarkerTextStyle class</h5>
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
