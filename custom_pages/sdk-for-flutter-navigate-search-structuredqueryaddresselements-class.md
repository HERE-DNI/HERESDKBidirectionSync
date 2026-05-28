---
title: "StructuredQueryAddressElements class"
slug: "sdk-for-flutter-navigate-search-structuredqueryaddresselements-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- StructuredQueryAddressElements-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/StructuredQueryAddressElements-class.html#constructors">Constructors</a></li>
<li><a href="search/StructuredQueryAddressElements/StructuredQueryAddressElements.html">StructuredQueryAddressElements</a></li>
<li class="section-title">
<a href="search/StructuredQueryAddressElements-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/StructuredQueryAddressElements/city.html">city</a></li>
<li><a href="search/StructuredQueryAddressElements/country.html">country</a></li>
<li><a href="search/StructuredQueryAddressElements/district.html">district</a></li>
<li><a href="search/StructuredQueryAddressElements/hashCode.html">hashCode</a></li>
<li><a href="search/StructuredQueryAddressElements/postalCode.html">postalCode</a></li>
<li class="inherited"><a href="search/StructuredQueryAddressElements/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/StructuredQueryAddressElements-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/StructuredQueryAddressElements/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/StructuredQueryAddressElements/toString.html">toString</a></li>
<li class="section-title"><a href="search/StructuredQueryAddressElements-class.html#operators">Operators</a></li>
<li><a href="search/StructuredQueryAddressElements/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">StructuredQueryAddressElements class</li>
</ol>
<div class="self-name">StructuredQueryAddressElements</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/StructuredQueryAddressElements-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>StructuredQueryAddressElements class</h1></div>
<section class="desc markdown">
<p>Defines query address elements which will be used to build address hierarchy during searches.</p>
<p>It is advised to provide at least one intermediate address element when a large address element is provided
for small admin area searches.
For example if a user is building a query for a street and providing only country as an address element,
consider providing city along with it.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="StructuredQueryAddressElements">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-structuredqueryaddresselements()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="city">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-city
↔ String?
</dt>
<dd>
  An optional field of city name, which will be used to get the results only from the given city.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="country">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-country
↔ String?
</dt>
<dd>
  An optional field of country name or code, which will be used to get the results only from the given country.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="district">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-district
↔ String?
</dt>
<dd>
  An optional field of district, which will be used to get the results only from the given district.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="postalCode">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-postalcode
↔ String?
</dt>
<dd>
  An optional field of postal code, which will be used to get the results only within the given postal code.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-runtimetype
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
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-structuredqueryaddresselements-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">StructuredQueryAddressElements class</li>
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
