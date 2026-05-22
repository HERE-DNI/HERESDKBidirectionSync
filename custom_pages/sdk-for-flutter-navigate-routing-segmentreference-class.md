---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-segmentreference-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentReference-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-segmentreference-segmentreference([String segmentId = "", /sdk-for-flutter-navigate-routing-traveldirection travelDirection = TravelDirection.bidirectional, double offsetStart = 0.0, double offsetEnd = 1.0, int tilePartitionId = 0, int? localId = 0])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="SegmentReference.withDefaults">
/sdk-for-flutter-navigate-routing-segmentreference-segmentreference-withdefaults()
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
/sdk-for-flutter-navigate-routing-segmentreference-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="localId">
/sdk-for-flutter-navigate-routing-segmentreference-localid
↔ int?
</dt>
<dd>
  Local ID of the segment inside the OCM tile.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offsetEnd">
/sdk-for-flutter-navigate-routing-segmentreference-offsetend
↔ double
</dt>
<dd>
  The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offsetStart">
/sdk-for-flutter-navigate-routing-segmentreference-offsetstart
↔ double
</dt>
<dd>
  The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-segmentreference-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentId">
/sdk-for-flutter-navigate-routing-segmentreference-segmentid
↔ String
</dt>
<dd>
  Topology segment id representing a unique identifier within the HERE platform catalogs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tilePartitionId">
/sdk-for-flutter-navigate-routing-segmentreference-tilepartitionid
↔ int
</dt>
<dd>
  HERE tile partition id (Morton-encoding + level indicator) of the segment.
As in HERE Map Content.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="travelDirection">
/sdk-for-flutter-navigate-routing-segmentreference-traveldirection
↔ /sdk-for-flutter-navigate-routing-traveldirection
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
/sdk-for-flutter-navigate-routing-segmentreference-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-segmentreference-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-segmentreference-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-navigate-routing-segmentreference-fromstring(<wbr/>String segmentRef)
    → /sdk-for-flutter-navigate-routing-segmentreference-class?

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
