---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-engineoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EngineOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/EngineOptions-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/EngineOptions/EngineOptions.html">EngineOptions</a></li>
<li class="section-title">
<a href="core.engine/EngineOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/EngineOptions/customAuthenticationMode.html">customAuthenticationMode</a></li>
<li><a href="core.engine/EngineOptions/customBaseUrl.html">customBaseUrl</a></li>
<li><a href="core.engine/EngineOptions/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core.engine/EngineOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/EngineOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/EngineOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/EngineOptions/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/EngineOptions-class.html#operators">Operators</a></li>
<li><a href="core.engine/EngineOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">EngineOptions class</li>
</ol>
<div class="self-name">EngineOptions</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/EngineOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EngineOptions class</h1></div>
<section class="desc markdown">
<p>Specifies several options specific to different engines.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EngineOptions">
<a href="../core.engine/EngineOptions/EngineOptions.html">/sdk-for-flutter-explore-core-engine-engineoptions-engineoptions</a>()
</dt>
<dd>
          Creates a new instance with default values.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="customAuthenticationMode">
<a href="../core.engine/EngineOptions/customAuthenticationMode.html">/sdk-for-flutter-explore-core-engine-engineoptions-customauthenticationmode</a>
↔ <a href="../core.engine/AuthenticationMode-class.html">/sdk-for-flutter-explore-core-engine-authenticationmode-class</a>?
</dt>
<dd>
  Allows bearer authentication mode for engines. This mode adds a header
("Authorization", "Bearer $Token") to each online request made by the
module the object is added to. The token can either be provided directly
or retrieved via key/secret from a dedicated backend.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="customBaseUrl">
<a href="../core.engine/EngineOptions/customBaseUrl.html">/sdk-for-flutter-explore-core-engine-engineoptions-custombaseurl</a>
↔ String?
</dt>
<dd>
  Allows engines to use custom base URLs for alternative services.
By default, the available endpoints use HERE backend endpoints.
If unsupported base URLs are specified, the related features will become non-functional.
Please contact your HERE representative to learn about possible custom base URL usage options
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/EngineOptions/hashCode.html">/sdk-for-flutter-explore-core-engine-engineoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/EngineOptions/runtimeType.html">/sdk-for-flutter-explore-core-engine-engineoptions-runtimetype</a>
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
<a href="../core.engine/EngineOptions/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-engineoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/EngineOptions/toString.html">/sdk-for-flutter-explore-core-engine-engineoptions-tostring</a>(<wbr/>)
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
<a href="../core.engine/EngineOptions/operator_equals.html">/sdk-for-flutter-explore-core-engine-engineoptions-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">EngineOptions class</li>
</ol>
<h5>core.engine library</h5>
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
