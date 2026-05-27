---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapPolylineDashImageRepresentation-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapPolylineDashImageRepresentation/MapPolylineDashImageRepresentation.html">MapPolylineDashImageRepresentation</a></li>
<li><a href="mapview/MapPolylineDashImageRepresentation/MapPolylineDashImageRepresentation.uniform.html">uniform</a></li>
<li class="section-title">
<a href="mapview/MapPolylineDashImageRepresentation-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapPolylineDashImageRepresentation/dashImage.html">dashImage</a></li>
<li><a href="mapview/MapPolylineDashImageRepresentation/dashLength.html">dashLength</a></li>
<li><a href="mapview/MapPolylineDashImageRepresentation/dashWidth.html">dashWidth</a></li>
<li><a href="mapview/MapPolylineDashImageRepresentation/gapLength.html">gapLength</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineDashImageRepresentation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineDashImageRepresentation-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapPolylineDashImageRepresentation class</li>
</ol>
<div class="self-name">MapPolylineDashImageRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineDashImageRepresentation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolylineDashImageRepresentation class abstract</h1></div>
<section class="desc markdown">
<p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
from each other.</p>
<p>This dash pattern representation consists only of images rendered at certain
points along the polyline. For rendering them without any distortions, polyline gets sliced into
series of straight segments that are multiple of sum of dash and gap lengths. For this
reason, the new polyline geometry might not align fully with original geometry.</p>
<p>The <a href="../mapview/MapPolylineDashImageRepresentation/dashImage.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashimage</a> is stretched according to <code>MapPolylineDashImageRepresentation.dashLength</code>
and <code>MapPolylineDashImageRepresentation.dashWidth</code>, with image's width matched to <code>dashLength</code> and
image's height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
left-hand side between vertices <code>n</code> and <code>n+1</code>.</p>
<p>The spacing between images is specified by <code>MapPolylineDashImageRepresentation.gapLength</code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li><a href="../mapview/MapPolylineRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapPolylineDashImageRepresentation">
<a href="../mapview/MapPolylineDashImageRepresentation/MapPolylineDashImageRepresentation.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation</a>(<a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashLength, <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> gapLength, <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashWidth, <a href="../mapview/MapImage-class.html">/sdk-for-flutter-explore-mapview-mapimage-class</a> image)
</dt>
<dd>
          Creates a simple dash pattern in which the lengths of a dash and gap can be different.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapPolylineDashImageRepresentation.uniform">
<a href="../mapview/MapPolylineDashImageRepresentation/MapPolylineDashImageRepresentation.uniform.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation-uniform</a>(<a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashLength, <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a> dashWidth, <a href="../mapview/MapImage-class.html">/sdk-for-flutter-explore-mapview-mapimage-class</a> image)
</dt>
<dd>
          Creates a uniform dash pattern in which the length of a gap is the same as the length of
a dash.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="dashImage">
<a href="../mapview/MapPolylineDashImageRepresentation/dashImage.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashimage</a>
→ <a href="../mapview/MapImage-class.html">/sdk-for-flutter-explore-mapview-mapimage-class</a>
</dt>
<dd>
  Image to be rendered in place of dash space.
It is stretched to fill whole polyline width and length of each dash.
Gets the image that is rendered in place of dash space.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="dashLength">
<a href="../mapview/MapPolylineDashImageRepresentation/dashLength.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashlength</a>
→ <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a>
</dt>
<dd>
  The map measure dependent length of a dash, to which image width is stretched.
Gets the map measure dependent length of a dash, to which image width is stretched.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="dashWidth">
<a href="../mapview/MapPolylineDashImageRepresentation/dashWidth.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-dashwidth</a>
→ <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a>
</dt>
<dd>
  The map measure dependent width of a dash, to which image height is stretched.
Gets the map measure dependent width of a dash, to which image height is stretched.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="gapLength">
<a href="../mapview/MapPolylineDashImageRepresentation/gapLength.html">/sdk-for-flutter-explore-mapview-mappolylinedashimagerepresentation-gaplength</a>
→ <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a>
</dt>
<dd>
  The map measure dependent length of a gap between dash images.
Gets the map measure dependent length of a gap between dash images.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapItemRepresentation/hashCode.html">/sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapItemRepresentation/runtimeType.html">/sdk-for-flutter-explore-mapview-mapitemrepresentation-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapItemRepresentation/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapitemrepresentation-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapItemRepresentation/toString.html">/sdk-for-flutter-explore-mapview-mapitemrepresentation-tostring</a>(<wbr/>)
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
<a href="../mapview/MapItemRepresentation/operator_equals.html">/sdk-for-flutter-explore-mapview-mapitemrepresentation-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">MapPolylineDashImageRepresentation class</li>
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
