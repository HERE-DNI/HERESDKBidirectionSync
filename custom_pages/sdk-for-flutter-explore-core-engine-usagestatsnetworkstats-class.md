---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- UsageStatsNetworkStats-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/UsageStatsNetworkStats-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/UsageStatsNetworkStats/UsageStatsNetworkStats.html">UsageStatsNetworkStats</a></li>
<li class="section-title">
<a href="core.engine/UsageStatsNetworkStats-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core.engine/UsageStatsNetworkStats/hashCode.html">hashCode</a></li>
<li><a href="core.engine/UsageStatsNetworkStats/methodCall.html">methodCall</a></li>
<li><a href="core.engine/UsageStatsNetworkStats/receivedBytes.html">receivedBytes</a></li>
<li><a href="core.engine/UsageStatsNetworkStats/requestCounter.html">requestCounter</a></li>
<li class="inherited"><a href="core.engine/UsageStatsNetworkStats/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/UsageStatsNetworkStats/sentBytes.html">sentBytes</a></li>
<li class="section-title inherited"><a href="core.engine/UsageStatsNetworkStats-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/UsageStatsNetworkStats/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/UsageStatsNetworkStats/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core.engine/UsageStatsNetworkStats-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core.engine/UsageStatsNetworkStats/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">UsageStatsNetworkStats class</li>
</ol>
<div class="self-name">UsageStatsNetworkStats</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/UsageStatsNetworkStats-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>UsageStatsNetworkStats class</h1></div>
<section class="desc markdown">
<p>Provides network statistics in bytes per method.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="UsageStatsNetworkStats">
<a href="../core.engine/UsageStatsNetworkStats/UsageStatsNetworkStats.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-usagestatsnetworkstats</a>(int sentBytes, int receivedBytes, String methodCall, int requestCounter)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../core.engine/UsageStatsNetworkStats/hashCode.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="methodCall">
<a href="../core.engine/UsageStatsNetworkStats/methodCall.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-methodcall</a>
↔ String
</dt>
<dd>
  Name or description of the method being called.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="receivedBytes">
<a href="../core.engine/UsageStatsNetworkStats/receivedBytes.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-receivedbytes</a>
↔ int
</dt>
<dd>
  Number of bytes received from the network.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="requestCounter">
<a href="../core.engine/UsageStatsNetworkStats/requestCounter.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-requestcounter</a>
↔ int
</dt>
<dd>
  Amount of calls for particular family of methodCall.
methodCall in this case is considered as base request,
additional query params are ignored, all calculated as one request.
e.g. <a href="https://search.hereapi.com/someparams">https://search.hereapi.com/someparams</a> and <a href="https://search.hereapi.com/someparams2">https://search.hereapi.com/someparams2</a>
will be considered as 1 methodCall, and requestCounter is 2.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/UsageStatsNetworkStats/runtimeType.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sentBytes">
<a href="../core.engine/UsageStatsNetworkStats/sentBytes.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-sentbytes</a>
↔ int
</dt>
<dd>
  Number of bytes sent over the network.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/UsageStatsNetworkStats/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/UsageStatsNetworkStats/toString.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-tostring</a>(<wbr/>)
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
<a href="../core.engine/UsageStatsNetworkStats/operator_equals.html">/sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">UsageStatsNetworkStats class</li>
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
