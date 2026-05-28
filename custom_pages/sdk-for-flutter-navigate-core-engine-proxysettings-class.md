---
title: "ProxySettings class"
slug: "sdk-for-flutter-navigate-core-engine-proxysettings-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ProxySettings-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/ProxySettings-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/ProxySettings/ProxySettings.html">ProxySettings</a></li>
<li class="section-title">
<a href="core.engine/ProxySettings-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/ProxySettings/credentials.html">credentials</a></li>
<li><a href="core.engine/ProxySettings/hashCode.html">hashCode</a></li>
<li><a href="core.engine/ProxySettings/ipAddress.html">ipAddress</a></li>
<li><a href="core.engine/ProxySettings/networkInterface.html">networkInterface</a></li>
<li><a href="core.engine/ProxySettings/port.html">port</a></li>
<li class="inherited"><a href="core.engine/ProxySettings/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/ProxySettings/type.html">type</a></li>
<li class="section-title inherited"><a href="core.engine/ProxySettings-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/ProxySettings/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/ProxySettings/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/ProxySettings-class.html#operators">Operators</a></li>
<li><a href="core.engine/ProxySettings/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li class="self-crumb">ProxySettings class</li>
</ol>
<div class="self-name">ProxySettings</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/ProxySettings-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ProxySettings class</h1></div>
<section class="desc markdown">
<p>Proxy configuration for the HERE SDK network that is applied per request.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ProxySettings">
/sdk-for-flutter-navigate-core-engine-proxysettings-proxysettings(/sdk-for-flutter-navigate-core-engine-proxysettingsproxytype type, InternetAddress ipAddress, int port)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="credentials">
/sdk-for-flutter-navigate-core-engine-proxysettings-credentials
↔ /sdk-for-flutter-navigate-core-engine-proxysettingscredentials-class?
</dt>
<dd>
  Optional field to define credentials to authenticate a user to the proxy server.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-engine-proxysettings-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="ipAddress">
/sdk-for-flutter-navigate-core-engine-proxysettings-ipaddress
↔ InternetAddress
</dt>
<dd>
  Represents the IP Address of the proxy server.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="networkInterface">
/sdk-for-flutter-navigate-core-engine-proxysettings-networkinterface
↔ String?
</dt>
<dd>
  Network interface. It's taken into account on Android platform when IPv6 is used.
Default value is "wlan0". If not set then no interface is used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="port">
/sdk-for-flutter-navigate-core-engine-proxysettings-port
↔ int
</dt>
<dd>
  Represents the port number of the proxy server.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-engine-proxysettings-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-core-engine-proxysettings-type
↔ /sdk-for-flutter-navigate-core-engine-proxysettingsproxytype
</dt>
<dd>
  Represents the type of the proxy server.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-engine-proxysettings-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-engine-proxysettings-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-engine-proxysettings-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ProxySettings class</li>
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
