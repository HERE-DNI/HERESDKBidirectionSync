---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapMarkerClusterCounterStyle-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapMarkerClusterCounterStyle-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapMarkerClusterCounterStyle/MapMarkerClusterCounterStyle.html">MapMarkerClusterCounterStyle</a></li>
<li class="section-title">
<a href="mapview/MapMarkerClusterCounterStyle-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapMarkerClusterCounterStyle/aboveMaxText.html">aboveMaxText</a></li>
<li><a href="mapview/MapMarkerClusterCounterStyle/fontSize.html">fontSize</a></li>
<li class="inherited"><a href="mapview/MapMarkerClusterCounterStyle/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapMarkerClusterCounterStyle/maxCountNumber.html">maxCountNumber</a></li>
<li class="inherited"><a href="mapview/MapMarkerClusterCounterStyle/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapMarkerClusterCounterStyle/textAnchor.html">textAnchor</a></li>
<li><a href="mapview/MapMarkerClusterCounterStyle/textColor.html">textColor</a></li>
<li class="section-title inherited"><a href="mapview/MapMarkerClusterCounterStyle-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapMarkerClusterCounterStyle/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapMarkerClusterCounterStyle/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapMarkerClusterCounterStyle-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapMarkerClusterCounterStyle/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapMarkerClusterCounterStyle class</li>
</ol>
<div class="self-name">MapMarkerClusterCounterStyle</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarkerClusterCounterStyle-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMarkerClusterCounterStyle class</h1></div>
<section class="desc markdown">
<p>Styling options for a marker cluster which is represented by the marker count as a text.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMarkerClusterCounterStyle">
<a href="../mapview/MapMarkerClusterCounterStyle/MapMarkerClusterCounterStyle.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-mapmarkerclustercounterstyle</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="aboveMaxText">
<a href="../mapview/MapMarkerClusterCounterStyle/aboveMaxText.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-abovemaxtext</a>
↔ String
</dt>
<dd>
  String to display if there are more markers clustered than <a href="../mapview/MapMarkerClusterCounterStyle/maxCountNumber.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-maxcountnumber</a>. Default value is "+99".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fontSize">
<a href="../mapview/MapMarkerClusterCounterStyle/fontSize.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-fontsize</a>
↔ double
</dt>
<dd>
  Font size of counter. Default value is 20.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapMarkerClusterCounterStyle/hashCode.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="maxCountNumber">
<a href="../mapview/MapMarkerClusterCounterStyle/maxCountNumber.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-maxcountnumber</a>
↔ int
</dt>
<dd>
  Maximal number of markers represented as exact number. Values smaller than 2 will be clamped to 2.
Default value is 99. When this value is changed, it is recommended to adapt <a href="../mapview/MapMarkerClusterCounterStyle/aboveMaxText.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-abovemaxtext</a> accordingly.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapMarkerClusterCounterStyle/runtimeType.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textAnchor">
<a href="../mapview/MapMarkerClusterCounterStyle/textAnchor.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-textanchor</a>
↔ <a href="../core/Anchor2D-class.html">/sdk-for-flutter-explore-core-anchor2d-class</a>
</dt>
<dd>
  Anchor of counter in regards to marker cluster image. Default is at the center.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="textColor">
<a href="../mapview/MapMarkerClusterCounterStyle/textColor.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-textcolor</a>
↔ Color
</dt>
<dd>
  Font color of counter. Default value is white.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapMarkerClusterCounterStyle/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapMarkerClusterCounterStyle/toString.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-tostring</a>(<wbr/>)
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
<a href="../mapview/MapMarkerClusterCounterStyle/operator_equals.html">/sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapMarkerClusterCounterStyle class</li>
</ol>
<h5>mapview library</h5>
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
