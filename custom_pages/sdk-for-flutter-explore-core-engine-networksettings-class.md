---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-networksettings-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- NetworkSettings-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/NetworkSettings-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/NetworkSettings/NetworkSettings.html">NetworkSettings</a></li>
<li class="section-title">
<a href="core.engine/NetworkSettings-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/NetworkSettings/certificates.html">certificates</a></li>
<li><a href="core.engine/NetworkSettings/diagnosticsOutputPath.html">diagnosticsOutputPath</a></li>
<li><a href="core.engine/NetworkSettings/domainNameSystemServers.html">domainNameSystemServers</a></li>
<li><a href="core.engine/NetworkSettings/hashCode.html">hashCode</a></li>
<li><a href="core.engine/NetworkSettings/proxySettings.html">proxySettings</a></li>
<li class="inherited"><a href="core.engine/NetworkSettings/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/NetworkSettings-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/NetworkSettings/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/NetworkSettings/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/NetworkSettings-class.html#operators">Operators</a></li>
<li><a href="core.engine/NetworkSettings/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">NetworkSettings class</li>
</ol>
<div class="self-name">NetworkSettings</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/NetworkSettings-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>NetworkSettings class</h1></div>
<section class="desc markdown">
<p>Network configuration to be used by <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> during the initialization.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="NetworkSettings">
<a href="../core.engine/NetworkSettings/NetworkSettings.html">/sdk-for-flutter-explore-core-engine-networksettings-networksettings</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="certificates">
<a href="../core.engine/NetworkSettings/certificates.html">/sdk-for-flutter-explore-core-engine-networksettings-certificates</a>
↔ <a href="../core.engine/CertificateSettings-class.html">/sdk-for-flutter-explore-core-engine-certificatesettings-class</a>?
</dt>
<dd>
  Certificate settings to use on Android
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="diagnosticsOutputPath">
<a href="../core.engine/NetworkSettings/diagnosticsOutputPath.html">/sdk-for-flutter-explore-core-engine-networksettings-diagnosticsoutputpath</a>
↔ String?
</dt>
<dd>
  Absolute file path to be used for redirecting CURL verbose output.
The application must have read and write permissions to the given path.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="domainNameSystemServers">
<a href="../core.engine/NetworkSettings/domainNameSystemServers.html">/sdk-for-flutter-explore-core-engine-networksettings-domainnamesystemservers</a>
↔ List&lt;<wbr/><a href="../core/NetworkEndpoint-class.html">/sdk-for-flutter-explore-core-networkendpoint-class</a>&gt;
</dt>
<dd>
  Domain Name Server list. This list fully replaces embedded mechanism to detect DNS.
The order is important. To reduce response time make sure that most probably servers
are at the beginning.
Currently only IPv4 is supported.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/NetworkSettings/hashCode.html">/sdk-for-flutter-explore-core-engine-networksettings-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="proxySettings">
<a href="../core.engine/NetworkSettings/proxySettings.html">/sdk-for-flutter-explore-core-engine-networksettings-proxysettings</a>
↔ <a href="../core.engine/ProxySettings-class.html">/sdk-for-flutter-explore-core-engine-proxysettings-class</a>?
</dt>
<dd>
  Proxy settings. It can be later accessed or changed with <a href="../core.engine/SDKNativeEngine/proxySettings.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-proxysettings</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/NetworkSettings/runtimeType.html">/sdk-for-flutter-explore-core-engine-networksettings-runtimetype</a>
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
<a href="../core.engine/NetworkSettings/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-networksettings-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/NetworkSettings/toString.html">/sdk-for-flutter-explore-core-engine-networksettings-tostring</a>(<wbr/>)
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
<a href="../core.engine/NetworkSettings/operator_equals.html">/sdk-for-flutter-explore-core-engine-networksettings-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">NetworkSettings class</li>
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
