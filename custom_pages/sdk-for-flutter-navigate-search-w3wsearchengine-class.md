---
title: "W3WSearchEngine class abstract"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- W3WSearchEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/W3WSearchEngine-class.html#constructors">Constructors</a></li>
<li><a href="search/W3WSearchEngine/W3WSearchEngine.html">W3WSearchEngine</a></li>
<li><a href="search/W3WSearchEngine/W3WSearchEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title inherited">
<a href="search/W3WSearchEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/W3WSearchEngine/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/W3WSearchEngine/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="search/W3WSearchEngine-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/W3WSearchEngine/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="search/W3WSearchEngine/searchByCoordinates.html">searchByCoordinates</a></li>
<li><a href="search/W3WSearchEngine/searchByWords.html">searchByWords</a></li>
<li class="inherited"><a href="search/W3WSearchEngine/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/W3WSearchEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/W3WSearchEngine/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">W3WSearchEngine class</li>
</ol>
<div class="self-name">W3WSearchEngine</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/W3WSearchEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>W3WSearchEngine class abstract</h1></div>
<section class="desc markdown">
<p>what3words is an alternative geocode system designed to identify any location on the planet.</p>
<p>The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which
has a three-word address. For example, the front door of HERE’s Berlin office is identified by
"///wage.mere.heap".
<code>W3WSearchEngine</code> allows you to convert 3 word addresses to coordinates and also coordinates
to 3 word addresses.</p>
<p><strong>Note:</strong> Using W3WSearchEngine requires a licence to access HERE what3words APIs.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="W3WSearchEngine">
/sdk-for-flutter-navigate-search-w3wsearchengine-w3wsearchengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="W3WSearchEngine.withSdkEngine">
/sdk-for-flutter-navigate-search-w3wsearchengine-w3wsearchengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-search-w3wsearchengine-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-w3wsearchengine-runtimetype
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
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-w3wsearchengine-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByCoordinates">
/sdk-for-flutter-navigate-search-w3wsearchengine-searchbycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, String? language, /sdk-for-flutter-navigate-search-w3wsearchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for a /sdk-for-flutter-navigate-search-w3wsquare-class, which includes
the 3 word address, that corresponds to the given coordinates.
  

</dd>
<dt class="callable" id="searchByWords">
/sdk-for-flutter-navigate-search-w3wsearchengine-searchbywords(<wbr/>String words, /sdk-for-flutter-navigate-search-w3wsearchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for a /sdk-for-flutter-navigate-search-w3wsquare-class that corresponds to
the given 3 words.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-w3wsearchengine-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-w3wsearchengine-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">W3WSearchEngine class</li>
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
