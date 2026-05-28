---
title: "SDKVersion class"
slug: "sdk-for-flutter-navigate-core-engine-sdkversion-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SDKVersion-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/SDKVersion-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/SDKVersion/SDKVersion.html">SDKVersion</a></li>
<li class="section-title">
<a href="core.engine/SDKVersion-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/SDKVersion/backendConfig.html">backendConfig</a></li>
<li><a href="core.engine/SDKVersion/hashCode.html">hashCode</a></li>
<li><a href="core.engine/SDKVersion/productVariant.html">productVariant</a></li>
<li class="inherited"><a href="core.engine/SDKVersion/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/SDKVersion/versionBuild.html">versionBuild</a></li>
<li><a href="core.engine/SDKVersion/versionGeneration.html">versionGeneration</a></li>
<li><a href="core.engine/SDKVersion/versionMajor.html">versionMajor</a></li>
<li><a href="core.engine/SDKVersion/versionMinor.html">versionMinor</a></li>
<li><a href="core.engine/SDKVersion/versionName.html">versionName</a></li>
<li><a href="core.engine/SDKVersion/versionPatch.html">versionPatch</a></li>
<li><a href="core.engine/SDKVersion/versionTag.html">versionTag</a></li>
<li class="section-title inherited"><a href="core.engine/SDKVersion-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/SDKVersion/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/SDKVersion/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/SDKVersion-class.html#operators">Operators</a></li>
<li><a href="core.engine/SDKVersion/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li class="self-crumb">SDKVersion class</li>
</ol>
<div class="self-name">SDKVersion</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKVersion-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SDKVersion class</h1></div>
<section class="desc markdown">
<p>The <code>SDKVersion</code> represents version information for an SDK product.</p>
<p>It encapsulates
various attributes related to the version, including product variant, version details and
backend configuration.
Please note, <code>sdk.core.engine.SDKBuildInformation</code> can be used to get <code>SDKVersion</code>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SDKVersion">
/sdk-for-flutter-navigate-core-engine-sdkversion-sdkversion(String productVariant, String versionName, int versionGeneration, int versionMajor, int versionMinor, int versionPatch, int versionBuild, String versionTag, String backendConfig)
</dt>
<dd>
          Creates a new SDK version instance from the provided parameter values.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="backendConfig">
/sdk-for-flutter-navigate-core-engine-sdkversion-backendconfig
↔ String
</dt>
<dd>
  Backend config
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-engine-sdkversion-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="productVariant">
/sdk-for-flutter-navigate-core-engine-sdkversion-productvariant
↔ String
</dt>
<dd>
  Product variant.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-engine-sdkversion-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="versionBuild">
/sdk-for-flutter-navigate-core-engine-sdkversion-versionbuild
↔ int
</dt>
<dd>
  Build number.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionGeneration">
/sdk-for-flutter-navigate-core-engine-sdkversion-versiongeneration
↔ int
</dt>
<dd>
  Generation number.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionMajor">
/sdk-for-flutter-navigate-core-engine-sdkversion-versionmajor
↔ int
</dt>
<dd>
  Major version number.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionMinor">
/sdk-for-flutter-navigate-core-engine-sdkversion-versionminor
↔ int
</dt>
<dd>
  Minor version number.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionName">
/sdk-for-flutter-navigate-core-engine-sdkversion-versionname
↔ String
</dt>
<dd>
  Version information as string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionPatch">
/sdk-for-flutter-navigate-core-engine-sdkversion-versionpatch
↔ int
</dt>
<dd>
  Patch number.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="versionTag">
/sdk-for-flutter-navigate-core-engine-sdkversion-versiontag
↔ String
</dt>
<dd>
  Version tag.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-engine-sdkversion-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-engine-sdkversion-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-engine-sdkversion-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li class="self-crumb">SDKVersion class</li>
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
`
}</HTMLBlock>
