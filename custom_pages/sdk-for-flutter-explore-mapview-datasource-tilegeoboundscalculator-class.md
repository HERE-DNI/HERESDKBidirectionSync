---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TileGeoBoundsCalculator-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/TileGeoBoundsCalculator-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/TileGeoBoundsCalculator/TileGeoBoundsCalculator.html">TileGeoBoundsCalculator</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/TileGeoBoundsCalculator-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/TileGeoBoundsCalculator/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/TileGeoBoundsCalculator/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/TileGeoBoundsCalculator-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/TileGeoBoundsCalculator/boundsOf.html">boundsOf</a></li>
<li class="inherited"><a href="mapview.datasource/TileGeoBoundsCalculator/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/TileGeoBoundsCalculator/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/TileGeoBoundsCalculator-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/TileGeoBoundsCalculator/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">TileGeoBoundsCalculator class</li>
</ol>
<div class="self-name">TileGeoBoundsCalculator</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/TileGeoBoundsCalculator-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TileGeoBoundsCalculator class abstract</h1></div>
<section class="desc markdown">
<p>A calculator of geodetic bounds for tiles identified by keys generated
in a particular tiling scheme (<a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a>).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TileGeoBoundsCalculator">
<a href="../mapview.datasource/TileGeoBoundsCalculator/TileGeoBoundsCalculator.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-tilegeoboundscalculator</a>(<a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a> tilingScheme)
</dt>
<dd>
          Creates an instance of <a href="../mapview.datasource/TileGeoBoundsCalculator-class.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-class</a>.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/TileGeoBoundsCalculator/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/TileGeoBoundsCalculator/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="boundsOf">
<a href="../mapview.datasource/TileGeoBoundsCalculator/boundsOf.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-boundsof</a>(<wbr/><a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey)
    → <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
</dt>
<dd>
  Computes the geodetic bounds (as <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>) for a tile identified by <a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/TileGeoBoundsCalculator/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/TileGeoBoundsCalculator/toString.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview.datasource/TileGeoBoundsCalculator/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-tilegeoboundscalculator-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">TileGeoBoundsCalculator class</li>
</ol>
<h5>mapview.datasource library</h5>
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
</HTMLBlock>
