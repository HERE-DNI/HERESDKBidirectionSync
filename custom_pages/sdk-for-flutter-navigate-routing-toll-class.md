---
title: "Toll class"
slug: "sdk-for-flutter-navigate-routing-toll-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Toll-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Toll-class.html#constructors">Constructors</a></li>
<li><a href="routing/Toll/Toll.html">Toll</a></li>
<li class="section-title">
<a href="routing/Toll-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Toll/countryCode.html">countryCode</a></li>
<li><a href="routing/Toll/fares.html">fares</a></li>
<li><a href="routing/Toll/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/Toll/runtimeType.html">runtimeType</a></li>
<li><a href="routing/Toll/tollSystems.html">tollSystems</a></li>
<li class="section-title inherited"><a href="routing/Toll-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/Toll/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Toll/toString.html">toString</a></li>
<li class="section-title"><a href="routing/Toll-class.html#operators">Operators</a></li>
<li><a href="routing/Toll/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">Toll class</li>
</ol>
<div class="self-name">Toll</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Toll-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Toll class</h1></div>
<section class="desc markdown">
<p>This struct presents all the data for a toll.</p>
<p><strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available for the Navigate license. If you're using the
<code>RoutingEngine</code>, this feature is considered to be stable.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Toll">
/sdk-for-flutter-navigate-routing-toll-toll(String countryCode, List&lt;<wbr/>String&gt; tollSystems, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-tollfare-class&gt; fares)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="countryCode">
/sdk-for-flutter-navigate-routing-toll-countrycode
↔ String
</dt>
<dd>
  The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fares">
/sdk-for-flutter-navigate-routing-toll-fares
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-tollfare-class&gt;
</dt>
<dd>
  The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle
characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the
list will contain more than one toll fare. Note that this list contains at least one element, i.e. it
is never empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-toll-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-toll-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tollSystems">
/sdk-for-flutter-navigate-routing-toll-tollsystems
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Names of the multiple toll systems which are associated with the toll, e.g. ["ATLANDES“, "ASF", "COFIROUTE"].
When the toll information covers several toll roads and the toll system of the each road is different,
all toll system names are listed here and the last element will be one of the exit toll booth.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-toll-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-toll-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-toll-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">Toll class</li>
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
`
}</HTMLBlock>
