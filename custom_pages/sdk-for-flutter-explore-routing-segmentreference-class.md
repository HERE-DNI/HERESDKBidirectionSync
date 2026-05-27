---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-segmentreference-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SegmentReference-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/SegmentReference-class.html#constructors">Constructors</a></li>
<li><a href="routing/SegmentReference/SegmentReference.html">SegmentReference</a></li>
<li><a href="routing/SegmentReference/SegmentReference.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="routing/SegmentReference-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/SegmentReference/hashCode.html">hashCode</a></li>
<li><a href="routing/SegmentReference/localId.html">localId</a></li>
<li><a href="routing/SegmentReference/offsetEnd.html">offsetEnd</a></li>
<li><a href="routing/SegmentReference/offsetStart.html">offsetStart</a></li>
<li class="inherited"><a href="routing/SegmentReference/runtimeType.html">runtimeType</a></li>
<li><a href="routing/SegmentReference/segmentId.html">segmentId</a></li>
<li><a href="routing/SegmentReference/tilePartitionId.html">tilePartitionId</a></li>
<li><a href="routing/SegmentReference/travelDirection.html">travelDirection</a></li>
<li class="section-title inherited"><a href="routing/SegmentReference-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/SegmentReference/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/SegmentReference/toString.html">toString</a></li>
<li class="section-title"><a href="routing/SegmentReference-class.html#operators">Operators</a></li>
<li><a href="routing/SegmentReference/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="routing/SegmentReference-class.html#static-methods">Static methods</a></li>
<li><a href="routing/SegmentReference/fromString.html">fromString</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">SegmentReference class</li>
</ol>
<div class="self-name">SegmentReference</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SegmentReference-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SegmentReference class</h1></div>
<section class="desc markdown">
<p>Reference to a segment id with a travel direction.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SegmentReference">
<a href="../routing/SegmentReference/SegmentReference.html">/sdk-for-flutter-explore-routing-segmentreference-segmentreference</a>([String segmentId = "", <a href="../routing/TravelDirection.html">/sdk-for-flutter-explore-routing-traveldirection</a> travelDirection = TravelDirection.bidirectional, double offsetStart = 0.0, double offsetEnd = 1.0, int tilePartitionId = 0, int? localId = 0])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="SegmentReference.withDefaults">
<a href="../routing/SegmentReference/SegmentReference.withDefaults.html">/sdk-for-flutter-explore-routing-segmentreference-segmentreference-withdefaults</a>()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../routing/SegmentReference/hashCode.html">/sdk-for-flutter-explore-routing-segmentreference-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="localId">
<a href="../routing/SegmentReference/localId.html">/sdk-for-flutter-explore-routing-segmentreference-localid</a>
↔ int?
</dt>
<dd>
  Local ID of the segment inside the OCM tile.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offsetEnd">
<a href="../routing/SegmentReference/offsetEnd.html">/sdk-for-flutter-explore-routing-segmentreference-offsetend</a>
↔ double
</dt>
<dd>
  The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offsetStart">
<a href="../routing/SegmentReference/offsetStart.html">/sdk-for-flutter-explore-routing-segmentreference-offsetstart</a>
↔ double
</dt>
<dd>
  The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/SegmentReference/runtimeType.html">/sdk-for-flutter-explore-routing-segmentreference-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentId">
<a href="../routing/SegmentReference/segmentId.html">/sdk-for-flutter-explore-routing-segmentreference-segmentid</a>
↔ String
</dt>
<dd>
  Topology segment id representing a unique identifier within the HERE platform catalogs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tilePartitionId">
<a href="../routing/SegmentReference/tilePartitionId.html">/sdk-for-flutter-explore-routing-segmentreference-tilepartitionid</a>
↔ int
</dt>
<dd>
  HERE tile partition id (Morton-encoding + level indicator) of the segment.
As in HERE Map Content.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="travelDirection">
<a href="../routing/SegmentReference/travelDirection.html">/sdk-for-flutter-explore-routing-segmentreference-traveldirection</a>
↔ <a href="../routing/TravelDirection.html">/sdk-for-flutter-explore-routing-traveldirection</a>
</dt>
<dd>
  Travel direction of the segment.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/SegmentReference/noSuchMethod.html">/sdk-for-flutter-explore-routing-segmentreference-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/SegmentReference/toString.html">/sdk-for-flutter-explore-routing-segmentreference-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../routing/SegmentReference/operator_equals.html">/sdk-for-flutter-explore-routing-segmentreference-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromString">
<a href="../routing/SegmentReference/fromString.html">/sdk-for-flutter-explore-routing-segmentreference-fromstring</a>(<wbr/>String segmentRef)
    → <a href="../routing/SegmentReference-class.html">/sdk-for-flutter-explore-routing-segmentreference-class</a>?

</dt>
<dd>
  Returns an instance of this struct from a string if it's well-formatted, <code>null</code> otherwise.
  

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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">SegmentReference class</li>
</ol>
<h5>routing library</h5>
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
