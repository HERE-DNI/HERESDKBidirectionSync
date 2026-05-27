---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PointTileSourceLoadResultHandler-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/PointTileSourceLoadResultHandler-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/PointTileSourceLoadResultHandler/PointTileSourceLoadResultHandler.html">PointTileSourceLoadResultHandler</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/PointTileSourceLoadResultHandler-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/PointTileSourceLoadResultHandler-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/PointTileSourceLoadResultHandler/failed.html">failed</a></li>
<li><a href="mapview.datasource/PointTileSourceLoadResultHandler/loaded.html">loaded</a></li>
<li class="inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/PointTileSourceLoadResultHandler/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">PointTileSourceLoadResultHandler class</li>
</ol>
<div class="self-name">PointTileSourceLoadResultHandler</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PointTileSourceLoadResultHandler-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PointTileSourceLoadResultHandler class abstract</h1></div>
<section class="desc markdown">
<p>Result handler of a load tile request.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PointTileSourceLoadResultHandler">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/PointTileSourceLoadResultHandler.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-pointtilesourceloadresulthandler</a>(void loadedLambda(<a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>, List&lt;<wbr/><a href="../mapview.datasource/PointData-class.html">/sdk-for-flutter-explore-mapview-datasource-pointdata-class</a>&gt;, <a href="../mapview.datasource/TileSourceTileMetadata-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class</a>), void failedLambda(<a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>))
</dt>
<dd>
          Result handler of a load tile request.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-runtimetype</a>
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
<dt class="callable" id="failed">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/failed.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-failed</a>(<wbr/><a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey)
    → void

</dt>
<dd>
  Called upon failed load tile request.
  

</dd>
<dt class="callable" id="loaded">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/loaded.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-loaded</a>(<wbr/><a href="../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey, List&lt;<wbr/><a href="../mapview.datasource/PointData-class.html">/sdk-for-flutter-explore-mapview-datasource-pointdata-class</a>&gt; data, <a href="../mapview.datasource/TileSourceTileMetadata-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class</a> metadata)
    → void

</dt>
<dd>
  Called upon successful load tile request.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/toString.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-tostring</a>(<wbr/>)
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
<a href="../mapview.datasource/PointTileSourceLoadResultHandler/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-pointtilesourceloadresulthandler-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">PointTileSourceLoadResultHandler class</li>
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
