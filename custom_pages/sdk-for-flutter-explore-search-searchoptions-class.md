---
title: "SearchOptions class"
slug: "sdk-for-flutter-explore-search-searchoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/SearchOptions-class.html#constructors">Constructors</a></li>
<li><a href="search/SearchOptions/SearchOptions.html">SearchOptions</a></li>
<li class="section-title">
<a href="search/SearchOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/SearchOptions/distributedResults.html">distributedResults</a></li>
<li><a href="search/SearchOptions/hashCode.html">hashCode</a></li>
<li><a href="search/SearchOptions/highDensityEncodingEnabled.html">highDensityEncodingEnabled</a></li>
<li><a href="search/SearchOptions/languageCode.html">languageCode</a></li>
<li><a href="search/SearchOptions/maxItems.html">maxItems</a></li>
<li class="inherited"><a href="search/SearchOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/SearchOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/SearchOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/SearchOptions/toString.html">toString</a></li>
<li class="section-title"><a href="search/SearchOptions-class.html#operators">Operators</a></li>
<li><a href="search/SearchOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">SearchOptions class</li>
</ol>
<div class="self-name">SearchOptions</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SearchOptions class</h1></div>
<section class="desc markdown">
<p>Encapsulates options that control the behavior of search and suggest operations.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SearchOptions">
/sdk-for-flutter-explore-search-searchoptions-searchoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distributedResults">
/sdk-for-flutter-explore-search-searchoptions-distributedresults
↔ bool
</dt>
<dd>
  Indicates if search along the route should produce well-distributed results.
It is only supported for:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-search-searchoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="highDensityEncodingEnabled">
/sdk-for-flutter-explore-search-searchoptions-highdensityencodingenabled
↔ bool
</dt>
<dd>
  Allows enabling high density encoding of relevant parameters.
For now, it only affects input parameters of type <code>GeoCorridor</code>.
Only supported for search in <code>SearchEngine</code>, otherwise it is ignored.
<strong>Note:</strong> This is a closed-alpha release of this feature, so there could be a few bugs and
unexpected behaviors.
Related APIs may change for new releases without a deprecation process.
Only participants of the closed-alpha group can get access from HERE to use this feature,
otherwise, a /sdk-for-flutter-explore-search-searcherror will be propagated in callbacks.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="languageCode">
/sdk-for-flutter-explore-search-searchoptions-languagecode
↔ /sdk-for-flutter-explore-core-languagecode?
</dt>
<dd>
  The preferred language of the result. When unset or unsupported language is chosen,
results will be returned in their local language.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxItems">
/sdk-for-flutter-explore-search-searchoptions-maxitems
↔ int?
</dt>
<dd>
  The maximum number of items in the response. It should be in the range [1, 100].
When not set, results will be limited to 20.
For location search (reverse geocode) by default results limited to 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-searchoptions-runtimetype
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
/sdk-for-flutter-explore-search-searchoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-searchoptions-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-searchoptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li class="self-crumb">SearchOptions class</li>
</ol>
<h5>search library</h5>
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
